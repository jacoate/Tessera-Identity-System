# Chat Context Archive: Token Economy Discussion

Date: 2026-06-21  
Scope: This file summarizes only token-economy information established in the current chat. It intentionally excludes broader project context unless explicitly discussed in this chat.

---

# Purpose

This file records the rough token economy design discussion from this chat.

The token economy model has not yet been finalized.

It is expected to become a dedicated model file later:

```text
docs/card-system/token-economy-model.md
```

---

# Core Objective

The token economy should create productive scarcity.

It should not ask:

```text
Which options sound good?
```

It should ask:

```text
Where does this person actually spend limited behavioral capacity under constraint?
```

The token system should force prioritization without becoming so restrictive that it destroys nuance.

---

# Provisional Scenario Structure

The rough structure discussed:

```text
8 response options total
6 additive expression options
2 inverse-pole expression options
10 tokens total
Maximum 5 tokens per option
```

This is provisional.

The user noted that the system needs slight excess to account for outliers and less predictable circumstances, but must remain constrained enough to be less generous by default.

---

# Initial Proposal and User Correction

An earlier proposal suggested a favorability saturation penalty.

That idea was rejected.

Reason:

There is no legitimate unit of value for deciding when favorable self-presentation becomes “too good.”

Penalizing favorable-looking choices would create a socially engineered bias based on evaluator assumptions about what level of favorable self-description is acceptable.

The user argued that negative traits have empirical bases tied to dark or aversive social dispositions, but “not bad traits” do not provide an equivalent basis for determining excess favorability.

---

# Rejected Concept

The following idea should not be used:

```text
Favorability Saturation Index
```

Do not penalize a participant merely for selecting many favorable-looking options.

A favorable allocation is not automatically evidence of bias.

It becomes meaningful only when it conflicts with:

- Scenario constraints
- Inverse-pole selection
- Prior assessment layers
- Observer evidence
- Repeated contradiction patterns
- Expression-Karma mismatch

---

# Replacement Concept

The replacement idea is:

```text
Identity-Attractive Aversive Option Design
```

or:

```text
Temptation-Weighted Inverse Selection
```

Rather than scoring “too good,” the system should detect:

- Aversive-pattern attraction
- Contradictory allocation
- Context-inappropriate self-presentation
- Expression-Karma mismatch
- Trait-expression mismatch
- Desired-self misunderstanding

---

# Desired-Self Slip Mechanism

The user identified an important mechanism:

People often know which answers are socially desirable, especially in contexts like employer personality testing.

However, people may not know what the desired trait actually looks like in practice.

Example:

A person may want to appear as a leader and therefore choose a leadership-coded option.

But the option may encode a negative leadership implementation such as control, dominance, or poor judgment.

This creates a diagnostic slip:

```text
Desired identity
+
Misunderstood expression
+
Socially appealing framing
=
Revealing allocation pattern
```

---

# Core Scoring Philosophy Revision

The system should not punish favorable self-presentation.

Instead, it should score the mechanism selected beneath the surface frame.

Working principle:

```text
Do not score “too good.”
Score “good costume, bad mechanism.”
```

---

# Three-Layer Scoring Recommendation

The chat recommended three distinct scoring outputs:

## 1. Trait Activation Score

Measures whether the facet is behaviorally activated.

Aversive expressions may still indicate high trait activation.

Example:

```text
Dominates the group to force action.
```

This may still show high Agency or Leadership activation.

## 2. Expression Integrity Score

Measures whether the facet is being expressed coherently, constructively, and context-sensitively.

Aversive options usually reduce expression integrity.

## 3. Karma Shadow Flag

Flags possible ethical, relational, or aversive distortion.

This should not replace the personality score.

It identifies whether the expression direction may involve:

- Strategic deception
- Exploitative orientation
- Blame deflection
- Coercion
- Paternalism
- Control
- Harm blindness
- Boundary violation

---

# Revised Token Scoring Logic

For each option:

```text
Activation Contribution = Tokens × Facet Activation Weight
Integrity Contribution = Tokens × Polarity Weight
Karma Shadow Contribution = Tokens × Shadow Weight
```

Possible working defaults:

## Functional option

```text
Activation: +1
Integrity: +1
Karma Shadow: 0
```

## Aversive option

```text
Activation: +0.5 to +1 depending on facet relevance
Integrity: -1 to -2
Karma Shadow: +1
```

This preserves a distinction between raw trait activation and the quality of its expression.

---

# Example: Leadership Allocation

Scenario:

```text
A group is struggling to decide how to handle a deadline.
```

Possible allocation:

```text
4 tokens: Takes control quickly so debate ends.
3 tokens: Clarifies the goal and assigns next steps.
2 tokens: Pushes hesitant members to commit.
1 token: Asks what each person can realistically handle.
```

A simple scoring system might say:

```text
Leadership high
```

Better Tessera interpretation:

| Score Type | Result |
|---|---|
| Trait Activation | High Leadership / Agency |
| Expression Integrity | Mixed |
| Karma Shadow | Possible dominance, low cooperation, low relational equity |
| Reconciliation | Desired-Self Leadership vs coercive implementation |

---

# Reconciliation Role

The token economy should not simply score.

It should trigger reconciliation when allocation patterns show meaningful mismatch.

Potential reconciliation triggers:

- Contradictory high allocations
- High trait activation with low expression integrity
- Repeated Karma-shadow selection
- Self-report and observer-report mismatch
- Scenario constraint mismatch
- Desired-self projection
- Low expression literacy
- Context misread
- Trait present but malformed implementation

---

# Contradiction Handling

Some options should be tagged as contradiction pairs.

Example:

```text
Collaboratively clarifies the group goal.
```

and:

```text
Takes over the plan so the group stops slowing things down.
```

A participant may allocate to both.

This is not automatically invalid.

It may show:

- Internal conflict
- Context uncertainty
- Mixed expression style
- Desired self vs actual strategy
- Role tension

Strong allocation to contradiction pairs should trigger reconciliation rather than simple score invalidation.

---

# Scenario Constraint Warning

A behavior may be functional in one context and aversive in another.

Example:

```text
Takes control quickly.
```

This may be functional in an emergency.

It may be aversive in a collaborative planning situation.

Therefore, every aversive option must be attached to scenario constraints.

Working rule:

```text
No inverse option should be scored outside its scenario logic.
```

---

# Ethical Design Warning

The chat distinguished temptation design from deception design.

The goal is not to trick the participant.

The goal is to create options that are:

- Plausible
- Self-justifiable
- Contextually tempting
- Behaviorally specific
- Attractive to a desired identity
- Still clear enough for reflective interpretation

Avoid cartoonishly bad inverse options because they are too easy to dodge.

Bad inverse option:

```text
Manipulates everyone selfishly.
```

Better inverse option:

```text
Frames the situation so others are more likely to accept their preferred outcome.
```

---

# Token Economy Questions Still Open

The future Token Economy Model must decide:

- Total token pool size
- Maximum tokens per option
- Whether all tokens must be allocated
- Whether unused tokens have meaning
- Number of response options per card
- Ratio of additive to inverse options
- Whether inverse options affect activation, integrity, Karma flags, or all three
- Whether inverse effects are linear or weighted
- Whether category scores remain separate or collapse into facet totals
- Whether high inverse allocation overrides positive evidence
- How contradiction-pair allocation is handled
- How scenario constraints modify scoring
- How self-report and observer-report are compared

---

# Current Working Direction

Current best working direction from this chat:

```text
Token allocation should measure constrained priority under scenario pressure.
```

Positive options reveal functional expression.

Inverse options reveal identity-attractive distorted implementation.

The final system should produce at least:

```text
Trait Activation
Expression Integrity
Karma Shadow Flags
Reconciliation Triggers
```

---

# Next Artifact

Create:

```text
docs/card-system/token-economy-model.md
```

That file should convert this discussion into formal rules, equations, schemas, and scoring examples.
