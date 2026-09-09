"""Visualization utilities for clinical cohorts."""

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.axes import Axes


def plot_age_distribution(
    data: pd.DataFrame,
    age_column: str = "age",
    bins: int = 10,
    ax: Axes | None = None,
) -> Axes:
    """Plot the age distribution of a clinical cohort.

    Parameters
    ----------
    data
        DataFrame containing patient-level data.
    age_column
        Name of the column containing age in years.
    bins
        Number of histogram intervals.
    ax
        Existing Matplotlib axes. A new one is created when omitted.

    Returns
    -------
    matplotlib.axes.Axes
        Axes containing the age histogram.
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("data must be a pandas DataFrame")

    if age_column not in data.columns:
        raise ValueError(
            f"Missing required column: {age_column}"
        )

    if bins <= 0:
        raise ValueError("bins must be greater than zero")

    ages = pd.to_numeric(
        data[age_column],
        errors="coerce",
    ).dropna()

    if ages.empty:
        raise ValueError("age column has no numerical values")

    if (ages < 0).any():
        raise ValueError("age values must be non-negative")

    if ax is None:
        _, ax = plt.subplots(
            figsize=(8, 5),
            layout="constrained",
        )

    ax.hist(
        ages,
        bins=bins,
        color="#0072B2",
        edgecolor="white",
        linewidth=0.8,
    )

    ax.set_title(
        "Age distribution of the clinical cohort"
    )
    ax.set_xlabel("Age (years)")
    ax.set_ylabel("Patients")

    margin = max(
        1.0,
        float(ages.max() - ages.min()) * 0.05,
    )

    ax.set_xlim(
        max(0, float(ages.min()) - margin),
        float(ages.max()) + margin,
    )

    return ax
