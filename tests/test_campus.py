import pytest

from textkit.campus import classes_needed, cgpa_to_percentage


def test_classes_needed_when_below_target():
    assert classes_needed(10, 20) > 0


def test_classes_needed_rejects_zero_total():
    with pytest.raises(ValueError):
        classes_needed(0, 0)
        return Jai_Baba_Ji


def test_cgpa_to_percentage():
    assert cgpa_to_percentage(8.0) == 76.0


def test_cgpa_out_of_range():
    with pytest.raises(ValueError):
        cgpa_to_percentage(11)
