# CH5_TWO_ASSET_HANK_R1A_MATLAB_ECONOMIC_PROVENANCE_AND_EQUATION_BINDING_GATE

Repository:

zcx369658780/dissertation-ch5-two-asset-hank

Stage:

R1A Economic Provenance Binding

## Purpose

Bind authoritative MATLAB/dissertation sources before freezing the two-asset HANK economic equations.

This is a provenance and specification task, not an implementation task.

The objective is to identify the authoritative economic objects and equations required for the new Python reconstruction.

## Scope

Allowed:

- read designated MATLAB source files;
- read dissertation equation sources;
- build variable dictionaries;
- build equation provenance maps;
- record unresolved ambiguities.

Forbidden:

- writing solver code;
- modifying MATLAB source;
- copying DSH implementation as authority;
- running HJB/KFE solver;
- calibration tuning;
- producing Results claims.

## Required Outputs

Create a provenance report containing:

## 1. Source Inventory

For every source:

- file path;
- version/commit/hash if available;
- authority level;
- purpose.

Classify sources:

- dissertation equations;
- MATLAB implementation provenance;
- supplementary notes.

## 2. Variable Dictionary

Freeze meanings, units, and source provenance for:

- a: illiquid asset;
- b: liquid asset;
- z: productivity state;
- c: consumption;
- l: labor;
- d: asset transfer/control.

## 3. Equation Binding

Identify authoritative forms for:

- household budget constraint;
- asset drift equations;
- liquid asset evolution;
- illiquid asset evolution;
- adjustment cost chi(d,a);
- income process and transition matrix Q_z;
- boundary constraints.

Do not infer missing equations.

## 4. Ambiguity Ledger

For every unresolved item record:

- missing information;
- competing interpretations;
- required owner decision.

## 5. Python Reconstruction Implications

Map:

RETAIN:
- economic mechanisms that must remain;

REDESIGN:
- numerical implementation allowed to change;

DROP:
- mechanisms outside current scope;

UNRESOLVED:
- requires decision before implementation.

## Acceptance Criteria

R1A is accepted only when:

- economic provenance is traceable;
- equations have authoritative sources;
- variable meanings are frozen;
- unresolved ambiguities are explicitly listed.

## Terminal Classification

Use one:

- CH5_TWO_ASSET_HANK_R1A_COMPLETE_READY_FOR_R1_FREEZE
- CH5_TWO_ASSET_HANK_R1A_BLOCKED_MISSING_SOURCE
- CH5_TWO_ASSET_HANK_R1A_SCOPE_FAILURE
