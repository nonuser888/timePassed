#!/usr/bin/env python3
"""CLI that shows year progress: * = days passed, O = days remaining."""

import sys
from datetime import date


def days_in_year(y: int) -> int:
    """Return 366 if leap year, else 365."""
    return 366 if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0) else 365


def main() -> None:
    today = date.today()
    year = today.year
    total = days_in_year(year)
    # Day of year, 1-based (Jan 1 = 1)
    passed = today.timetuple().tm_yday
    remaining = total - passed

    passed_str = "*" * passed
    remaining_str = "O" * remaining
    bar = passed_str + remaining_str

    # Optional: wrap at 73 chars for readability (or show one long line)
    width = 73
    lines = [bar[i : i + width] for i in range(0, len(bar), width)]

    print(f"\n  {year}: {passed} days passed, {remaining} days left ({total} total)\n")
    for line in lines:
        print(f"  {line}")
    print(f"\n  Legend: * = passed ({passed})   O = remaining ({remaining})\n")
    sys.exit(0)


if __name__ == "__main__":
    main()
