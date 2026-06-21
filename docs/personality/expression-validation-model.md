# Expression Validation Model

Version: 0.2 Provisional
Status: Active / Provisional
Scope: Tessera expression evidence and validation procedures

---

## Overwrite Notice

This file updates the earlier expression validation note to distinguish expression validation scales from aspect card response scales and to align with the candidate-facet model.

Reason for replacement:

- expression validation is not the same procedure as aspect assessment;
- expressions provide evidence for candidate facets, not direct trait proof;
- future digital infrastructure should preserve the difference between aspect responses, expression evidence, symbols, and Karma review.

---

## Definition

Expressions are observable behavioral evidence.

An expression is a specific behavior that may provide evidence for a candidate facet.

Expressions are not traits, diagnoses, moral conclusions, or final scores.

---

## Function

Expressions may:

- support a candidate facet interpretation;
- challenge a candidate facet interpretation;
- reveal context-dependent expression;
- identify possible suppression or inhibition;
- route reconciliation review;
- provide observer-readable evidence for identity mapping.

---

## Example

Candidate Facet: Leadership

Possible expressions:

- Organizes groups.
- Delegates tasks.
- Coordinates efforts.
- Resolves indecision.

These expressions may support Leadership as an expression channel of Assertiveness, but should be reviewed alongside aspect response patterns and context.

---

## Validation Scales

Expression cards may use scales such as:

### Frequency

- Never
- Rarely
- Sometimes
- Often
- Consistently

### Identification

- Not Me
- Somewhat Me
- Mostly Me
- Definitely Me

These scales are for expression validation. They do not have to match the aspect-card response scale.

---

## Interpretation Rule

Low expression is not the same as distorted expression.

A low-frequency expression may reflect:

- low trait activation;
- context restriction;
- social inhibition;
- role suppression;
- limited opportunity;
- uncertainty;
- observer mismatch.

Distorted expression requires active counter-pattern evidence and should be reviewed through expression integrity, reconciliation, and possible Karma context when relevant.

---

## Digital Schema Note

Future databases should store expression evidence separately from aspect scores.

Suggested fields:

```text
expression_id
parent_aspect
candidate_facet
expression_text
validation_scale_type
response_value
observer_type
symbol_tags
reconciliation_cues
possible_karma_review_context
validation_status
```
