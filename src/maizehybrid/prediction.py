"""Module 2 — cross prediction (v0.2, GCA / SCA).

Model, from the Sanya trial (t/ha):
  hybrid yield = trial_mean + GCA_female + GCA_male + SCA

  trial_mean = mean of the two parent lines' own yields
  GCA(line)  = line_yield - trial_mean
  SCA        = hybrid_yield - trial_mean - GCA_female - GCA_male
  mid-parent heterosis = (hybrid - mid_parent) / mid_parent * 100
  better-parent heterosis = (hybrid - max(parent)) / max(parent) * 100

With 2 parent lines there is only 1 possible cross, so SCA is
estimated from that single cross, not from a multi-cross diallel.
That is stated in the code, not hidden. v1 (the Bot's job) adds
genomic selection and multi-site GCA/SCA once more crosses exist.

Drought / disease are not in the yield formula yet. They are
stored per line (1-5 in parent_lines.csv) and used as a
selection filter: a cross is selected only if both parents
score >= 4 on drought and disease. That is the v0.2 rule.
"""


def mid_parent(female_yield, male_yield):
    return (female_yield + male_yield) / 2


def heterosis_pct(female_yield, male_yield, hybrid_yield):
    """Mid-parent heterosis, %."""
    mid = mid_parent(female_yield, male_yield)
    if mid == 0:
        return 0.0
    return round((hybrid_yield - mid) / mid * 100, 1)


def better_parent_heterosis_pct(female_yield, male_yield, hybrid_yield):
    best = max(female_yield, male_yield)
    if best == 0:
        return 0.0
    return round((hybrid_yield - best) / best * 100, 1)


def gca(line_yield, trial_mean):
    return round(line_yield - trial_mean, 2)


def sca(hybrid_yield, trial_mean, gca_female, gca_male):
    return round(hybrid_yield - trial_mean - gca_female - gca_male, 2)


def predict_cross(female_yield, male_yield, hybrid_yield):
    """Full breakdown for one cross, from Sanya trial numbers."""
    mean = mid_parent(female_yield, male_yield)
    gca_f = gca(female_yield, mean)
    gca_m = gca(male_yield, mean)
    return {
        "trial_mean": round(mean, 2),
        "gca_female": gca_f,
        "gca_male": gca_m,
        "sca": sca(hybrid_yield, mean, gca_f, gca_m),
        "heterosis_pct": heterosis_pct(female_yield, male_yield, hybrid_yield),
        "better_parent_heterosis_pct": better_parent_heterosis_pct(
            female_yield, male_yield, hybrid_yield
        ),
        "predicted_yield_t_per_ha": hybrid_yield,
    }


def rank_crosses(crosses):
    return sorted(
        crosses,
        key=lambda c: (float(c["predicted_yield_t_per_ha"]), float(c["heterosis_pct"])),
        reverse=True,
    )
