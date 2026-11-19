"""Module 2 — cross prediction (v0.1, simple ranking).

Real v1 will use GCA/SCA + genomic selection. For the scaffold,
rank by predicted yield, then heterosis. This is enough to show
Poke the pipeline is real and testable.
"""


def rank_crosses(crosses):
    return sorted(
        crosses,
        key=lambda c: (float(c["predicted_yield_t_per_ha"]), float(c["heterosis_pct"])),
        reverse=True,
    )


def heterosis_pct(female_yield, male_yield, hybrid_yield):
    """(hybrid - mid-parent) / mid-parent * 100."""
    mid = (female_yield + male_yield) / 2
    if mid == 0:
        return 0.0
    return round((hybrid_yield - mid) / mid * 100, 1)
