"""Clinical summary utilities."""

from collections.abc import Sequence

import pandas as pd

DEFAULT_COLUMNS = ("age", "hba1c")


def summarize_clinical_data(
    data: pd.DataFrame,
    columns: Sequence[str] = DEFAULT_COLUMNS,
) -> pd.DataFrame:
    """Summarize selected numerical clinical variables.

    Parameters
    ----------
    data
        DataFrame containing the clinical observations.
    columns
        Numerical columns to include in the summary.

    Returns
    -------
    pandas.DataFrame
        One row per variable with count, mean, standard deviation,
        median, minimum, and maximum.
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("data must be a pandas DataFrame")

    missing_columns = [
        column
        for column in columns
        if column not in data.columns
    ]

    if missing_columns:
        missing_text = ", ".join(missing_columns)
        raise ValueError(
            f"Missing required columns: {missing_text}"
        )

    summary = (
        data.loc[:, list(columns)]
        .agg(
            [
                "count",
                "mean",
                "std",
                "median",
                "min",
                "max",
            ]
        )
        .transpose()
    )

    summary.index.name = "variable"

    return summary.reset_index()
