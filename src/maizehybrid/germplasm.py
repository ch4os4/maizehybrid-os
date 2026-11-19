"""Module 1 — germplasm / parent lines (stub interface)."""
import csv


def load_parent_lines(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def by_group(lines, group):
    return [l for l in lines if l["heterotic_group"] == group]


def dent_x_flint_pairs(dents, flints):
    """All possible Dent x Flint single crosses."""
    return [(d["id"], f["id"]) for d in dents for f in flints]
