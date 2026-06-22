# Tessera Current Development Context

Status: active project-context handoff
Purpose: preserve the current development thread so older project chats can be deleted or ignored without losing continuity.
Scope: card-based Tessera tabletop identity mapping system.

---

## 1. Current Project Boundary

Tessera is currently scoped as a physical/card-based personality and identity mapping system.

The active project is not the broader MEIA-style application, simulation engine, or full developmental identity platform. Those materials may remain useful as theoretical references, but they should not steer active card-system implementation unless explicitly reintroduced.

The current system develops the tabletop identity map through this hierarchy:

```text
Domain
↓
Aspect
↓
Facet
↓
Expression
↓
Reconciliation
```

Each layer must have a distinct function and should not duplicate another layer.

The core design question is:

```text
How is this personality expressed?
```

not:

```text
What personality type is this?
```

---

## 2. Active Repository

Repository:

```text
jacoate/Tessera-Identity-System
```

Important committed project files so far:

```text
README.md
```

Defines the project as a tabletop personality identity mapping system and narrows the scope to the card system.

```text
docs/card-system/domain-cards.md
```

Defines domain cards as broad organizational anchors.

```text
docs/card-system/aspect-facet-taxonomy.md
```

Defines the active 8-aspect / 65-facet taxonomy.

```text
docs/card-system/rough-expression-library-model.md
```

Defines the rough expression library model and observer-readable behavior format.

This file exists to preserve the current project state after older chats are removed.

---

## 3. Development Process Rules

The user prefers:

1. Review before major repo commits whenever the structure is still speculative.
2. No hard locking of evolving material unless explicitly requested.
3. If a prior structure conflicts with new reasoning, the conflict should be surfaced.
4. Empirical inaccuracies or conceptual contradictions should be corrected directly.
5. The active repo should only contain material relevant to the current card-system build.
6. Broader theoretical material should be archived rather than allowed to confuse active progression.

The current vocabulary should avoid treating any unfinished model section as final.

Preferred labels:

```text
Draft
Working Model
Review Pending
Expression-Ready but Not Final
```

Avoid language implying irreversible lock-in unless the user explicitly requests it.

---

## 4. Domain Layer

Domains are organizational layout anchors.

They answer:

```text
What broad personality territory are we examining?
```

They do not answer:

```text
How does the person actually behave?
```

Current domain set:

1. Extraversion
2. Agreeableness
3. Conscientiousness
4. Neuroticism
5. Openness / Intellect
6. Honesty-Humility

Domain cards are essential fact cards and navigation aids.

Domains are not directly tested. Domain scoring or aggregation should only be implemented after the aspect system is sufficiently confirmed.

Academic updates to domains should not be automated. If future research requires domain revision, the user will manually update the system with resources.

---

## 5. Aspect Layer

Aspects are the primary assessment units.

They answer:

```text
How much of this disposition exists?
```

Current active aspect set:

1. Agency
2. Social Vitality
3. Communion
4. Self-Regulation
5. Emotional Stability
6. Exploration
7. Honesty
8. Reflection

Aspects are broad functional containers. They should not duplicate their own facets.

Domains summarize or organize aspect results later, but aspects are where assessment begins.

---

## 6. Current Aspect / Facet Taxonomy

The active taxonomy contains 8 aspects and 65 active facets.

### 6.1 Agency

Core theme: influence, initiative, effectiveness, goal pursuit, and directed action.

Facets:

1. Assertiveness
2. Leadership
3. Initiative
4. Influence
5. Self-Efficacy
6. Achievement Orientation
7. Courage
8. Visibility / Presence
9. Perseverance

Notes:

- Social Confidence was removed from Agency.
- The earlier Social Confidence construct was reinterpreted as social-environment endurance and moved to Social Vitality under the name Social Stamina.

### 6.2 Social Vitality

Core theme: social energy, interpersonal activation, expressive positivity, and sustained engagement.

Facets:

1. Sociability
2. Enthusiasm
3. Humor
4. Playfulness
5. Positive Affect
6. Affability
7. Personal Disclosure
8. Social Participation
9. Social Stamina

Notes:

- Social Vitality is understood through a vitality-bar metaphor.
- It describes how much social energy a person can bring through events before needing to settle or recharge.
- It also captures the ability to maintain upbeat, energetic, or charismatic expression under changing social demands.
- Hedonism was removed.
- Warmth was moved to Communion.

### 6.3 Communion

Core theme: relational orientation, interpersonal concern, affiliative tendency, and natural responsiveness to others.

Facets:

1. Compassion
2. Trust
3. Cooperation
4. Protectiveness
5. Warmth

Notes:

- Communion was retained after review.
- Communion represents relational tendencies, not ethical valuation.
- Karma handles relational ethics and moral utilization.
- Empathy, Altruism, Forgiveness, Gratitude, Punitive, and similar moralized constructs should not be folded into Communion unless specifically re-reviewed.

### 6.4 Self-Regulation

Core theme: discipline, planning, behavioral control, attention management, and follow-through.

Facets:

1. Organization
2. Planning
3. Prudence
4. Self-Discipline
5. Persistence
6. Deliberation
7. Detail Consciousness
8. Reliability
9. Attention Control

Notes:

- Organization and Orderliness were consolidated into Organization.
- Reliability remains under Self-Regulation.
- Reliability means behavioral follow-through and execution of accepted obligations.
- Honor handles valuing one’s word, but Reliability handles the disciplined act of following through.

Prudence vs. Deliberation:

- Deliberation = decision process, slowing down to consider options before acting.
- Prudence = consequence/risk sensitivity, considering preventable harm or long-term cost.

### 6.5 Emotional Stability

Core theme: emotional regulation, resilience, security, recovery, and tolerance of affective disruption.

Facets:

1. Emotional Regulation
2. Emotional Recovery
3. Emotional Threshold
4. Mood Stability
5. Security
6. Stress Tolerance
7. Emotional Awareness

Notes:

- Attachment Security was folded into Security.
- Security can branch into relational, situational, self-, future, and social security.
- Stress Tolerance and Frustration Tolerance were consolidated into Stress Tolerance.
- Emotional Awareness remains distinct from Reflection because it identifies emotional state, while introspective reflection examines self-process.

### 6.6 Exploration

Core theme: curiosity, novelty, imagination, intellectual engagement, complexity tolerance, and discovery through thought or experience.

Facets:

1. Inquisitiveness
2. Creativity
3. Imagination
4. Abstract Thinking
5. Aesthetic Appreciation
6. Novelty Seeking
7. Need for Cognition
8. Tolerance for Ambiguity
9. Experimentation

Notes:

- Intellectual Curiosity was renamed Inquisitiveness for readability and to avoid implying intelligence or IQ.
- Discovery Orientation was removed because it overlapped too strongly with Inquisitiveness, Novelty Seeking, and Experimentation.

### 6.7 Honesty

Core theme: truthfulness, transparency, reciprocity, principled conduct, and respect for one’s word.

Facets:

1. Truthfulness
2. Transparency
3. Reciprocity
4. Authentic Communication
5. Sincerity
6. Fairness
7. Honor

Notes:

- The duplicate Honesty facet under the Honesty aspect was removed.
- Promise Keeping was removed as a separate facet.
- Honor was added.
- Honor means the tendency to regard commitments, obligations, duties, and one’s word as binding principles of conduct.

Distinction:

- Truthfulness = accuracy of representation.
- Transparency = openness about relevant information.
- Sincerity = genuineness of intent.
- Honor = value placed on commitments and one’s word.
- Reliability = execution of commitments and belongs under Self-Regulation.

### 6.8 Reflection

Core theme: self-awareness, metacognition, perspective-taking, meaning construction, and revision of beliefs or identity.

Facets:

1. Introspection
2. Extrospection
3. Self-Knowledge
4. Perspective Taking
5. Metacognition
6. Meaning-Making
7. Identity Coherence
8. Self-Evaluation
9. Belief Examination
10. Cognitive Flexibility

Notes:

- Reflection was added as an eighth aspect because introspection/extrospection/metacognition did not fit cleanly elsewhere.
- Perspective Taking is placed here as cognitive perspective processing rather than moral empathy.
- Introspection is the process of self-examination.
- Self-Knowledge is the outcome of that process.

---

## 7. Karma Model

Karma is the Tessera name for the ethical overlay system.

Karma is not another personality aspect tree.

It evaluates the ethical direction, distortion, or utilization of personality tendencies.

Personality taxonomy answers:

```text
What tendency exists and how is it expressed?
```

Karma answers:

```text
How is that tendency ethically directed or distorted?
```

The Ethical Integrity model informing Karma treats ethical integrity as multidimensional rather than a single good/bad continuum.

Current Karma dimensions:

1. Authentic Presentation
   - Benevolent: Sincerity
   - Aversive: Strategic Deception
2. Relational Equity
   - Benevolent: Fairness / Exploitation Aversion
   - Aversive: Exploitative Orientation
3. Self-Regard Calibration
   - Benevolent: Modesty
   - Aversive: Grandiosity / Entitlement
4. Material Orientation
   - Benevolent: Greed-Avoidance
   - Aversive: Status-Striving / Materialism
5. Affective Empathy
   - Benevolent: Compassion / Responsiveness
   - Aversive: Callousness / Indifference
6. Accountability Orientation
   - Benevolent: Responsibility Acceptance
   - Aversive: Blame Deflection
7. Intentional Orientation
   - Benevolent: Benevolent Intent
   - Aversive: Malevolent / Indifferent Intent
8. Moral Reasoning
   - Benevolent: Sophisticated / Universal Principles
   - Aversive: Concrete / Egocentric
9. Constraint Internalization
   - Benevolent: Autonomous Ethics
   - Aversive: Heteronomous / External Regulation
10. Moral Sensitivity
   - Benevolent: High Harm Awareness
   - Aversive: Moral Blindness
11. Moral Courage
   - Benevolent: Cost-Bearing Willingness
   - Aversive: Cost-Avoidance / Compliance
12. Development Orientation
   - Benevolent: Growth-Open / Reflective
   - Aversive: Fixed / Defensive

Important Karma principle:

A personality tendency can be high while its expression is ethically distorted.

Example:

```text
Agency high
Leadership activation high
Expression integrity low
Karma shadow: dominance / relational inequity
```

This should not erase Agency. It should identify distorted implementation.

---

## 8. Assessment Methodology

### 8.1 Aspect Assessment

Aspects are assessed directly.

The assessment system uses repeated measurement rather than a single score.

Three-pass assessment:

1. Pass One: initial administration.
2. Pass Two: new card arrangement and different wording.
3. Pass Three: third independent administration with different wording and card selection.

Repeated testing measures:

1. Trait Strength
2. Trait Stability
3. Trait Variability

Large variance is not automatically error. It may indicate:

1. Context sensitivity
2. Role-dependent expression
3. Self-concept conflict
4. Situational modulation
5. Inconsistent self-perception

### 8.2 Facet Validation

Facets are interpretive channels rather than full psychometric inventories.

They answer:

```text
What kind of this aspect exists?
```

Facets receive abbreviated validation.

Facet cards should explain:

1. What tendency the facet represents.
2. What it looks like.
3. What behaviors emerge from it.
4. How it differs from neighboring facets.
5. Which expression cards become relevant.

### 8.3 Expression Validation

Expressions are behavioral evidence.

Expressions are not traits.

An expression is:

```text
A specific observable behavior that provides evidence for a facet.
```

Expressions answer:

```text
What observable evidence supports this facet?
```

---

## 9. Rough Expression Library Model

Expression items should be written as observer-readable behaviors.

Use:

```text
Speaks up when their position is challenged.
```

Avoid default first-person phrasing such as:

```text
I speak up when my position is challenged.
```

Reason:

The same card can be used by:

1. The individual mapping themself.
2. A therapist mapping a client.
3. A facilitator.
4. A third-party observer.

Current expression categories:

1. Behavioral
2. Communication
3. Decision-Making
4. Relational
5. Problem-Solving
6. Self-Management

The user prefers keeping all six expression constituent categories for wider contextual implementation.

Expression design rule:

Expressions should be observable, repeatable, specific, linked to one parent facet, and useful for self-report, observer report, or reconciliation.

---

## 10. Token Economy Direction

The token economy has not yet been committed as a model file.

Current rough idea:

- Scenario cards provide response options.
- The evaluator allocates a fixed pool of counters/tokens.
- Earlier draft: 10 counters, max 5 per option.
- Earlier draft: 8 options, with 6 additive and 2 inverse/aversive options.
- The exact number of options and ratio of additive/inverse options remains unresolved.

Important correction:

The system should not penalize choices merely for being too favorable.

Reason:

There is no legitimate objective unit of value for deciding when a not-bad or favorable trait presentation becomes too good. Penalizing favorable saturation would create social-engineered bias.

Replace the earlier idea of a favorability saturation penalty with:

```text
Identity-attractive aversive option design
```

and:

```text
Reconciliation triggering
```

The test should not punish someone for selecting favorable options.

It should reveal whether the path they select toward a desired identity contains a distorted mechanism.

Core syntax for scenario options:

```text
Observer-readable behavior + contextual pressure + surface-valid motive
```

A good aversive option should be:

1. Plausible
2. Self-justifiable
3. Contextually tempting
4. Behaviorally specific
5. Not cartoonishly bad

Example functional leadership option:

```text
Clarifies the group's goal so everyone can coordinate under time pressure.
```

Example aversive leadership-coded option:

```text
Takes over the plan so the group stops slowing things down.
```

The second option has surface appeal as decisiveness or efficiency but may encode dominance, low cooperation, or poor deliberation depending on context.

Important scoring distinction:

Aversive expression should not always reduce trait activation.

It may show:

```text
Trait activation high
Expression integrity low
Karma shadow active
```

Recommended future score layers:

1. Trait Activation Score
2. Expression Integrity Score
3. Karma Shadow Flag
4. Reconciliation Trigger

This preserves the possibility that a trait exists strongly but is implemented poorly.

---

## 11. Reconciliation Section: Blank-Slate Purpose

The Reconciliation branch has just begun.

Current working purpose:

```text
Reconciliation identifies, interprets, and organizes contradictions between personality assessment results, expression evidence, Karma indicators, and self/observer interpretation so the final identity map preserves complexity rather than forcing artificial consistency.
```

Shortest principle:

```text
Contradiction is data.
```

Reconciliation exists to explain meaningful mismatches between:

1. Aspect scores
2. Facet validation
3. Expression evidence
4. Token allocation patterns
5. Karma-shadow indicators
6. Self-concept
7. Observer interpretation
8. Contextual constraints

Reconciliation is not:

1. A punishment system
2. A diagnostic label
3. A simple score correction tool
4. A morality judgment
5. A forced resolution engine

Reconciliation functions:

1. Explain trait-expression gaps.
2. Explain self-concept versus behavior gaps.
3. Explain positive trait with distorted expression.
4. Preserve context sensitivity.
5. Route the next step.

Possible reconciliation card candidates:

1. Situational Restriction
2. Social Inhibition
3. Selective Expression
4. Role Suppression
5. Measurement Error
6. Opportunity Deficit
7. Desired-Self Projection
8. Role Misinterpretation
9. Low Expression Literacy
10. Context Misread
11. Karma-Expression Mismatch
12. Identity Conflict
13. Trait-Expression Gap
14. Observer/Self Disagreement
15. Context-Specific Activation
16. Suppressed Expression
17. Malformed Expression
18. Ethical Distortion
19. Identity Transition

These are not finalized.

---

## 12. Current Next Steps

Immediate branch:

```text
Reconciliation section as a blank slate
```

First task:

```text
Determine the purpose of Reconciliation.
```

Likely next repo files after this context file:

```text
docs/card-system/reconciliation-model.md
```

and later:

```text
docs/card-system/token-economy-model.md
```

The token economy model should be built before final expression-card content because it will govern all testing mechanics.

---

## 13. Current Active Design Principles

1. The card system should preserve complexity rather than flatten it.
2. Contradictions should be interpreted before being treated as errors.
3. Self-report bias should be managed through forced tradeoff, scenario pressure, observer-readable phrasing, and identity-attractive aversive options.
4. Negative options should not be obvious traps.
5. Aversive options should represent distorted expression, not simply low trait expression.
6. Karma flags should not replace personality scores.
7. Expression integrity and trait activation may diverge.
8. The identity map should show tendency, expression, distortion, context, and reconciliation.
9. Material not yet implemented should be archived instead of mixed into active system docs.

---

## 14. Current Clean Working Thread

The recommended clean working order is:

1. Confirm Reconciliation purpose.
2. Draft Reconciliation model structure.
3. Draft Reconciliation card categories.
4. Return to token economy model.
5. Use token model to define expression-card scoring.
6. Build card content for taxonomy and Karma system.
7. Integrate all layers into final identity-map flow.
