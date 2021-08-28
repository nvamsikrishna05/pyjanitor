import pytest
from hypothesis import given  # noqa: F401


@pytest.mark.functions
def test_rename_columns(dataframe):
    df = dataframe.clean_names().rename_columns(
        {"a": "index", "bell_chart": "chart"}
    )
    assert set(df.columns) == set(
        ["index", "chart", "decorated_elephant", "animals@#$%^", "cities"]
    )
    assert "a" not in set(df.columns)


@pytest.mark.functions
def test_rename_columns_absent_column(dataframe):
    """
    rename_column should raise an error if the column is absent.
    """
    df = dataframe.copy()
    with pytest.raises(ValueError):
        df.clean_names().rename_columns({"a": "index", "bb": "chart"})

    assert set(df.columns) == set(dataframe.columns)


@pytest.mark.functions
def test_rename_columns_function(dataframe):
    df = dataframe.clean_names().rename_columns(function=str.upper)
    assert set(df.columns) == set(
        ["A", "BELL_CHART", "DECORATED_ELEPHANT", "ANIMALS@#$%^", "CITIES"]
    )

    assert "a" not in set(df.columns)


@pytest.mark.functions
def test_rename_columns_no_args(dataframe):
    df = dataframe.copy()
    with pytest.raises(ValueError):
        df.clean_names().rename_columns()

    assert set(df.columns) == set(dataframe.columns)
