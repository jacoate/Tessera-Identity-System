# Rough Expression Library Model

Version: 0.2 Provisional
Status: Active / Provisional
Scope: Tessera Identity System expression drafting

---

## Overwrite Notice

This file replaces the prior draft expression model that used an active `Aspect: Honesty` example and described inverse expressions as subtracting from expression integrity while flagging Karma review.

Reason for replacement:

- Honesty / Honesty-Humility is no longer an active personality taxonomy branch;
- Karma linkage should be contextual and review-oriented rather than automatic moral scoring;
- expression records should be compatible with the current ten-aspect taxonomy and neutral symbol layer;
- future digital schemas need clear separation between personality activation, expression evidence, symbol context, and Karma review.

---

## Purpose

The expression library translates candidate facets into observer-readable behavioral evidence.

Expression records may support:

- self-mapping;
- facilitator-guided interpretation;
- observer comparison;
- expression validation;
- reconciliation review;
- future digital schema development.

Expressions are not traits. They are observable, repeatable behaviors that provide possible evidence for a candidate facet.

---

## Expression Wording Standard

Expression items should use observer-readable phrasing when possible.

Avoid first-person-only wording:

```text
I speak up when my position is challenged.
```

Prefer observer-readable wording:

```text
Speaks up when their position is challenged.
```

This allows the same expression card to be interpreted by the individual, a facilitator, a researcher, or a third-party observer without rewriting the card.

---

## Expression Categories

The current rough expression library uses six drafting categories:

| Category | Function |
|---|---|
| Behavioral | Observable action or conduct. |
| Communication | Spoken, written, or expressive behavior. |
| Decision-Making | Choice pattern or priority selection. |
| Relational | Interpersonal behavior or social positioning. |
| Problem-Solving | Response to obstacle, conflict, uncertainty, or complexity. |
| Self-Management | Regulation, recovery, inhibition, or sustained control. |

Not every final facet requires every category. The categories are drafting lenses, not required subscales.

---

## Positive, Low, and Distorted Expression

Expression drafting should preserve three distinctions:

```text
Positive / coherent expression
Low or absent expression
Distorted / aversive expression
```

Low expression is not the same as negative expression.

Example:

```text
Does not speak up.
```

This may suggest low assertiveness, social inhibition, uncertainty, role suppression, or context restriction. It should not automatically be interpreted as distorted expression.

A distorted expression would involve an active counter-pattern:

```text
Uses pressure to force agreement instead of communicating a position clearly.
```

Distorted expression may route to reconciliation or Karma review, but should not be treated as proof of intent or moral character.

---

## Relationship to Symbols

Expression records may include neutral context symbols.

Symbols do not score the expression. They indicate themes that may become relevant during reconciliation or Karma scenario review.

Example symbols:

- Agency
- Status
- Cost
- Care
- Disclosure
- Equity
- Resource
- Accountability

Repeated symbols may identify a recurring context theme, but they should not accumulate into hidden trait scores.

---

## Relationship to Karma

Karma can inform the design of distorted or ethically loaded expression options, but Karma does not replace personality scoring and does not automatically convert expression choices into moral conclusions.

Use language such as:

```text
Possible Karma review context
```

Avoid language such as:

```text
Confirmed Karma shadow
Definitive moral flag
Proof of deception
```

Karma review becomes relevant when an expression intersects with tradeoff, cost, power, concealment, harm, accountability, exploitation, or consequence.

---

## Provisional Expression Item Schema

Each draft expression item should eventually be stored with fields such as:

| Field | Purpose |
|---|---|
| Expression ID | Stable identifier for future card or database use. |
| Domain Family | Organizational anchor, if needed. |
| Aspect | Parent aspect from the current ten-aspect model. |
| Candidate Facet | Parent candidate facet. |
| Expression Category | Behavioral, Communication, Decision-Making, Relational, Problem-Solving, or Self-Management. |
| Positive Expression | Observer-readable coherent expression. |
| Low / Inhibited Expression | Possible low-expression or suppressed-expression wording. |
| Distorted Expression A | Active counter-pattern or aversive implementation. |
| Distorted Expression B | Optional second distorted pattern. |
| Symbol Tags | Neutral context markers. |
| Possible Karma Review Context | Karma dimensions that may become relevant if scenario context supports review. |
| Reconciliation Cues | Possible routes such as role suppression, social inhibition, cost sensitivity, or self-concept mismatch. |
| Scoring Notes | Draft notes for analog or digital scoring, marked provisional. |
| Empirical / Speculative Status | Whether the item is sourced from empirical construct logic, Tessera design extrapolation, or entertainment-only mechanics. |

---

## Example Draft Expression Record

```text
Expression ID: ASSERT-INFL-COMM-001
Domain Family: Extraversion
Aspect: Assertiveness
Candidate Facet: Influence
Expression Category: Communication

Positive Expression:
Explains an idea in a way that helps others understand the choice.

Low / Inhibited Expression:
Avoids explaining their position when others may disagree.

Distorted Expression A:
Frames information selectively so others move toward the preferred choice without seeing relevant tradeoffs.

Distorted Expression B:
Uses confidence or urgency to push agreement before others can evaluate alternatives.

Symbol Tags:
Agency / Disclosure / Status / Cost

Possible Karma Review Context:
Authentic Presentation, Relational Equity, Moral Sensitivity, Accountability Orientation.

Reconciliation Cues:
Influence may be present, but expression integrity should be reviewed if persuasion relies on omission, pressure, or reduced autonomy.

Scoring Notes:
Positive expression may support Influence. Low expression may indicate inhibition or context restriction. Distorted expression may trigger review but should not automatically produce a moral conclusion without scenario context.

Empirical / Speculative Status:
Facet/expression logic is provisional Tessera modeling informed by personality-expression concepts. It is not validated as a scale item until tested.
```

---

## Token Economy Dependency

The expression library cannot be finalized until the token economy model is defined.

The token economy model should determine:

- total tokens per scenario;
- maximum tokens per option;
- whether all tokens must be allocated;
- whether unused tokens have meaning;
- number of response options per card;
- whether distorted options affect expression integrity, trigger review, or both;
- whether categories are scored separately or collapsed into facet estimates;
- how review flags are described without implying certainty.

---

## Current Rough Scoring Assumption

Current provisional assumption:

```text
Positive expression options
-> may support candidate facet evidence

Low / inhibited expression options
-> may support contextuality or reconciliation review

Distorted expression options
-> may reduce expression integrity or route to Karma review when scenario context supports it
```

This preserves the distinction between:

```text
personality tendency
observable expression
contextual inhibition
ethical implementation
```

---

## Digital Schema Warning

Future databases should not treat `Possible Karma Review Context` as a confirmed Karma outcome. It is a routing hint for interpretation, scenario comparison, or later validation.

Recommended separation:

```text
trait_activation_evidence
expression_integrity_review
context_symbol_tags
possible_karma_review_context
final_interpretation_note
validation_status
```

---

## Next Step

Create or revise the Token Economy Model only after the current taxonomy, symbol, Karma-boundary, and reconciliation rules have been reviewed together.
