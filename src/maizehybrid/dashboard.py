"""Module 6 — grower / distributor dashboard (v0.2, working stub).

What a distributor in Kazakhstan actually sees, in one screen:
  seed lot -> trial result -> stock -> grower order

All distributor / lot data in data/ is synthetic demo data, marked
as such. Real distributor names and lot numbers stay private.
"""
import csv


def load_csv(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def distributor_summary(distributors, seed_lots, crosses):
    """One row per distributor: region, lot, cross, yield, status."""
    cross_yield = {c["id"]: c["predicted_yield_t_per_ha"] for c in crosses}
    rows = []
    for d in distributors:
        lots = [l for l in seed_lots if l["distributor_id"] == d["id"]]
        for lot in lots:
            rows.append({
                "distributor": d["name"],
                "region": d["region"],
                "language": d["language"],
                "lot_id": lot["id"],
                "cross_id": lot["cross_id"],
                "yield_t_per_ha": cross_yield.get(lot["cross_id"], "?"),
                "stock_kg": lot["stock_kg"],
                "status": lot["status"],
                "qr": lot["qr_id"],
            })
    return rows


def grower_view(lot, cross):
    """What a grower scans from the QR on a seed bag."""
    return {
        "lot": lot["id"],
        "cross": lot["cross_id"],
        "origin_trial": "Sanya",
        "yield_t_per_ha": cross["predicted_yield_t_per_ha"],
        "heterosis_pct": cross["heterosis_pct"],
        "traits": "drought tolerance, disease resistance",
        "sowing": "sweet corn, fresh market",
    }


def deployment_checklist():
    """What the Bot ships first, in order. No vague 'dashboard'."""
    return [
        "1. Seed lot + QR: lot MH-LOT-001, X-001, Sanya origin, QR traceable to distributor",
        "2. Distributor screen (RU/KZ/EN): stock by region, Almaty / Shymkent / Turkistan",
        "3. Grower screen: scan QR -> yield, heterosis, traits, sowing guide",
        "4. Offline phone capture: trial plots in Kazakhstan sync when back online",
        "5. Trial intake: Kazakhstan plots feed back into GCA/SCA, replacing Sanya-only numbers",
    ]
