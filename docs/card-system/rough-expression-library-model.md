# Rough Expression Library Model

Version: 0.1 Draft  
Status: Staged for Review  
Scope: Tessera Tabletop Card System

---

# Purpose

This document defines the rough working model for the Tessera expression library.

The expression library will translate facets into observer-readable behavioral evidence that can be used by:

- An individual mapping themself
- A therapist mapping a client
- A third-party observer
- A facilitator comparing self-report against observed behavior

The goal is to preserve a consistent perspective format regardless of who is performing the evaluation.

---

# Core Principle

Expressions are not traits.

Expressions are observable, repeatable behaviors that provide evidence for a facet.

An expression should answer:

```text
What behavior shows this facet in action?
```

---

# Expression Wording Standard

All expression items should use observer-readable phrasing.

## Avoid First-Person Integration Language

Do not use:

```text
I speak up when my position is challenged.
```

Use:

```text
Speaks up when their position is challenged.
```

## Reason

Observer-readable phrasing supports multiple use cases without rewriting the card content.

The same card can be interpreted by:

- The individual
- A therapist
- A researcher
- A facilitator
- A third-party observer

This avoids locking the tool into self-report format.

---

# Expression Categories

The current expression library uses six constituent categories:

| Category | Function |
|---|---|
| Behavioral | Observable action or conduct |
| Communication | Spoken, written, or expressive behavior |
| Decision-Making | Choice pattern or priority selection |
| Relational | Interpersonal behavior or social positioning |
| Problem-Solving | Response to obstacle, conflict, uncertainty, or complexity |
| Self-Management | Internal regulation, recovery, inhibition, or sustained control |

All six categories should remain available for every facet during the rough drafting stage.

Not every final card must use every category, but the full category set should be preserved so each facet can be examined across wider contexts.

---

# Why All Categories Are Retained

A single facet may express differently depending on context.

For example, Reliability can appear as:

| Category | Example Expression Direction |
|---|---|
| Behavioral | Completes agreed tasks |
| Communication | Gives updates when delayed |
| Decision-Making | Chooses follow-through over convenience |
| Relational | Becomes dependable to others |
| Problem-Solving | Creates systems to prevent dropped obligations |
| Self-Management | Continues despite fluctuating motivation |

This wider expression spread supports identity mapping across more than one life setting.

---

# Positive and Inverse Expression Structure

Expression scenarios should include both additive and subtractive options.

The current rough model uses:

```text
Scenario Card
↓
8 response options
↓
6 additive expression options
2 subtractive inverse-pole options
↓
10 tokens allocated
↓
Maximum 5 tokens per option
```

This is a provisional structure only.

The final number of options, tokens, and polarity ratios must be determined in the Token Economy Model.

---

# Additive Expression Options

Additive options represent observer-readable behaviors that support the target facet.

Example:

```text
Explains their position clearly when others disagree.
```

Potential scoring direction:

```text
Adds to the relevant expression category and parent facet.
```

---

# Subtractive Inverse-Pole Options

Subtractive options represent distorted, aversive, coercive, avoidant, manipulative, or malformed expression patterns.

They should not merely represent low expression.

## Weak inverse item

```text
Does not speak up.
```

This may simply indicate low assertiveness, inhibition, uncertainty, fear, context restriction, or role suppression.

## Stronger inverse-pole item

```text
Overrides others rather than stating a position clearly.
```

or

```text
Uses pressure to force agreement instead of communicating a position directly.
```

These show distorted expression rather than mere absence.

---

# Key Distinction

Low expression is not the same as negative expression.

```text
Low expression
≠
Aversive expression
```

A participant can show little evidence of a facet without showing harmful or distorted expression.

Subtractive options should therefore represent active counter-patterns, not simple absence.

---

# Karma Shadow Linkage

The Karma model should inform the flavor of inverse-pole options.

Karma does not replace personality scoring.

Instead, it helps identify when a personality expression is being used in an aversive or ethically distorted direction.

Example:

## Facet

```text
Influence
```

## Category

```text
Communication
```

## Additive expression

```text
Explains an idea in a way that helps others understand the choice.
```

## Inverse-pole expression

```text
Frames information selectively to steer others without giving them the full picture.
```

## Possible Karma shadow

```text
Strategic Deception
Exploitative Orientation
```

---

# Provisional Expression Item Schema

Each draft expression item should eventually be stored with the following fields:

| Field | Purpose |
|---|---|
| Aspect | Parent aspect |
| Facet | Parent facet |
| Expression Category | Behavioral, Communication, Decision-Making, Relational, Problem-Solving, or Self-Management |
| Positive Expression | Observer-readable additive behavior |
| Inverse Expression A | Observer-readable subtractive behavior |
| Inverse Expression B | Second subtractive behavior, preferably using a different distortion pattern |
| Likely Karma Shadow | Possible Karma dimension or negative-pole linkage |
| Scenario Use | Contexts where the expression may appear |
| Scoring Notes | How the expression should be treated during token allocation |

---

# Example Draft Expression Record

```text
Aspect: Honesty
Facet: Transparency
Expression Category: Communication

Positive Expression:
States relevant motives, limits, or uncertainty before others make a decision.

Inverse Expression A:
Withholds relevant information so others form a more favorable impression.

Inverse Expression B:
Reveals only the facts that protect their own position.

Likely Karma Shadow:
Strategic Deception / Exploitative Orientation

Scenario Use:
Negotiation, teamwork, apology, leadership, conflict, disclosure, shared decision-making.

Scoring Notes:
Positive expression adds to Transparency. Inverse expressions may subtract from expression integrity and flag Karma review.
```

---

# Token Economy Dependency

The expression library cannot be finalized until the token economy model is defined.

The token economy model must determine:

- Total tokens per scenario
- Maximum tokens per option
- Whether all tokens must be allocated
- Whether unused tokens have meaning
- Number of response options per card
- Ratio of additive to subtractive options
- Whether inverse options subtract from facet score, expression integrity, or both
- Whether inverse options trigger Karma flags
- Whether inverse options use linear subtraction or weighted subtraction
- Whether categories are scored separately or collapsed into facet totals
- Whether high allocation to inverse options overrides positive evidence

---

# Current Rough Scoring Assumption

Current provisional assumption:

```text
Positive expression options
→ Add to personality facet/category

Inverse expression options
→ Subtract from expression integrity
→ Flag possible Karma shadow dimension
```

This allows the model to preserve the distinction between:

```text
Personality tendency
```

and

```text
Ethical or relational direction of expression
```

---

# Implementation Notes

The expression library should be drafted before full card text is finalized.

The rough expression library should identify possible behaviors across all aspects, facets, and expression categories.

The token economy model should then define how those behaviors become testable card options.

After the token economy model is established, final expression cards can be written with consistent scoring rules.

---

# Next Step

Create the Token Economy Model.

Recommended file:

```text
docs/card-system/token-economy-model.md
```

That file should define the scoring mechanics, polarity handling, token allocation rules, and how personality expression scores interact with Karma flags.
