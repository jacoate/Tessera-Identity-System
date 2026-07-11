# Model File Manifest

Version: 0.5 Provisional  
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
- **Partially Superseded**: contains useful historical or handoff material, but some structural claims have been replaced by newer files.
- **Superseded**: retained as historical reference but no longer governing.
- **Archival**: source/reference material not currently governing the active model.
- **Automation**: workflow or procedural file that supports repository governance.

---

## Current Active / Governance / Expansion / Source Files

| Path | Status | Function |
|---|---|---|
| `README.md` | Active / Provisional | Project overview, current working architecture, TNOA introduction, and empirical/speculative boundary |
| `.github/workflows/update-repo-tree.yml` | Automation / Governance | Regenerates `docs/governance/repo-tree.md` after updates reach main |
| `.github/workflows/build-and-validate-specifications.yml` | Automation / Governance | Builds the deterministic TNOA PDF, validates Markdown/PDF pairing, and checks governance references |
| `scripts/build_tnoa_pdf.py` | Automation / Documentation | Deterministic ReportLab renderer for the TNOA Markdown specification |
| `docs/governance/revision-and-overwrite-policy.md` | Governance | Revision policy, overwrite confirmation rules, empirical preservation rule |
| `docs/governance/repo-access-and-editing-protocol.md` | Governance | Connector access boundary and edit procedure |
| `docs/governance/repo-tree.md` | Governance | Repository tree index and enumeration boundary record |
| `docs/governance/model-file-manifest.md` | Governance | Manifest of known model-relevant files |
| `docs/specifications/tnoa-development-and-measurement-specification-v0.1.md` | Active / Provisional / Expansion Scaffold | Editable source specification for Normative Orientation Architecture development, measurement, ontology, and validation |
| `docs/specifications/tnoa-development-and-measurement-specification-v0.1.pdf` | Active / Provisional / Review Artifact | Fixed-layout review edition generated from the TNOA Markdown specification |
| `docs/project-context/current-development-context.md` | Source Reference / Partially Superseded | Historical card-system handoff containing earlier taxonomy and scope statements; consult newer README, manifest, and specifications for current architecture |
| `docs/chat-context/2026-06-21-taxonomy-decisions.md` | Superseded / Source Reference | Historical eight-aspect taxonomy decision archive; not active schema |
| `docs/taxonomy/provisional-primary-aspect-set.md` | Active / Provisional | Current review-ready 10-aspect taxonomy |
| `docs/taxonomy/june-21-integration-map.md` | Active / Provisional / Source Reference | Maps June 21 source clusters into the current ten-aspect model |
| `docs/assessment/aspect-questioning-model.md` | Active / Provisional | Aspect card questioning and response-pattern interpretation model |
| `docs/assessment/three-pass-methodology.md` | Active / Provisional | Reframed repeated-review methodology, not a fixed three-pass requirement |
| `docs/symbols/context-symbol-layer.md` | Active / Provisional | Neutral non-scoring symbol layer for reconciliation and cross-reference |
| `docs/karma/taxonomy-karma-boundary.md` | Active / Provisional | Boundary between personality taxonomy and Karma interpretation; TNOA specification supplies the broader descriptive normative layer |
| `docs/card-system/aspect-facet-taxonomy.md` | Active / Provisional | Candidate facet scaffold aligned with the ten-aspect model |
| `docs/card-system/card-architecture.md` | Active / Provisional | Card architecture aligned with hierarchy, symbols, and Karma boundary |
| `docs/card-system/domain-cards.md` | Active / Provisional | Five-domain-family reference model |
| `docs/card-system/karma-system-model.md` | Active / Provisional | Ethical-review overlay retained separately from personality and the descriptive TNOA architecture |
| `docs/card-system/rough-expression-library-model.md` | Active / Provisional | Expression schema aligned with symbols, Karma review, and ten-aspect taxonomy |
| `docs/personality/personality-assessment-architecture.md` | Active / Provisional | Architecture without locked language or required three-pass assumption |
| `docs/personality/facet-framework.md` | Active / Provisional | Candidate-facet framework and digital schema boundary |
| `docs/personality/reconciliation-framework.md` | Active / Provisional | Reconciliation framework aligned with symbols and Karma review context |
| `docs/personality/expression-validation-model.md` | Active / Provisional | Expression validation boundaries and schema distinction |
| `docs/ecology/distal-influences.md` | Expansion Scaffold / Source-Review Needed | Future ecological/developmental integration context |
| `docs/ecology/proximal-influences.md` | Expansion Scaffold / Source-Review Needed | Future ecological/relational integration context |
| `docs/identity/identity-development.md` | Expansion Scaffold / Source-Review Needed | Future identity-development integration context |
| `docs/identity/master-identity-tree.md` | Expansion Scaffold / Source-Review Needed | Future holistic identity tree scaffold |
| `docs/archive/unimplemented-ideas-and-future-work.md` | Archival / Source Reference | Candidate ideas not implemented in active architecture |

---

## Normative Orientation Architecture Status

The Tessera Normative Orientation Architecture (TNOA) is an active provisional expansion scaffold.

Its current role is to describe how values, principles, norms, ideology, morality, ethics, factual premises, motives, intentions, context, behavior, and developmental updating are separately analyzed and then integrated.

TNOA does not currently authorize:

- a global morality score;
- diagnosis of moral character;
- proof of hidden intention;
- automatic conversion from personality to ethical judgment;
- presentation of an integrated Tessera profile as validated.

The Karma model remains a separate ethical-review overlay. Future integration should preserve the distinction between descriptive normative representation and explicitly benchmarked ethical evaluation.

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

Honesty-Humility is not currently treated as an active personality taxonomy branch. Its moral content may be represented through Karma review and TNOA descriptive variables, while non-moral behavioral material may be used as source material for card wording, neutral symbol tags, reconciliation context, source-lineage documentation, or manual commentary.

---

## June 21 Archive Status

The June 21 taxonomy archive is a source-reference document, not active schema.

Its eight historical clusters are mapped into the current model through:

```text
docs/taxonomy/june-21-integration-map.md
```

Future digital implementations should not ingest the June 21 eight-aspect list as active `personality.aspect` data.

---

## Empirical / Integrative / Speculative Boundary

Empirically supported information should be preserved, cited, routed, or archived rather than overwritten.

Integrative Tessera structures should be labeled as provisional frameworks when the underlying constructs are supported but the combined architecture has not been validated.

Speculative Tessera-specific model content should remain explicitly labeled as provisional, candidate, hypothesis, design extrapolation, entertainment-only, or requiring validation when appropriate.

---

## Maintenance Rule

Before repo-wide governance claims are made, review this manifest and `docs/governance/repo-tree.md`.

If the repository tree has not been fully generated or verified, claims should be limited to known files listed in this manifest.

When a newly discovered file contains conflicting structure, update this manifest after the conflict is resolved, superseded, or classified for review.
