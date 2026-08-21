# Chapter 5 Two-Asset HANK Model Constitution R0

Status: SCIENTIFIC_SPECIFICATION_DRAFT

Purpose:

Define the economic identity of the new Chapter 5 two-asset HANK reconstruction before implementation.

## Model identity

This repository reconstructs an auditable two-asset heterogeneous-agent household core. It is not a direct line-by-line MATLAB translation and it is not a continuation of the previous one-asset prototype.

## Core state space

The baseline household state is:

(a,b,z)

where:

- a: illiquid asset;
- b: liquid asset;
- z: productivity/income state.

## Controls

Required household controls:

- consumption c;
- labor l;
- illiquid asset adjustment/transfer d.

## Required mechanisms

The first version must preserve:

- two-asset accounting;
- adjustment cost mechanism;
- separate liquid and illiquid assets;
- household distribution.

## HJB requirements

The solver must explicitly define:

- asset drifts;
- forward/backward derivatives;
- policy construction;
- boundary conditions.

The same economic object must support later KFE construction.

## Generator

The intended decomposition is:

G = G_a + G_b + G_z

The generator used for HJB and KFE must be consistent.

## KFE

Required diagnostics:

- G^T g = 0;
- mass conservation;
- non-negativity;
- uniqueness assessment.

## Asset accounting

Must report separately:

A_hh = integral(a*g)

B_hh = integral(b*g)

A one-asset aggregation is not acceptable as the baseline model.

## Current exclusions

The first implementation stage does not include:

- NK block;
- spatial extension;
- regional aggregation;
- transition dynamics;
- deep learning acceleration.

## Reconstruction principles

All future implementation must distinguish:

1. structural parity;
2. algorithmic parity;
3. numerical parity.

MATLAB materials are economic provenance sources, not automatic numerical oracles.
