# Deployment — Kazakhstan, past the Sanya numbers

Sanya proves the cross works in trial. Kazakhstan is where it
has to sell. This is what the Devin Bot builds first, in order.

## 1. Seed lot + QR (already in the repo)

- Lot MH-LOT-001: cross X-001, 5,000 kg, distributor Almaty Agro
  (synthetic demo name), status ready, QR MH-QR-001.
- Lot MH-LOT-002: 3,000 kg, Shymkent Seed, ready.
- Lot MH-LOT-003: 2,000 kg, Turkistan Growers, planned.
- Total demo stock: 10,000 kg of X-001.
- A grower scans the QR and sees: lot, cross, Sanya origin,
  13.4 t/ha, heterosis 14.0%, traits drought + disease,
  sowing guide for fresh-market sweet corn.

## 2. Distributor dashboard (RU / KZ / EN)

One screen per distributor, not a generic admin panel:

- Region: Almaty / Shymkent / Turkistan.
- Stock by lot, status ready / planned, QR per lot.
- Trial result attached to each lot, so a distributor can
  show a grower the Sanya numbers, not just a price.
- Language: Russian and Kazakh first, English for us.

## 3. Grower dashboard

- Scan QR -> yield, heterosis, traits, sowing guide.
- No account needed for the grower to read a lot.
- Orders go back to the distributor, not to us directly.

## 4. Offline trial capture (the part that replaces Sanya)

- Field staff in Kazakhstan record plots on a phone, offline.
- Data syncs when back online, and feeds into GCA/SCA.
- After one Kazakhstan season, the prediction no longer
  depends on Sanya alone — that is the explicit goal.

## 5. What is NOT claimed

- No Kazakhstan trial has run yet. Sanya is the only completed
  trial. Distributor names and lot numbers in `data/` are
  synthetic stand-ins for real partners.
- No yield is promised for Kazakhstan. The dashboard shows
  Sanya numbers labelled as Sanya, and Kazakhstan plots as
  planned until they are measured.
