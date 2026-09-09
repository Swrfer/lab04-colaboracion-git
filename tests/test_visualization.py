"""Tests for the cohort visualization utilities."""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd
import pytest
from matplotlib.axes import Axes

from lab04_git import plot_age_distribution


def test_plot_age_distribution_returns_axes_with_labels():
    data = pd.DataFrame(
        {
            "age": [34, 42, 51, 63, 77],
        }
    )

    ax = plot_age_distribution(data, bins=5)

    assert isinstance(ax, Axes)
    assert ax.get_xlabel() == "Age (years)"
    assert ax.get_ylabel() == "Patients"
    assert "Age distribution" in ax.get_title()
    assert ax.get_xlim()[0] <= data["age"].min()
    assert ax.get_xlim()[1] >= data["age"].max()

    plt.close(ax.figure)


def test_plot_age_distribution_uses_existing_axes():
    data = pd.DataFrame(
        {
            "age": [40, 50, 60],
        }
    )
    _, supplied_ax = plt.subplots()

    returned_ax = plot_age_distribution(
        data,
        ax=supplied_ax,
    )

    assert returned_ax is supplied_ax

    plt.close(supplied_ax.figure)


def test_plot_age_distribution_reports_missing_column():
    data = pd.DataFrame(
        {
            "hba1c": [6.5, 7.0],
        }
    )

    with pytest.raises(
        ValueError,
        match="Missing required column: age",
    ):
        plot_age_distribution(data)


def test_plot_age_distribution_rejects_invalid_bins():
    data = pd.DataFrame(
        {
            "age": [40, 50],
        }
    )

    with pytest.raises(
        ValueError,
        match="bins must be greater than zero",
    ):
        plot_age_distribution(data, bins=0)


def test_plot_age_distribution_rejects_negative_age():
    data = pd.DataFrame(
        {
            "age": [40, -5],
        }
    )

    with pytest.raises(
        ValueError,
        match="age values must be non-negative",
    ):
        plot_age_distribution(data)
