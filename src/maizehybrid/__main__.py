import csv, pathlib
from .prediction import rank_crosses

def main():
    base = pathlib.Path(__file__).resolve().parents[2] / "data"
    with open(base / "crosses.csv") as f:
        crosses = list(csv.DictReader(f))
    print("MaizeHybrid OS demo — top crosses by predicted yield:")
    for c in rank_crosses(crosses):
        print(f"  {c['id']}: {c['female_id']} x {c['male_id']} "
              f"-> {c['predicted_yield_t_per_ha']} t/ha "
              f"(heterosis {c['heterosis_pct']}%, {c['status']})")

if __name__ == "__main__":
    main()
