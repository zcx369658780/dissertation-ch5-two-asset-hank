# Project Rule Index Current

## Purpose

Entry point for Chapter 5 Two-Asset HANK Reconstruction governance.

## Rule Reading Order

1. Read project governance index.
2. Read repository task file before execution.
3. Treat GitHub task files as execution authority.
4. Keep scientific scope, implementation scope and evidence scope separated.
5. Read capability routing rules before denying available GitHub operations.

## Core Rules

- `PROJECT_RULE_GITHUB_CAPABILITY_AND_AUTHORITY_ROUTING_CURRENT.md`
  - GitHub capability detection;
  - authority routing;
  - mutation verification boundary.

## Default Boundaries

Unless explicitly authorized by a GitHub task:

- do not implement model code;
- do not run MATLAB or Python models;
- do not modify solver logic;
- do not generate Results claims;
- do not modify protected scientific sources.

## Workflow

GPT reviewer/route authority:

- defines next gate;
- creates task authority;
- reviews evidence;
- may perform authorized GitHub governance operations when repository access exists.

Builder:

- executes only GitHub-authorized tasks;
- reports evidence, files, checks and blockers.

## Acceptance

A task is executable only when:

- the task file exists on live GitHub main;
- required rule files exist;
- authority boundaries are satisfied.

A GitHub operation is considered completed only after repository evidence verifies the mutation.
