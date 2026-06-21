# Candidate Facet Framework

Version: 0.2 Provisional
Status: Active / Provisional
Scope: Tessera personality taxonomy and expression routing

---

## Overwrite Notice

This file updates the earlier facet framework to align with the current candidate-facet terminology.

Reason for replacement:

- current taxonomy uses candidate facets rather than treating every facet as a fixed subscale;
- candidate facets should support interpretation and expression drafting without claiming validation;
- future digital infrastructure should not hard-code provisional facets as final psychometric factors.

---

## Definition

A candidate facet is a possible structural expression channel through which an aspect may manifest behaviorally.

Candidate facets answer:

```text
What kind of this aspect appears to be expressed?
```

They do not answer:

```text
How much moral integrity does this person have?
```

Moral-context review belongs to Karma when ethically relevant scenario conditions are present.

---

## Purpose

Candidate facets support:

- explanation of aspect patterns;
- differentiation between people with similar aspect strength;
- routing to relevant expression cards;
- reconciliation when response patterns and behavior diverge;
- future digital schema planning.

---

## Example

Aspect: Assertiveness

Candidate facets:

- Direction-Setting
- Initiative
- Verbal Confidence
- Leadership
- Influence
- Boundary Assertion

These are provisional expression channels. They should be refined through item development, card testing, expert review, and later empirical validation.

---

## Design Boundary

Candidate facets are interpretation instruments rather than full psychometric inventories.

They should not be described as validated subscales unless evidence supports that claim.

They should not duplicate Karma dimensions, neutral symbols, or reconciliation categories.

---

## Digital Schema Note

Future databases should store a candidate facet's validation status separately from its use in card routing.

Suggested fields:

```text
candidate_facet_id
parent_aspect
working_definition
source_status
validation_status
expression_routes
symbol_contexts
revision_notes
```
