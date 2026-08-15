# Supplementary Artifacts for A Layered Federated Architecture for Cyber Threat Intelligence Sharing

This repository contains supplementary artifacts associated with the anonymized manuscript:

**A Layered Federated Architecture for Cyber Threat Intelligence Sharing**

The materials support inspection of the empirical corpus, the sector classification process, and the Monte Carlo robustness analysis reported in the paper.

## Purpose

The study evaluates a layered federated governance architecture for cyber threat intelligence sharing.

The empirical evaluation uses public CTI records to examine whether explicit contextual evidence can support selective and auditable sector routing.

The supplementary artifacts are provided to improve transparency, auditability, and reproducibility of the empirical classification and robustness analysis.

## Repository Contents

### `corpus_inventory.xlsx`

Corpus inventory associated with the empirical evaluation.

The manuscript reports a total of **7,854 processable CTI records**, comprising:

- 7,850 processable MISP events;
- 4 CISA STIX advisories.

The inventory documents the records considered in the empirical corpus and their provenance.

### `empirical_sector_classification.xlsx`

Empirical classification artifact associated with the layered architecture.

The classification procedure assigns a record to an N1 sector only when explicit sector evidence is present in the original record title or in a sectoral tag.

The manuscript reports:

- **181 records** with sufficient explicit sector evidence;
- **214 sector associations**;
- **21 records** associated with more than one sector;
- **7,673 unresolved records**.

Unresolved records are not treated as irrelevant. Their status indicates only that the evaluated title and tag fields do not provide sufficient evidence for automatic sector assignment.

Any N2 or N3 information in the classification artifact represents proposed downstream treatment or routing possibilities. It must not be interpreted as an observed delivery, an operational recipient, or an empirically validated N2 or N3 destination.

### `monte_carlo.py`

Python script used to reproduce the Monte Carlo robustness analysis reported in the paper.

The script contains:

- the reference scenario indicators for the centralized and federated architectures;
- the Dirichlet concentration parameters for the five weighting regimes;
- the simulation procedure;
- 100,000 replications per weighting regime;
- generation of the detailed Monte Carlo results file.

The architecture indicator values are predefined scenario parameters and must not be interpreted as direct empirical measurements of operational CTI network performance.

### `monte_carlo_results.csv`

Detailed numerical results of the Monte Carlo robustness analysis.

The experiment evaluates whether the modeled utility ordering between the federated and centralized architectures remains stable under uncertainty in the criterion weights.

Five weighting regimes are considered:

1. Diffuse
2. Balanced and concentrated
3. Context and actionability priority
4. Exposure control priority
5. Latency and noise priority

For each regime, the file reports:

- probability that federated utility exceeds centralized utility;
- probability that centralized utility exceeds federated utility;
- mean utility difference;
- median utility difference;
- 2.5th percentile;
- 97.5th percentile.

The utility difference is defined as:

`Delta U = Uf - Uc`

where:

- `Uf` is the modeled utility of the federated architecture;
- `Uc` is the modeled utility of the centralized architecture.

The simulation results must not be interpreted as direct empirical measurements of operational CTI network performance.

## Empirical Sector Domains

The empirical classification considers eight N1 functional domains:

| Code | Functional domain |
|------|-------------------|
| GOV | Digital government and public ICT |
| FIN | Finance, insurance, and payment services |
| EDU | Education, research, and academic networks |
| HLT | Health and health data services |
| ENE | Energy, oil, gas, and industrial infrastructure |
| TEL | Telecommunications and connectivity |
| TRA | Transportation, aviation, and logistics |
| INV | Justice, public security, intelligence, and digital forensics |

The manuscript reports the following distribution of sector associations:

| Domain | Associations |
|--------|-------------:|
| GOV | 47 |
| FIN | 81 |
| EDU | 10 |
| HLT | 12 |
| ENE | 24 |
| TEL | 17 |
| TRA | 12 |
| INV | 11 |
| **Total** | **214** |

Of the 214 reported associations:

- 89 are supported by explicit sectoral tags;
- 125 are supported by direct references in record titles.

## Classification Policy

Sector classification follows a conservative evidence policy.

A sector association is accepted only when supported by:

- an explicit sectoral tag; or
- a direct sector reference in the record title.

The following information is not sufficient by itself to establish a sector association:

- feed origin;
- country;
- malware family;
- threat level;
- TLP marking;
- indicator type;
- presence of an indicator of compromise.

Records without sufficient explicit evidence remain unresolved for contextual enrichment or human review.

Multiple sector associations are retained when the available evidence explicitly supports more than one domain.

## Data Provenance

The empirical corpus described in the manuscript is based on public CTI material.

The primary source is the CIRCL MISP OSINT feed.

The corpus also contains four CISA advisories available as STIX reports:

- AA23-144A, Volt Typhoon;
- AA23-061A, Royal Ransomware;
- AA23-352A, Play Ransomware;
- AA25-141B, LummaC2.

Nine additional manifest references without retrievable event payloads were excluded from processing, as described in the manuscript.

The public corpus is used to evaluate the classification mechanism. It does not reproduce the sensitivity, legal restrictions, or organizational conditions of an operational government CTI network.

## Interpretation of the Artifacts

The supplementary materials should be interpreted according to the scope of the paper.

The centralized baseline represents complete distribution of 7,854 records to the 27 Courts of Justice in the Brazilian state judiciary, producing 212,058 deliveries.

This value represents a dissemination surface used as an analytical baseline. It is not a measurement of observed network traffic, transferred bytes, analyst workload, or operational activity.

Similarly, sector associations represent routing eligibility supported by explicit evidence. They are not observed messages or defensive actions.

The empirical evaluation directly examines N1 sector classification. Selection among specific N2 and N3 recipients is outside the scope of the evaluated dataset.

## Reproducibility and Auditability

The corpus inventory and empirical classification workbook support independent inspection of the records and the evidence associated with the reported sector assignments.

The Monte Carlo script contains the reference scenario indicators, the Dirichlet concentration parameters defining the five weighting regimes, and the simulation procedure used in the robustness analysis.

The Monte Carlo results file provides the detailed numerical outputs reported in the paper.

Together, these artifacts support independent inspection of the empirical classification and reproduction of the Monte Carlo robustness analysis.

Independent analysis should preserve the methodological distinction between:

- observed source records;
- N1 sector associations supported by explicit evidence;
- proposed downstream routing possibilities;
- modeled architecture utility.

These categories should not be interpreted as equivalent operational measurements.

## Anonymization

The repository is intended to accompany an anonymized submission.

The supplementary materials do not intentionally identify the authors or their institutional affiliations.

## Status

Supplementary material for a manuscript under peer review.

The repository may be updated to improve documentation and reproducibility while preserving the methods, data definitions, and reported results of the submitted manuscript.
