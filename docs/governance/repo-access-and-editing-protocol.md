# Repository Access and Editing Protocol

## Purpose

This document defines how repository governance should be handled when using an external assistant or connector to review, create, or modify Tessera Identity System files.

The goal is to preserve trust, prevent accidental overwrites, and avoid claiming repository-wide certainty when the available tool access cannot verify the full repository state.

## Access Boundary

Repository governance through a connector depends on two separate conditions:

1. **Permission access**: whether the connector is authorized to read and write repository contents.
2. **Enumeration access**: whether the connector can reliably list or search the full repository file tree.

A connector may have permission to fetch, create, and update known files while still lacking reliable full-tree enumeration. These are different capabilities and should not be treated as equivalent.

## Required Scope Language

When full-tree enumeration has not been verified, repository changes should be described as known-file updates, not full-repository audits.

Recommended wording:

> This change has been checked against the files fetched directly by path and against the current governance manifest. It has not been verified against every file in the repository unless the full repo tree, manifest, or reliable repository search has been reviewed.

## Editing Protocol

Before modifying an existing file, the assistant or contributor should:

1. Identify the target file path.
2. Fetch the current file contents.
3. Identify the specific section likely to change.
4. State whether the change may overwrite, replace, reinterpret, or supersede an existing format.
5. Request explicit confirmation when the change may structurally overwrite prior model content.
6. Apply the update only after confirmation.
7. Report the changed file path and resulting commit SHA.

## New File Protocol

New files may be created when they do not overwrite existing files and their purpose is clear. If a new file changes governance, taxonomy, Karma interpretation, scoring, symbols, reconciliation, or manual procedure, it should still be reported as a structural addition.

## Repo-Wide Governance Requirement

Repo-wide governance claims require at least one of the following:

1. A reliable recursive repository tree listing.
2. A maintained `docs/governance/repo-tree.md` file generated from the repository.
3. A maintained `docs/governance/model-file-manifest.md` identifying all active model-relevant files.
4. A reliable search index confirmed to return repository-wide results.

If none of these is available, governance statements must be limited to known files.

## Overwrite Notice Requirement

Any change that may supersede or reinterpret existing structure should include an overwrite notice before modification.

Recommended format:

```text
Overwrite Notice:
This change may replace or reinterpret [existing structure/file/section].

Affected areas:
- [area]
- [area]

Reason:
[why the change improves construct clarity, reduces redundancy, improves analog usability, or corrects an empirical/structural issue]

Confirmation required before update: Yes.
```

## Current Working Standard

The preferred governance process is:

```text
Fetch repo-tree.md
Fetch model-file-manifest.md
Fetch relevant target files
Identify potential overwrite/conflict
Request confirmation if structural
Apply change
Report commit SHA
Update manifest if a model-relevant file was added or retired
```

## Non-Absolute Interpretation Standard

No repository governance file should imply that conceptual structures are permanently fixed. Current structures may be described as provisional, review-ready, active, superseded, archival, or deprecated, but not locked against amendment.
