"""Explicit ownership, double-entry cash flows and national consolidation."""
from math import isfinite, fsum
from dataclasses import dataclass, field
from .reconciled_household_prices import check_income

@dataclass
class Journal:
    entries: list = field(default_factory=list)

    def transfer(self, payer, payee, amount, category, province=None):
        if not isfinite(amount) or payer == payee:
            raise ValueError("invalid cash entry")
        if amount < 0:
            payer, payee, amount = payee, payer, -amount
        self.entries.append(dict(payer=payer,payee=payee,amount=amount,
                                 category=category,province=province))

    def balances(self):
        accounts = {e[k] for e in self.entries for k in ("payer","payee")}
        return {a: fsum((e["amount"] if e["payee"] == a else
                        -e["amount"] if e["payer"] == a else 0)
                       for e in self.entries) for a in sorted(accounts)}

def capital_claims(total, private, public, raw_return, *, used_return=None, claimed=None):
    if min(total, private, public) < 0 or not all(isfinite(x) for x in (total,private,public,raw_return)):
        raise ValueError("invalid ownership")
    if abs(total-private-public) > 1e-12*max(1,total):
        raise ValueError("capital counted twice or unassigned")
    if used_return is not None and used_return != raw_return:
        raise ValueError("unadopted clip distribution refused")
    payouts = (private*raw_return, public*raw_return)
    if claimed is not None and any(abs(x-y)>1e-12*max(1,abs(x)) for x,y in zip(payouts,claimed)):
        raise ValueError("duplicate capital return allocation")
    return payouts

def record_asset_gap(journal, amount, owner=None, *, recipients=None):
    if amount and (type(owner) is not str or owner not in ("government","intermediary","resource")):
        raise ValueError("asset gap has no unique economic owner")
    expected = {"government":"government","intermediary":"intermediary","resource":"resource"}
    if recipients is not None and list(recipients) != [expected.get(owner)]:
        raise ValueError("AtTax double booking rejected")
    if amount:
        journal.transfer("households", expected[owner], amount, "asset_gap")

def record_wage(journal, gross, tax_rate, cost_rate=0, cost_owner=None, province=None):
    mobility = gross*cost_rate
    if mobility and cost_owner not in ("government_fee","intermediary","resource"):
        raise ValueError("ambiguous mobility ownership")
    net = gross*(1-tax_rate-cost_rate)
    check_income(gross,net,gross*tax_rate,mobility)
    journal.transfer("firms","households",gross,"gross_wages",province)
    journal.transfer("households","government",gross*tax_rate,"wage_tax",province)
    if mobility:
        recipient = "government" if cost_owner=="government_fee" else cost_owner
        journal.transfer("households",recipient,mobility,"mobility",province)
    return net

def transfer_total(population, means):
    if len(population) != len(means) or any(n<=0 for n in population):
        raise ValueError("population axis mismatch")
    return fsum(n*t for n,t in zip(population,means))

def government_interest(net_liquid_assets, rate, issuer):
    if issuer != "national_government":
        raise ValueError("Bt is not automatically government debt")
    return net_liquid_assets*rate

def provincial_analysis(case, result):
    """Analytical attribution only: one government, not provincial debt issuers.

    Wage/corporate/public income and purchases use workplace j; population,
    transfers and attributed liquid interest use resident i. The national sum
    is the unified government's cash balance.
    """
    if case.get("scenario") != "SYNTHETIC_SCENARIO":
        raise ValueError("only explicit artificial account attribution")
    rows=[]
    for i in range(case["n"]):
        wages=result["w"][i]*result["L"][i]*case["tax"]
        corporate=(1-case["markup"])*result["Y"][i]*case["corporate_tax"]
        public=case["Kg"][i]*result["returns"][i]
        transfer=case["N"][i]*result["transfer"]
        interest=case["N"][i]*fsum(s["p"]*s["b"] for s in case["mu"][i])*case["rb"]
        purchases=case["G_share"]*result["Y"][i]
        rows.append(dict(province=i,wage_tax=wages,corporate_tax=corporate,
            public_net_return=public,resident_transfer=transfer,
            attributed_national_debt_interest=interest,purchases=purchases,
            net_contribution=wages+corporate+public-transfer-interest-purchases))
    return rows
