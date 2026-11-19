from maizehybrid.prediction import rank_crosses, heterosis_pct
from maizehybrid.germplasm import dent_x_flint_pairs


def test_rank_crosses_puts_best_first():
    crosses = [
        {"id": "X-1", "female_id": "D1", "male_id": "F1",
         "predicted_yield_t_per_ha": "12.0", "heterosis_pct": "10", "status": "planned"},
        {"id": "X-2", "female_id": "D2", "male_id": "F2",
         "predicted_yield_t_per_ha": "13.4", "heterosis_pct": "18", "status": "planned"},
    ]
    assert rank_crosses(crosses)[0]["id"] == "X-2"


def test_heterosis():
    # mid-parent 10.0, hybrid 12.0 -> 20%
    assert heterosis_pct(10.0, 10.0, 12.0) == 20.0


def test_dent_x_flint_pairs():
    dents = [{"id": "D1"}, {"id": "D2"}]
    flints = [{"id": "F1"}]
    assert dent_x_flint_pairs(dents, flints) == [("D1", "F1"), ("D2", "F1")]
