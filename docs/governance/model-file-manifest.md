# Model File Manifest

Version: 0.4 Provisional
Status: Governance
Scope: active, governance-relevant, expansion-scaffold, source-archive, and review-relevant Tessera model files

---

## Purpose

This manifest identifies files currently known to contain active, governance-relevant, expansion-scaffold, source-archive, or review-relevant Tessera Identity System model content.

The manifest is a working index. It should be updated whenever a model-relevant file is created, retired, superseded, renamed, discovered, or structurally overwritten.

---

## Status Labels

- **Active**: currently used in the working model.
- **Governance**: defines editing, revision, overwrite, access, source-protection, or enumeration rules.
- **Provisional**: active but open to review and amendment.
- **Expansion Scaffold**: future-facing model structure that is not yet an operationalized assessment system.
- **Source-Review Needed**: requires empirical source review before being treated as official model structure.
- **Source Reference**: retained for candidate material, design lineage, or comparison, but not governing active schema.
- **Superseded**: retained as historical reference but no longer governing.
- **Archival**: source/reference material not currently governing the active model.
- **Automation**: workflow or procedural file that supports repository governance.

---

## Current Active / Governance / Expansion / Source Files

| Path | Status | Function |
|---|---|---|
| `README.md` | Active / Provisional | Project overview, current working architecture summary, empirical/speculative boundary |
| `.github/workflows/update-repo-tree.yml` | Automation / Governance | Regenerates `docs/governance/repo-tree.md` from the Git repository tree |
| `docs/governance/revision-and-overwrite-policy.md` | Governance | Revision policy, overwrite confirmation rules, empirical preservation rule |
| `docs/governance/repo-access-and-editing-protocol.md` | Governance | Connector access boundary and edit procedure |
| `docs/governance/repo-tree.md` | Governance | Repository tree index and enumeration boundary record |
| `docs/governance/model-file-manifest.md` | Governance | Manifest of known model-relevant files |
| `docs/chat-context/2026-06-21-taxonomy-decisions.md` | Superseded / Source Reference | Historical eight-aspect taxonomy decision archive; not active schema |
| `docs/taxonomy/provisional-primary-aspect-set.md` | Active / Provisional | Current review-ready 10-aspect taxonomy |
| `docs/taxonomy/june-21-integration-map.md` | Active / Provisional / Source Reference | Maps June 21 source clusters into the current ten-aspect model |
| `docs/assessment/aspect-questioning-model.md` | Active / Provisional | Aspect card questioning and response-pattern interpretation model |
| `docs/assessment/three-pass-methodology.md` | Active / Provisional | Reframed repeated-review methodology, not a fixed three-pass requirement |
| `docs/symbols/context-symbol-layer.md` | Active / Provisional | Neutral non-scoring symbol layer for reconciliation and cross-reference |
| `docs/karma/taxonomy-karma-boundary.md` | Active / Provisional | Boundary between personality taxonomy and Karma interpretation |
| `docs/card-system/aspect-facet-taxonomy.md` | Active / Provisional | Candidate facet scaffold aligned with the ten-aspect model |
| `docs/card-system/card-architecture.md` | Active / Provisional | Card architecture aligned with hierarchy, symbols, and Karma boundary |
| `docs/card-system/domain-cards.md` | Active / Provisional | Five-domain-family reference model |
| `docs/card-system/karma-system-model.md` | Active / Provisional | Karma model with non-scoring review boundary |
| `docs/card-system/rough-expression-library-model.md` | Active / Provisional | Expression schema aligned with symbols, Karma review, and ten-aspect taxonomy |
| `docs/personality/personality-assessment-architecture.md` | Active / Provisional | Architecture without locked language or required three-pass assumption |
| `docs/personality/facet-framework.md` | Active / Provisional | Candidate-facet framework and digital schema boundary |
| `docs/personality/reconciliation-framework.md` | Active / Provisional | Reconciliation framework aligned with symbols and Karma review context |
| `docs/personality/expression-validation-model.md` | Active / Provisional | Expression validation boundaries and schema distinction |
| `docs/ecology/distal-influences.md` | Expansion Scaffold / Source-Review Needed | Future ecological/developmental integration context |
| `docs/ecology/proximal-influences.md` | Expansion Scaffold / Source-Review Needed | Future ecological/relational integration context |
| `docs/identity/identity-development.md` | Expansion Scaffold / Source-Review Needed | Future identity-development integration context |
| `docs/identity/master-identity-tree.md` | Expansion Scaffold / Source-Review Needed | Future holistic identity tree scaffold |

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

## June 21 Archive Status

The June 21 taxonomy archive is a source-reference document, not active schema.

Its eight historical clusters are mapped into the current model through:

```text
docs/taxonomy/june-21-integration-map.md
```

Future digital implementations should not ingest the June 21 eight-aspect list as active `personality.aspect` data.

---

## Empirical / Speculative Boundary

Empirically supported information should be preserved, cited, routed, or archived rather than overwritten.

Speculative Tessera-specific model content should remain explicitly labeled as provisional, candidate, hypothesis, design extrapolation, entertainment-only, or requiring validation when appropriate.

---

## Maintenance Rule

Before repo-wide governance claims are made, review this manifest and `docs/governance/repo-tree.md`.

If the repository tree has not been fully generated or verified, claims should be limited to known files listed in this manifest.

When a newly discovered file contains conflicting structure, update this manifest after the conflict is resolved, superseded, or classified for review.
