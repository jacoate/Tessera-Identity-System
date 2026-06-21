# Domain Cards / Domain-Family Reference

Version: 0.2 Provisional
Status: Active / Provisional
Scope: Tessera Identity System personality taxonomy

---

## Overwrite Notice

This file replaces the prior six-domain domain-card draft that listed Honesty-Humility as an active personality domain and stated a current quantity of 6.

Reason for replacement:

- the current working personality taxonomy uses five domain families and ten primary aspects;
- Honesty-Humility is no longer treated as an active personality taxonomy branch or scored bridge;
- its moral content is represented by Karma dimensions, while non-moral residues may appear as neutral symbols, wording, or reconciliation context;
- future analog and digital implementations require a clearer separation between organizational taxonomy anchors and ethical interpretation mechanisms.

This document remains provisional and should be revised if later empirical review or system design identifies a nonredundant reason to alter the domain-family structure.

---

## 1. Definition

A Domain Family is a high-level organizational category within the Tessera personality architecture.

Domain families summarize related aspects and function as visual anchor nodes for identity map construction. They are not primary assessment units and should not be treated as independently validated Tessera scales unless later empirical work supports that use.

---

## 2. Purpose

### Organizational Purpose

Groups related aspects into a coherent navigation structure.

### Summary Purpose

Provides a high-level view of personality-expression territory.

### Mapping Purpose

Creates visual hierarchy and navigation within the identity map.

### Educational Purpose

Introduces personality structure in an accessible way without implying that domain families are directly tested.

---

## 3. Current Provisional Domain-Family Set

| Domain Family | Primary Aspects |
|---|---|
| Extraversion | Assertiveness; Enthusiasm |
| Agreeableness | Compassion; Politeness |
| Conscientiousness | Industriousness; Orderliness |
| Negative Emotionality / Neuroticism | Withdrawal; Volatility |
| Openness / Intellect | Openness; Intellect |

Current active domain-family count: 5.

Honesty-Humility is not currently an active domain family. It remains a source construct for Karma, symbols, wording, reconciliation context, and research lineage when nonredundant.

---

## 4. Domain-Family Design Requirements

A domain family should:

- contain multiple aspects;
- represent broad personality territory;
- provide meaningful organizational value;
- remain distinct from Karma dimensions;
- be compatible with empirical personality research where possible;
- remain open to revision when evidence or system architecture requires it.

A domain family should not be added merely to preserve a source model if its content is already represented more precisely elsewhere in Tessera.

---

## 5. Domain Card Specification

Card Type: Domain-Family Reference

Function: Organizational Anchor

Placement: Top Layer of Identity Map

Current Quantity: 5

Suggested Contents:

- Domain-family name
- Brief definition
- Associated aspects
- Identity map connections
- Source-lineage notes when useful
- Boundary note if overlap with Karma is likely

---

## 6. Current Assessment Status

Domain families are not directly assessed.

The current assessment architecture begins at the aspect level.

Any future domain aggregation methodology should be developed only after aspect cards, facet candidates, expression validation, and reconciliation procedures have been reviewed.

Domain-family summaries should use non-absolute language such as:

- appears consistent with;
- suggests a pattern in;
- may reflect higher/lower expression in;
- should be reviewed alongside.

---

## 7. Domain-to-Aspect Matrix

| Domain Family | Aspect 1 | Aspect 2 |
|---|---|---|
| Extraversion | Assertiveness | Enthusiasm |
| Agreeableness | Compassion | Politeness |
| Conscientiousness | Industriousness | Orderliness |
| Negative Emotionality / Neuroticism | Withdrawal | Volatility |
| Openness / Intellect | Openness | Intellect |

---

## 8. Identity Map Function

Domain-family cards occupy the highest organizational layer of the personality map. They help players see where aspect results cluster without implying that the domain family itself has been independently tested.

---

## 9. Digital Schema Note

Future digital implementations should model domain families as organizational containers rather than direct psychometric score objects unless later validation supports domain-level scoring.

Suggested field distinction:

```text
domain_family: organizational anchor
aspect: primary tested construct
facet: candidate expression channel
karma_dimension: separate ethical-context construct
```

---

## 10. Manual Revision Policy

Domain-family additions, removals, renamings, or reinterpretations require overwrite notice and review.

Empirically backed information should not be deleted. If a construct is removed from active architecture, its source-lineage and nonredundant content should be preserved or explicitly routed elsewhere.
