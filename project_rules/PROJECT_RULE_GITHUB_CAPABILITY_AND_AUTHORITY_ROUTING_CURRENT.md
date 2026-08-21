# GitHub Capability and Authority Routing Current

## Purpose

Prevent workflow capability misclassification in GitHub-governed projects.

This rule applies when GPT reviewer/route authority has access to GitHub repository operations.

## Core Principle

Do not confuse:

- prohibition against fabricating GitHub actions;
- absence of GitHub write capability;
- actual availability of GitHub repository tools.

These are different states.

## Capability Check Order

Before stating that a GitHub publication cannot be performed:

1. Check whether the current environment provides GitHub repository operations.
2. Check whether the target repository is accessible.
3. Check whether the requested operation is within the role authority.
4. Execute only the authorized operation.
5. Verify the resulting GitHub state after mutation.

## Forbidden Reasoning Pattern

Do NOT infer:

"Cannot claim an unverified commit" -> "Cannot create a commit."

Correct interpretation:

"Cannot claim an unverified commit" -> "Must perform the operation first, then verify evidence."

## GitHub Authority Workflow

For repositories using GitHub-governed workflow:

GPT reviewer/route authority may:

- create authorized task files;
- create governance documents;
- update repository rule files when explicitly required;
- verify live repository state.

GPT MUST NOT:

- claim a mutation before execution;
- claim a commit hash without GitHub evidence;
- bypass task authority.

## Acceptance Boundary

A GitHub mutation is accepted only after:

- repository response confirms mutation;
- resulting file state is fetched or otherwise verified;
- live authority is distinguished from draft content.

## Non-Declaration

This rule does not authorize scientific implementation, model execution, calibration, or Results generation. Scientific operations still require their own task authority.
