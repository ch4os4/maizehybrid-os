from maizehybrid.dashboard import (
    distributor_summary, grower_view, deployment_checklist,
)


def test_distributor_summary():
    dists = [{"id": "D-KZ-01", "name": "Almaty Agro", "region": "Almaty Region", "language": "RU/KZ"}]
    lots = [{"id": "MH-LOT-001", "cross_id": "X-001", "distributor_id": "D-KZ-01",
             "stock_kg": "5000", "status": "ready", "qr_id": "MH-QR-001"}]
    crosses = [{"id": "X-001", "predicted_yield_t_per_ha": "13.4"}]
    rows = distributor_summary(dists, lots, crosses)
    assert len(rows) == 1
    assert rows[0]["region"] == "Almaty Region"
    assert rows[0]["stock_kg"] == "5000"
    assert rows[0]["qr"] == "MH-QR-001"


def test_grower_view():
    lot = {"id": "MH-LOT-001", "cross_id": "X-001"}
    cross = {"predicted_yield_t_per_ha": "13.4", "heterosis_pct": "14.0"}
    v = grower_view(lot, cross)
    assert v["origin_trial"] == "Sanya"
    assert v["yield_t_per_ha"] == "13.4"
    assert "drought" in v["traits"]


def test_deployment_checklist_has_5_steps():
    assert len(deployment_checklist()) == 5
