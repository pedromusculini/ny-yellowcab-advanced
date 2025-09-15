import pytest
import pandas as pd
from scripts.validate_curated import validate_curated_data

def test_validate_curated_data_valid():
    df = pd.DataFrame({
        'trip_speed_mph': [50, 30, 80],
        'tip_percentage': [10, 20, 5],
        'trip_type': ['short', 'medium', 'long'],
        'is_peak_hour': [0, 1, 0]
    })
    errors = validate_curated_data(df)
    assert len(errors) == 0

def test_validate_curated_data_invalid_speed():
    df = pd.DataFrame({
        'trip_speed_mph': [150],
        'tip_percentage': [10],
        'trip_type': ['short'],
        'is_peak_hour': [0]
    })
    errors = validate_curated_data(df)
    assert len(errors) == 1
    assert "Unrealistic speeds" in errors[0]

def test_validate_curated_data_invalid_tip():
    df = pd.DataFrame({
        'trip_speed_mph': [50],
        'tip_percentage': [150],
        'trip_type': ['short'],
        'is_peak_hour': [0]
    })
    errors = validate_curated_data(df)
    assert len(errors) == 1
    assert "Invalid tip percentages" in errors[0]

def test_validate_curated_data_invalid_type():
    df = pd.DataFrame({
        'trip_speed_mph': [50],
        'tip_percentage': [10],
        'trip_type': ['invalid'],
        'is_peak_hour': [0]
    })
    errors = validate_curated_data(df)
    assert len(errors) == 1
    assert "Invalid trip types" in errors[0]

def test_validate_curated_data_invalid_peak():
    df = pd.DataFrame({
        'trip_speed_mph': [50],
        'tip_percentage': [10],
        'trip_type': ['short'],
        'is_peak_hour': [2]
    })
    errors = validate_curated_data(df)
    assert len(errors) == 1
    assert "Invalid peak hour indicators" in errors[0]