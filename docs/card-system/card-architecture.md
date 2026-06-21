# Card Architecture

Version: 0.2 Provisional
Status: Active / Provisional
Scope: Tessera analog card architecture and future schema planning

---

## Overwrite Notice

This file replaces the earlier card-layer summary that used `Domain Cards -> Aspect Cards -> Facet Cards -> Expression Cards -> Reconciliation Cards` without the current candidate-facet, symbol, and Karma-boundary language.

Reason for replacement:

- the current hierarchy uses Domain Family, Aspect, Candidate Facet, Expression, and Reconciliation;
- symbols are now neutral non-scoring reference markers;
- Karma is separate from personality taxonomy and should not be encoded as an automatic score bridge;
- future digital infrastructure requires clearer card type boundaries.

---

## Personality Layer

```text
Domain-Family Reference Cards
Aspect Cards
Candidate Facet Cards
Expression Cards
Reconciliation Cards
```

### Domain-Family Reference Cards

Organizational anchors. They summarize related aspects but are not directly tested.

### Aspect Cards

Primary personality-testing cards. They use response patterns to estimate broad dispositional tendencies.

### Candidate Facet Cards

Interpretive cards that describe possible expression channels within an aspect. Candidate facets are not validated subscales unless later evidence supports that status.

### Expression Cards

Observer-readable behavioral evidence cards. They may support, challenge, or contextualize candidate facet interpretation.

### Reconciliation Cards

Cards that help explain mismatch, context sensitivity, inhibited expression, self-concept conflict, or difference between response pattern and observed behavior.

---

## Symbol Layer

Some cards may include neutral context symbols.

Symbols do not score personality, prove intent, or generate Karma outcomes. They provide reference points for later reconciliation or Karma review.

---

## Karma Layer

Karma cards and scenario references belong to a separate moral-context review system. Karma should evaluate ethical context under tradeoff, cost, harm, power, concealment, accountability, autonomy, or consequence.

Personality card results should not automatically convert into Karma results.

---

## Assessment Flow

```text
Aspect Card Sort
-> Response Pattern Review
-> Candidate Facet Routing
-> Expression Validation
-> Symbol Context Review
-> Reconciliation Review
-> Identity Map Update
```

Karma review may enter the process only when scenario content or expression context makes ethical review relevant.

---

## Purpose

Cards function as identity mapping tools rather than random gameplay mechanics.

The resulting structure creates a visual representation of personality architecture, behavioral expression, contextual variation, and possible reconciliation pathways.

---

## Digital Schema Note

Future digital systems should preserve the distinction between:

```text
card_type
source_construct
active_taxonomy_field
candidate_facet
expression_evidence
symbol_context
possible_karma_review_context
reconciliation_hypothesis
validation_status
```

No card field should be treated as validated assessment output unless appropriate validation has been completed.
