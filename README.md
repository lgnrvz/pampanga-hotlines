# Pampanga Emergency Hotlines

Lightweight, offline-ready directory of emergency hotlines for Pampanga province, Philippines. Covers all 22 cities/municipalities — police, fire, disaster response, hospitals, utilities, and government agencies.

🌐 **Live site:** [lgnrvz.github.io/pampanga-hotlines](https://lgnrvz.github.io/pampanga-hotlines)

## About

This is a static site with no dependencies. All hotline data is stored in `hotlines.json`. Just open `index.html` in any browser — no build step, no server required.

## Contributing

Numbers change, offices move, new hotlines get published — we rely on the community to keep this accurate. If you spot an outdated number, a missing contact, or have a more legit/verified source:

1. **Fork** this repo
2. **Edit** `hotlines.json` (or `index.html` if it's structural)
3. **Submit a Pull Request** with:
   - What you changed and why
   - A source reference (LGU Facebook post, official website, verified public listing)

PRs without a source may take longer to review. We prioritize community-verified numbers over third-party aggregators.

### Format

Entries in `hotlines.json` use this structure:

```json
{
  "police": [
    { "city": "Angeles City", "numbers": ["(045) 322-7796", "0917-851-9581"] }
  ],
  "hospitals": [
    { "name": "JBLMGH", "city": "San Fernando", "numbers": ["(045) 961-3363"], "er": true }
  ]
}
```

- `er: true` means the hospital has a 24/7 emergency room
- `er: "(045) 625-9389"` means it has a direct ER number

## Data

- `hotlines.json` — Complete directory of emergency contacts
- `index.html` — Searchable, mobile-friendly web interface
- `refresh.py` — Weekly automated refresh script

## Cities & Municipalities Covered

Angeles City, Apalit, Arayat, Bacolor, Candaba, Floridablanca, Guagua, Lubao, Mabalacat City, Macabebe, Magalang, Masantol, Mexico, Minalin, Porac, City of San Fernando (capital), San Luis, San Simon, Santa Ana, Santa Rita, Santo Tomas, Sasmuan

## License

Data compiled for public service. Use it, share it, improve it.
