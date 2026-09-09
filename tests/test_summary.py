"""Tests for the clinical summary utilities."""

import pandas as pd
import pytest

from lab04_git import summarize_clinical_data


def test_summarize_clinical_data_returns_expected_statistics():
    data = pd.DataFrame(
        {
            "age": [40, 50, 60],
            "hba1c": [6.5, 7.0, 7.5],
        }
    )

    result = summarize_clinical_data(data)
    result = result.set_index("variable")

    assert list(result.index) == ["age", "hba1c"]
    assert result.loc["age", "count"] == 3
    assert result.loc["age", "mean"] == pytest.approx(50.0)
    assert result.loc["age", "median"] == pytest.approx(50.0)
    assert result.loc["hba1c", "mean"] == pytest.approx(7.0)


def test_summarize_clinical_data_ignores_missing_values():
    data = pd.DataFrame(
        {
            "age": [40, None, 60],
            "hba1c": [6.5, 7.0, None],
        }
    )

    result = summarize_clinical_data(data).set_index(
        "variable"
    )

    assert result.loc["age", "count"] == 2
    assert result.loc["hba1c", "count"] == 2


def test_summarize_clinical_data_rejects_non_dataframe():
    with pytest.raises(
        TypeError,
        match="data must be a pandas DataFrame",
    ):
        summarize_clinical_data(
            {"age": [40], "hba1c": [7.0]}
        )


def test_summarize_clinical_data_reports_missing_columns():
    data = pd.DataFrame(
        {
            "age": [40, 50],
        }
    )

    with pytest.raises(
        ValueError,
        match="Missing required columns: hba1c",
    ):
        summarize_clinical_data(data)
