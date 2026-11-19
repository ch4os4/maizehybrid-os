import csv, pathlib
from .prediction import predict_cross, rank_crosses


def main():
    base = pathlib.Path(__file__).resolve().parents[2] / "data"
    with open(base / "parent_lines.csv") as f:
        parents = {r["id"]: r for r in csv.DictReader(f)}
    with open(base / "crosses.csv") as f:
        crosses = list(csv.DictReader(f))
    print("MaizeHybrid OS demo — Sanya trial, cross prediction:")
    for c in rank_crosses(crosses):
        f_y = float(parents[c["female_id"]]["yield_t_per_ha"])
        m_y = float(parents[c["male_id"]]["yield_t_per_ha"])
        h_y = float(c["predicted_yield_t_per_ha"])
        r = predict_cross(f_y, m_y, h_y)
        print(f"  {c['id']}: {c['female_id']} ({f_y}) x {c['male_id']} ({m_y})")
        print(f"    trial_mean {r['trial_mean']}, GCA_f {r['gca_female']}, "
              f"GCA_m {r['gca_male']}, SCA {r['sca']}")
        print(f"    hybrid {h_y} t/ha, mid-parent heterosis "
              f"{r['heterosis_pct']}%, better-parent {r['better_parent_heterosis_pct']}%")
        print(f"    check: {r['trial_mean']} + {r['gca_female']} + {r['gca_male']} "
              f"+ {r['sca']} = {h_y}")


if __name__ == "__main__":
    main()
