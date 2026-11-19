# MaizeHybrid OS — 玉米杂交育种操作系统

> From DW577 oil sunflower to gene-edited hybrid sweet corn.
> A breeding pipeline OS for a family farm business in transition.

My family previously operated US-imported DW577 oil sunflower.
We now hold IP for a corn hybrid seed and are shifting to
gene-edited hybrid breeding — for edible / fruit (sweet) corn.

**Target market:** the five Central Asian Stans — Kazakhstan,
Kyrgyzstan, Tajikistan, Turkmenistan, Uzbekistan — plus Russia.
These are sweet-corn growing regions where drought tolerance and
disease resistance decide whether a variety sells.

**Breeding goals:** drought tolerance first, disease resistance
second. Yield and eating quality for fresh / fruit corn.

**Trial status:** field trial completed in Sanya. 2 parent lines.

This repo is the software side of that shift. It does **not** do
wet-lab gene editing. It manages the whole pipeline a Devin Bot
can own:

**Parent lines → cross prediction → field trials → trait registry → seed traceability → grower dashboard**

## Why this exists

- Hybrid corn is a $9.8B market in 2025, heading to $16.4B by 2034.
  CRISPR / genomic selection is compressing the breeding cycle.
- Traditional breeding lives in spreadsheets. That breaks when you go
  from one sunflower variety (DW577) to maize parent lines, crosses,
  and trial sites across Central Asia and Russia.
- We need one system of record before the next planting season.

## Modules (what the Devin Bot owns)

| # | Module | What it does | Est. PRs |
|---|--------|--------------|----------|
| 1 | `germplasm` | 2 parent lines, heterotic groups, genotype + phenotype | ~30 |
| 2 | `prediction` | Cross prediction, GCA / SCA, heterosis, yield ranking | ~35 |
| 3 | `trials` | Field trials: Sanya (done), Central Asia / Russia sites next | ~35 |
| 4 | `traits` | CRISPR trait registry: drought / disease edits, compliance | ~30 |
| 5 | `traceability` | Seed lots, IP number, QR, distributor chain (Stans + Russia) | ~30 |
| 6 | `dashboard` | Grower / distributor view, DW577 sunflower → maize transition | ~25 |
| | **Total** | | **~185** |

## Data

All data in `data/` is **synthetic demo data** for now — 2 parent
lines (the real count), 1 main cross, Sanya trial plots. Real
germplasm / trial data stays private and will replace it behind
env config. No real IP numbers are in this repo.

- `data/parent_lines.csv` — 2 parent lines
- `data/crosses.csv` — main hybrid cross
- `data/field_trials.csv` — Sanya trial
- `data/schema.sql` — SQLite schema

## Quick start

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .[dev]
pytest -q
python -m maizehybrid --demo
```

## Roadmap — next 30 days

1. Germplasm DB + import from CSV (week 1)
2. Cross prediction v1: GCA/SCA ranking from Sanya trial (week 1-2)
3. Field trial API + offline phone capture for Stans / Russia sites (week 2-3)
4. Trait registry + compliance checklist for drought / disease edits (week 3)
5. Seed lot traceability + QR (week 3-4)
6. Grower dashboard (week 4)

## Status

Skeleton / MVP scaffold. Modules 1-2 have working stubs + tests.
Modules 3-6 are defined interfaces, to be built by the Devin Bot.
