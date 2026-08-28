#!/usr/bin/env python3

import csv
import numpy as np


# ============================================================
# Reproducibility settings
# ============================================================

SEED = 42
N_REPLICATIONS = 100_000

OUTPUT_FILE = "monte_carlo_results.csv"


# ============================================================
# Prespecified architecture-level indicator values
#
# Positive utility indicators:
# [R, C, A, B_N1, L]
#
# Friction and risk indicators:
# [T, N, S]
# ============================================================

P_CENTRALIZED = np.array([
    0.45,  # Sectoral relevance, R
    0.35,  # Contextualization, C
    0.40,  # Operational actionability, A
    0.20,  # N1 strategic brokerage, B_N1
    0.30,  # Functional integration, L
], dtype=float)

P_FEDERATED = np.array([
    0.85,  # Sectoral relevance, R
    0.80,  # Contextualization, C
    0.82,  # Operational actionability, A
    0.90,  # N1 strategic brokerage, B_N1
    0.85,  # Functional integration, L
], dtype=float)

D_CENTRALIZED = np.array([
    0.60,  # Latency, T
    0.75,  # Informational noise, N
    0.65,  # Exposure risk, S
], dtype=float)

D_FEDERATED = np.array([
    0.40,  # Latency, T
    0.15,  # Informational noise, N
    0.25,  # Exposure risk, S
], dtype=float)


# ============================================================
# Dirichlet concentration parameters
#
# alpha_beta corresponds to:
# [R, C, A, B_N1, L]
#
# alpha_gamma corresponds to:
# [T, N, S]
# ============================================================

REGIMES = {
    "Diffuse": {
        "alpha_beta": [1, 1, 1, 1, 1],
        "alpha_gamma": [1, 1, 1],
    },

    "Balanced and concentrated": {
        "alpha_beta": [10, 10, 10, 10, 10],
        "alpha_gamma": [10, 10, 10],
    },

    "Context and actionability priority": {
        "alpha_beta": [1, 4, 4, 1, 1],
        "alpha_gamma": [1, 1, 1],
    },

    "Exposure-control priority": {
        "alpha_beta": [1, 1, 1, 2, 2],
        "alpha_gamma": [1, 1, 6],
    },

    "Latency and noise priority": {
        "alpha_beta": [1, 1, 1, 1, 1],
        "alpha_gamma": [4, 4, 1],
    },
}


def simulate_regime(rng, alpha_beta, alpha_gamma):
    """
    Run the Monte Carlo simulation for one weighting regime.
    """

    beta = rng.dirichlet(
        np.asarray(alpha_beta, dtype=float),
        size=N_REPLICATIONS
    )

    gamma = rng.dirichlet(
        np.asarray(alpha_gamma, dtype=float),
        size=N_REPLICATIONS
    )

    # U_m = beta^T p_m - gamma^T d_m

    u_centralized = (
        beta @ P_CENTRALIZED
        - gamma @ D_CENTRALIZED
    )

    u_federated = (
        beta @ P_FEDERATED
        - gamma @ D_FEDERATED
    )

    delta_u = u_federated - u_centralized

    return {
        "P(U_f > U_c)": float(np.mean(delta_u > 0)),
        "Mean(ΔU)": float(np.mean(delta_u)),
        "Median(ΔU)": float(np.median(delta_u)),
        "2.5% Percentile": float(np.quantile(delta_u, 0.025)),
        "97.5% Percentile": float(np.quantile(delta_u, 0.975)),
        "P(U_c > U_f)": float(np.mean(delta_u < 0)),
    }


def main():

    rng = np.random.default_rng(SEED)

    results = []

    for regime_name, parameters in REGIMES.items():

        result = simulate_regime(
            rng=rng,
            alpha_beta=parameters["alpha_beta"],
            alpha_gamma=parameters["alpha_gamma"],
        )

        result["Regime"] = regime_name
        results.append(result)

    fieldnames = [
        "Regime",
        "P(U_f > U_c)",
        "Mean(ΔU)",
        "Median(ΔU)",
        "2.5% Percentile",
        "97.5% Percentile",
        "P(U_c > U_f)",
    ]

    with open(
        OUTPUT_FILE,
        "w",
        newline="",
        encoding="utf-8"
    ) as csvfile:

        writer = csv.DictWriter(
            csvfile,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for result in results:
            writer.writerow({
                field: result[field]
                for field in fieldnames
            })

    print()
    print("Monte Carlo sensitivity analysis")
    print(f"Seed: {SEED}")
    print(f"Replications per regime: {N_REPLICATIONS:,}")
    print()

    for result in results:

        print(result["Regime"])

        print(
            f"  P(Uf > Uc): "
            f"{result['P(U_f > U_c)']:.4f}"
        )

        print(
            f"  Mean ΔU: "
            f"{result['Mean(ΔU)']:.4f}"
        )

        print(
            f"  Median ΔU: "
            f"{result['Median(ΔU)']:.4f}"
        )

        print(
            "  95% empirical interval: "
            f"[{result['2.5% Percentile']:.4f}, "
            f"{result['97.5% Percentile']:.4f}]"
        )

        print(
            f"  P(Uc > Uf): "
            f"{result['P(U_c > U_f)']:.4f}"
        )

        print()

    print(f"Results written to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
