# Model File Manifest

Version: 0.2 Provisional
Status: Governance
Scope: active, governance-relevant, and review-pending Tessera model files

---

## Purpose

This manifest identifies files currently known to contain active, governance-relevant, superseded, or review-pending Tessera Identity System model content.

The manifest is a working index. It should be updated whenever a model-relevant file is created, retired, superseded, renamed, discovered, or structurally overwritten.

---

## Status Labels

- **Active**: currently used in the working model.
- **Governance**: defines editing, revision, overwrite, access, or source-protection rules.
- **Provisional**: active but open to review and amendment.
- **Superseded**: retained as historical reference but no longer governing.
- **Review Pending**: known model-relevant file requiring review against current architecture.
- **Archival**: source/reference material not currently governing the active model.
- **Automation**: workflow or procedural file that supports repository governance.

---

## Current Active / Governance Files

| Path | Status | Function |
|---|---|---|
| `README.md` | Active / Provisional | Project overview, current working architecture summary, empirical/speculative boundary |
| `.github/workflows/update-repo-tree.yml` | Automation / Governance | Regenerates `docs/governance/repo-tree.md` from the Git repository tree |
| `docs/governance/revision-and-overwrite-policy.md` | Governance | Revision policy, overwrite confirmation rules, empirical preservation rule |
| `docs/governance/repo-access-and-editing-protocol.md` | Governance | Connector access boundary and edit procedure |
| `docs/governance/repo-tree.md` | Governance | Repository tree index and enumeration boundary record |
| `docs/governance/model-file-manifest.md` | Governance | Manifest of known model-relevant files |
| `docs/taxonomy/provisional-primary-aspect-set.md` | Active / Provisional | Current review-ready 10-aspect taxonomy |
| `docs/assessment/aspect-questioning-model.md` | Active / Provisional | Aspect card questioning and response-pattern interpretation model |
| `docs/assessment/three-pass-methodology.md` | Active / Provisional | Reframed repeated-review methodology, not a fixed three-pass requirement |
| `docs/symbols/context-symbol-layer.md` | Active / Provisional | Neutral non-scoring symbol layer for reconciliation and cross-reference |
| `docs/karma/taxonomy-karma-boundary.md` | Active / Provisional | Boundary between personality taxonomy and Karma interpretation |
| `docs/card-system/aspect-facet-taxonomy.md` | Active / Provisional | Updated candidate facet scaffold aligned with the ten-aspect model |
| `docs/card-system/domain-cards.md` | Active / Provisional | Updated five-domain-family reference model |
| `docs/card-system/karma-system-model.md` | Active / Provisional | Updated Karma model with non-scoring review boundary |
| `docs/card-system/rough-expression-library-model.md` | Active / Provisional | Updated expression schema aligned with symbols, Karma review, and ten-aspect taxonomy |
| `docs/personality/personality-assessment-architecture.md` | Active / Provisional | Updated architecture without locked language or required three-pass assumption |

---

## Known Review-Pending Files

These files were visible in the repository tree and may contain useful material, older assumptions, or partially compatible structures. They should be reviewed before future digital infrastructure treats them as active schema.

| Path | Status | Review Reason |
|---|---|---|
| `docs/personality/facet-framework.md` | Review Pending | Likely compatible but should be aligned with candidate-facet language |
| `docs/personality/reconciliation-framework.md` | Review Pending | Likely compatible but should be aligned with symbol-derived and Karma-derived reconciliation context |
| `docs/personality/expression-validation-model.md` | Review Pending | May need scale/schema distinction from aspect card response sorting |
| `docs/card-system/card-architecture.md` | Review Pending | Should be reviewed for older layer naming or fixed procedure language |
| `docs/card-system/facet-card-model.md` | Review Pending | Should be aligned with candidate facet status and current schema language |
| `docs/card-system/identity-map-layout.md` | Review Pending | Should be reviewed for consistency with current hierarchy and future digital planning |
| `docs/card-system/reconciliation-cards.md` | Review Pending | Should be aligned with updated reconciliation and symbol procedures |
| `docs/card-system/symbol-system.md` | Review Pending | Should be compared against current non-scoring symbol layer |

---

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

---

## Honesty-Humility Status

Honesty-Humility is not currently treated as an active personality taxonomy branch. Its moral content is represented in the Karma model, while any non-moral behavioral material may be used only as source material for card wording, neutral symbol tags, reconciliation context, source-lineage documentation, or manual commentary.

---

## Empirical / Speculative Boundary

Empirically supported information should be preserved, cited, routed, or archived rather than overwritten.

Speculative Tessera-specific model content should remain explicitly labeled as provisional, candidate, hypothesis, design extrapolation, entertainment-only, or requiring validation when appropriate.

---

## Maintenance Rule

Before repo-wide governance claims are made, review this manifest and `docs/governance/repo-tree.md`.

If the repository tree has not been fully generated or verified, claims should be limited to known files listed in this manifest.

When a newly discovered file contains conflicting structure, update this manifest after the conflict is resolved, superseded, or classified for review.
