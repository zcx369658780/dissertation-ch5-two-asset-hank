# PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT

## Rule Status

- Type: Project governance rule
- Scope: GitHub capability detection, authority routing, task publication workflow
- Applies to: `zcx369658780/dissertation-ch5-two-asset-hank`

---

# 1. Purpose

This rule prevents GitHub capability misclassification in GitHub-governed research workflows.

The project MUST distinguish between:

1. inability to verify a GitHub mutation;
2. inability to perform a GitHub mutation.

These are different states.

---

# 2. Core Principle

The following reasoning pattern is forbidden:

```
Cannot claim an unverified commit
        =>
Cannot execute GitHub operations
```

Correct interpretation:

```
Cannot claim an unverified commit
        =>
Must execute the authorized operation first, then verify evidence
```

---

# 3. Capability Check Order

Before stating that GitHub publication cannot be performed:

1. Check available GitHub repository operations.
2. Check target repository accessibility.
3. Determine whether the requested operation is within role authority.
4. Execute only authorized mutation.
5. Read back GitHub state after mutation.

Do not infer capability from historical workflow assumptions.

---

# 4. Authorized Governance Operations

Within reviewer/task-issuer authority, allowed operations include:

- create authorized task files;
- create governance documents;
- update repository rule files when required;
- synchronize governance metadata;
- verify live repository state.

GPT MUST NOT:

- claim mutation before execution;
- claim commit hash without evidence;
- bypass task authority.

---

# 5. Task Authority Workflow

A task becomes executable only after live GitHub publication.

Required sequence:

```
Task draft
    ↓
GitHub publication
    ↓
Fresh GitHub read-back verification
    ↓
Codex execution prompt
```

Chat content alone is not execution authority.

---

# 6. Post-Mutation Verification

After every GitHub mutation, verify:

- repository identity;
- branch/default branch;
- file path;
- file existence;
- content identity.

Successful mutation response alone is insufficient.

---

# 7. Scientific Boundary

GitHub governance authority does NOT authorize scientific actions.

The following still require independent scientific task authority:

- equation specification;
- HJB/KFE implementation;
- solver changes;
- calibration changes;
- numerical experiments;
- Results claims.

---

# 8. Historical Failure Prevention

Avoid:

```
Historical workflow memory
        ↓
Assume GitHub unavailable
        ↓
Generate task draft only
        ↓
Send Codex without live authority
```

Use capability-first routing instead.

---

# 9. Acceptance Rule

A governance publication is complete only when:

1. GitHub mutation succeeds;
2. GitHub read-back confirms the artifact;
3. downstream agents can independently discover the authority file.
