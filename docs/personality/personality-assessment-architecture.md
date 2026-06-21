# Personality Assessment Architecture

Version: 0.2 Provisional
Status: Active / Provisional
Scope: Tessera Identity System personality assessment architecture

---

## Overwrite Notice

This file replaces the prior architecture note that used the heading **Locked Principles** and stated that three-pass assessment was required.

Reason for replacement:

- the current governance model rejects locked or final language for active model structures;
- repeated assessment remains useful but should not be encoded as a universal requirement before the response-pattern model is further tested;
- future analog and digital implementations require provisional, reviewable architecture rather than hard-coded assumptions.

---

## Current Working Hierarchy

```text
Domain Family
-> Aspect
-> Candidate Facet
-> Expression
-> Reconciliation
```

### Domain Family

Organizational summary layer. Domain families are not directly tested unless later evidence supports that use.

### Aspect

Primary personality testing unit. Aspect cards measure broad dispositional tendencies through response patterns.

### Candidate Facet

Possible expression channel inside an aspect. Candidate facets help route interpretation and expression drafting, but should not be treated as validated subscales without evidence.

### Expression

Observable behavioral evidence that may support a candidate facet.

### Reconciliation

Interpretive process for apparent mismatch, contradiction, contextual variability, or difference between self-report, response pattern, observer evidence, and behavior.

---

## Current Architectural Principles

These principles are provisional design rules, not locked assumptions.

1. Domain families summarize aspect territory and support identity-map navigation.
2. Aspects are the current primary testing units.
3. Candidate facets explain how an aspect may manifest.
4. Expressions provide observable behavioral evidence.
5. Reconciliation explains mismatch without assuming error or moral failure.
6. Variance may be meaningful and should be reviewed rather than automatically discarded.
7. Symbols are non-scoring contextual markers.
8. Karma is a separate ethical-context model and should not be collapsed into personality scoring.
9. Empirically backed information should be preserved, cited, or routed rather than overwritten.
10. Tessera-specific speculative structures should remain labeled as provisional until validated.

---

## Assessment Flow

```text
Aspect Card Sort
-> Response Pattern Review
-> Aspect Strength Estimate
-> Consistency / Contextuality Review
-> Candidate Facet Routing
-> Expression Validation
-> Reconciliation Review
-> Identity Map Update
```

This flow is intended for analog play and future digital schema planning. It does not imply predictive certainty or validated measurement status without later testing.

---

## Marker Derivation

Behavioral consistency, directiveness, contextuality, or conflict markers should be derived from the final response pattern. Participants may provide reflection after the result is reviewed, but self-labeling should not replace pattern evidence.

Preferred interpretation language:

- the response pattern suggests;
- this appears consistent with;
- this may reflect;
- this should be reviewed alongside.

Avoid unsupported claims such as proves, confirms definitively, or guarantees.

---

## Digital Expansion Note

A future digital version may eventually use databases, automated routing, longitudinal records, or assisted interpretation. Until validation is available, digital implementations should preserve the difference between:

```text
empirical source construct
Tessera speculative construct
player-facing card mechanic
interpretive hypothesis
validated score
```

No digital schema should treat current speculative fields as validated assessment outputs merely because they are machine-readable.
