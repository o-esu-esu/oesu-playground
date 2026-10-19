"""Small calculators every student needs."""

DEFAULT_TARGET = 75  # minimum attendance percentage most colleges ask for


def classes_needed(attended: int, total: int, target: float = DEFAULT_TARGET) -> int:
    """Return how many more classes you must attend in a row to reach ``target``%.

    Returns 0 if you are already at or above the target.

    >>> classes_needed(30, 50)
    30
    """
    if total <= 0:
        raise ValueError("total must be more than 0")
    extra = 0
    while (attended + extra) / (total + extra) * 100 < target:
        extra += 1
    return extra


def cgpa_to_percentage(cgpa: float) -> float:
    """Convert a 10-point CGPA to a percentage using the common x 9.5 rule.

    >>> cgpa_to_percentage(8.0)
    76.0
    """
    if cgpa < 0 or cgpa > 10:
        raise ValueError("CGPA must be between 0 and 10")
    return round(cgpa * 9.5, 2)
