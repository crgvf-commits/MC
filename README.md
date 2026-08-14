# Monte Carlo Robustness Analysis

This repository contains the supplementary results of the Monte Carlo
robustness analysis reported in the paper:

"A Layered Federated Architecture for Cyber Threat Intelligence Sharing:
Governance and Empirical Routing Validation"

## Purpose

The analysis evaluates whether the utility ordering between the federated
and centralized CTI-sharing architectures remains stable under uncertainty
in the criterion weights.

The Monte Carlo experiment uses five weighting regimes and 100,000
independent replications per regime.

The architecture-level indicator values are prespecified scenario parameters
and should not be interpreted as direct empirical measurements of
operational CTI-network performance.

## Files

- `monte_carlo_results.csv`: Monte Carlo results for the five weighting regimes.

## Reported measures

The file reports, for each weighting regime:

- probability that federated utility exceeds centralized utility;
- probability that centralized utility exceeds federated utility;
- mean utility difference;
- median utility difference;
- 2.5th percentile;
- 97.5th percentile.

The utility difference is defined as:

Delta U = Uf - Uc

where Uf represents the utility of the federated architecture and Uc the
utility of the centralized architecture.
