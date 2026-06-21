# Model File Manifest

## Purpose

This manifest identifies files currently known to contain active or governance-relevant Tessera Identity System model content.

The manifest is a working index, not a claim that no other model-relevant files exist. It should be updated whenever a model-relevant file is created, retired, superseded, renamed, or discovered.

## Status Labels

- **Active**: currently used in the working model.
- **Governance**: defines editing, revision, overwrite, or access rules.
- **Provisional**: active but open to review and amendment.
- **Superseded**: retained as historical reference but no longer governing.
- **Archival**: source/reference material not currently governing the active model.
- **Automation**: workflow or procedural file that supports repository governance.

## Known Active / Governance Files

| Path | Status | Function |
|---|---|---|
| `README.md` | Active / Provisional | Project overview and current working architecture summary |
| `.github/workflows/update-repo-tree.yml` | Automation / Governance | Regenerates `docs/governance/repo-tree.md` from the Git repository tree |
| `docs/governance/revision-and-overwrite-policy.md` | Governance | Revision policy and overwrite confirmation rules |
| `docs/governance/repo-access-and-editing-protocol.md` | Governance | Connector access boundary and edit procedure |
| `docs/governance/repo-tree.md` | Governance | Repository tree index and enumeration boundary record |
| `docs/governance/model-file-manifest.md` | Governance | Manifest of known model-relevant files |
| `docs/taxonomy/provisional-primary-aspect-set.md` | Active / Provisional | Current review-ready 10-aspect taxonomy |
| `docs/assessment/aspect-questioning-model.md` | Active / Provisional | Aspect card questioning and response-pattern interpretation model |
| `docs/symbols/context-symbol-layer.md` | Active / Provisional | Neutral non-scoring symbol layer for reconciliation and cross-reference |
| `docs/karma/taxonomy-karma-boundary.md` | Active / Provisional | Boundary between personality taxonomy and Karma interpretation |

## Known Current Aspect Set

```text
Extraversion
- Assertiveness
- Enthusiasm

Agreeableness
- Compassion
- Politeness

Conscientiousness
- Industriousness
- Orderliness

Negative Emotionality / Neuroticism
- Withdrawal
- Volatility

Openness / Intellect
- Openness
- Intellect
```

## Honesty-Humility Status

Honesty-Humility is not currently treated as an active personality taxonomy branch. Its moral content is represented in the Karma model, while any non-moral behavioral material may be used only as source material for card wording, neutral symbol tags, reconciliation context, or manual commentary.

## Maintenance Rule

Before repo-wide governance claims are made, review this manifest and `docs/governance/repo-tree.md`.

If the repository tree has not been fully generated or verified, claims should be limited to known files listed in this manifest.
