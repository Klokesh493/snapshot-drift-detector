import csv
import sys


def drift(row):
    return abs(int(row["expected_interval_hours"]) - int(row["actual_interval_hours"]))


def offenders(rows, tolerance=2):
    return [row["workload"] for row in rows if drift(row) > tolerance]


def main(path):
    with open(path, newline="", encoding="utf-8") as handle:
        for item in offenders(list(csv.DictReader(handle))):
            print(item)


if __name__ == "__main__":
    main(sys.argv[1])
