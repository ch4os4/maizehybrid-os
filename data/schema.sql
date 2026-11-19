-- MaizeHybrid OS — schema v0.1 (SQLite, synthetic demo data only)
CREATE TABLE IF NOT EXISTS parent_lines (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  heterotic_group TEXT CHECK (heterotic_group IN ('Dent','Flint','Other')),
  crop TEXT NOT NULL DEFAULT 'maize',
  maturity_days INTEGER,
  yield_t_per_ha REAL,
  drought_tolerance INTEGER CHECK (drought_tolerance BETWEEN 1 AND 5),
  disease_resistance INTEGER CHECK (disease_resistance BETWEEN 1 AND 5),
  source TEXT
);

CREATE TABLE IF NOT EXISTS crosses (
  id TEXT PRIMARY KEY,
  female_id TEXT REFERENCES parent_lines(id),
  male_id TEXT REFERENCES parent_lines(id),
  predicted_yield_t_per_ha REAL,
  heterosis_pct REAL,
  status TEXT CHECK (status IN ('planned','in_trial','selected','rejected')) DEFAULT 'planned'
);

CREATE TABLE IF NOT EXISTS field_trials (
  id TEXT PRIMARY KEY,
  cross_id TEXT REFERENCES crosses(id),
  site TEXT NOT NULL,
  plot TEXT,
  planted_date TEXT,
  yield_t_per_ha REAL,
  notes TEXT
);

CREATE TABLE IF NOT EXISTS traits (
  id TEXT PRIMARY KEY,
  cross_id TEXT REFERENCES crosses(id),
  gene TEXT NOT NULL,
  edit_type TEXT CHECK (edit_type IN ('CRISPR-Cas9','base_edit','marker_only')),
  trait TEXT NOT NULL,
  status TEXT CHECK (status IN ('proposed','validated','approved','rejected')) DEFAULT 'proposed'
);

CREATE TABLE IF NOT EXISTS seed_lots (
  id TEXT PRIMARY KEY,
  cross_id TEXT REFERENCES crosses(id),
  ip_number TEXT,
  quantity_kg REAL,
  qr_code TEXT
);
