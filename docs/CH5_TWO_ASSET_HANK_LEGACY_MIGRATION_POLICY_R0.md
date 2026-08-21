# Chapter 5 Two-Asset HANK Legacy Migration Policy R0

Status: SCIENTIFIC_SPECIFICATION_DRAFT

Purpose:

Define how legacy MATLAB materials should be evaluated before entering the new reconstruction.

## Principles

MATLAB code is treated as economic provenance, not as an unquestioned implementation oracle.

Every legacy mechanism must be classified:

- RETAIN;
- REDESIGN;
- DROP;
- UNRESOLVED.

## Initial classification

Likely RETAIN:

- two-asset household concept;
- household heterogeneity;
- HJB/KFE economic structure;
- asset accounting distinction.

Likely REDESIGN:

- numerical solver implementation;
- discretization choices;
- diagnostics framework;
- software architecture.

Likely DROP or DEFER:

- legacy output scripts;
- undocumented helpers;
- unverified compatibility branches.

## Parity requirements

Future migration must separately evaluate:

- structural parity;
- algorithmic parity;
- numerical parity.

Similar filenames or functions do not establish equivalence.

## Decision gate

No production implementation starts until migration decisions are reviewed.
