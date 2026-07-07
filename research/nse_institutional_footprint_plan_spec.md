# SPEC-1-NSE Institutional Footprint Dashboard

## Background

Build a local Python-based NSE end-of-day scanner for individual investors to detect possible institutional accumulation using delivery percentage, delivery trend, volume, price structure, money flow, and relative strength.

The system will keep the backend database local and publish only generated Markdown/HTML reports to GitHub Pages for mobile viewing.

The enhanced delivery indicator must include a delivery spike tag, 20-session Unicode sparkline, consecutive high-delivery days, and delivery percentile.

---

## Requirements

### Must Have

- Python-only local application.
- Local SQLite database.
- NSE EOD bhavcopy and delivery data ingestion.
- NIFTYMIDSML400 as primary benchmark.
- 20-day delivery trend sparkline.
- Delivery percentile using previous 252 sessions.
- Consecutive high-delivery day count.
- Institutional Campaign Score, or ICS.
- Markdown reports.
- Static mobile-first HTML reports.
- GitHub Pages compatible `docs/` output.
- Do not commit local database or raw data to GitHub.

### Should Have

- Watchlist report.
- Sector rotation report.
- Fresh institutional entries report.
- Per-stock HTML pages.
- Plotly charts.
- Backtest summary.

### Could Have

- GitHub Actions later.
- Telegram/email alerts later.
- Weekly summary.
- Signal success tracking.

### Won’t Have in MVP

- Intraday data.
- Live alerts.
- Cloud database.
- Web server.
- React frontend.
- ML model.

---

## Method

### Final Architecture

```text
Local Machine
   │
   ▼
NSE EOD Download Scripts
   │
   ▼
SQLite Database
   │
   ▼
Indicators + Delivery Engine
   │
   ▼
Institutional Campaign Score
   │
   ▼
Markdown + Static HTML Reports
   │
   ▼
GitHub Repository docs/
   │
   ▼
GitHub Pages Mobile Dashboard
```

---

## Repository Structure

```text
nse-footprint/
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── download.py
│   ├── import_data.py
│   ├── indicators.py
│   ├── delivery.py
│   ├── relative_strength.py
│   ├── scoring.py
│   ├── lifecycle.py
│   ├── reports.py
│   ├── charts.py
│   ├── html.py
│   ├── publish.py
│   └── backtest.py
│
├── templates/
│   ├── base.html.j2
│   ├── index.html.j2
│   ├── report.html.j2
│   ├── stock.html.j2
│   ├── report.md.j2
│   └── stock.md.j2
│
├── docs/
│   ├── index.html
│   ├── fresh.html
│   ├── elite.html
│   ├── building.html
│   ├── breakouts.html
│   ├── sectors.html
│   ├── watchlist.html
│   ├── distribution.html
│   └── stocks/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── tests/
├── config.yaml
├── config.example.yaml
├── requirements.txt
├── README.md
└── .gitignore
```

---

## `.gitignore`

```gitignore
footprint.db
*.db
*.sqlite
data/
cache/
.env
config.yaml
watchlist.private.yaml
__pycache__/
.pytest_cache/
```

---

## Python Dependencies

```txt
pandas
numpy
requests
beautifulsoup4
pyyaml
jinja2
plotly
python-dateutil
tqdm
pytest
```

Optional later:

```txt
ta
scipy
```

---

## Configuration

### `config.example.yaml`

```yaml
database:
  path: footprint.db

market:
  benchmark: NIFTYMIDSML400
  universe: NSE_EQ

delivery:
  lookback: 20
  percentile_history: 252
  percentile_min_periods: 60
  spike_multiple: 1.5
  sparkline_blocks: "▁▂▃▄▅▆▇█"

volume:
  lookback: 20
  spike_multiple: 1.5
  min_turnover_cr: 5

trend:
  ema_short: 20
  ema_mid: 50
  ema_long: 200

scoring:
  elite: 95
  strong: 85
  building: 70
  watch: 55

  weights:
    delivery_trend: 30
    volume_quality: 20
    price_structure: 20
    money_flow: 15
    relative_strength: 15

reports:
  top_n: 50
  output_dir: docs
  mobile_first: true

watchlist:
  - BEL
  - HAL
  - LT
```

---

## Database Schema

Use SQLite.

### `stocks`

```sql
CREATE TABLE IF NOT EXISTS stocks (
    symbol TEXT PRIMARY KEY,
    company_name TEXT,
    series TEXT,
    isin TEXT,
    sector TEXT,
    industry TEXT,
    active INTEGER DEFAULT 1
);
```

### `daily_prices`

```sql
CREATE TABLE IF NOT EXISTS daily_prices (
    trade_date TEXT NOT NULL,
    symbol TEXT NOT NULL,
    open REAL,
    high REAL,
    low REAL,
    close REAL,
    prev_close REAL,
    volume INTEGER,
    turnover REAL,
    trades INTEGER,
    PRIMARY KEY (trade_date, symbol)
);
```

### `daily_delivery`

```sql
CREATE TABLE IF NOT EXISTS daily_delivery (
    trade_date TEXT NOT NULL,
    symbol TEXT NOT NULL,
    delivery_qty INTEGER,
    delivery_percent REAL,
    PRIMARY KEY (trade_date, symbol)
);
```

### `indicators`

```sql
CREATE TABLE IF NOT EXISTS indicators (
    trade_date TEXT NOT NULL,
    symbol TEXT NOT NULL,

    ema20 REAL,
    ema50 REAL,
    ema200 REAL,

    avg_volume20 REAL,
    volume_ratio20 REAL,
    avg_turnover20 REAL,
    turnover_ratio20 REAL,

    cmf20 REAL,
    cmf_positive_days INTEGER,

    obv REAL,
    obv_slope20 REAL,

    atr14 REAL,

    high20 REAL,
    high52w REAL,
    breakout20 INTEGER,
    breakout52w INTEGER,

    rs_20 REAL,
    rs_50 REAL,
    rs_100 REAL,
    rs_200 REAL,
    rs_percentile REAL,
    rs_trend TEXT,

    PRIMARY KEY (trade_date, symbol)
);
```

### `delivery_indicators`

```sql
CREATE TABLE IF NOT EXISTS delivery_indicators (
    trade_date TEXT NOT NULL,
    symbol TEXT NOT NULL,

    delivery_avg20 REAL,
    delivery_ratio20 REAL,
    delivery_slope20 REAL,
    delivery_momentum20 REAL,
    delivery_consistency20 REAL,

    delivery_percentile252 INTEGER,
    delivery_consecutive_high_days INTEGER,
    delivery_sparkline20 TEXT,
    delivery_visual_tag TEXT,

    PRIMARY KEY (trade_date, symbol)
);
```

### `scores`

```sql
CREATE TABLE IF NOT EXISTS scores (
    trade_date TEXT NOT NULL,
    symbol TEXT NOT NULL,

    delivery_score REAL,
    volume_score REAL,
    price_score REAL,
    money_flow_score REAL,
    relative_strength_score REAL,

    ics REAL,
    rating TEXT,
    lifecycle_stage TEXT,
    reason TEXT,

    first_elite_date TEXT,
    days_in_elite INTEGER,

    PRIMARY KEY (trade_date, symbol)
);
```

### `watchlist`

```sql
CREATE TABLE IF NOT EXISTS watchlist (
    symbol TEXT PRIMARY KEY,
    note TEXT,
    active INTEGER DEFAULT 1
);
```

### Indexes

```sql
CREATE INDEX IF NOT EXISTS idx_prices_symbol_date ON daily_prices(symbol, trade_date);
CREATE INDEX IF NOT EXISTS idx_delivery_symbol_date ON daily_delivery(symbol, trade_date);
CREATE INDEX IF NOT EXISTS idx_scores_date_ics ON scores(trade_date, ics DESC);
```

---

## Core Algorithms

### 1. Delivery Sparkline, 20 Sessions

Function:

```python
def delivery_sparkline(values: list[float], lookback: int = 20) -> str:
    """
    Return 20-character Unicode sparkline using delivery percentages.
    If fewer than 20 values exist, return ''.
    Normalize only across the 20 values.
    If all values are equal, return '▄' * 20.
    """
```

Rules:

```text
blocks = ▁ ▂ ▃ ▄ ▅ ▆ ▇ █
```

Formula:

```text
idx = round((value - min_value) / (max_value - min_value) * 7)
```

---

### 2. Delivery Percentile

Function:

```python
def delivery_percentile(
    history: list[float],
    lookback: int = 252,
    min_periods: int = 60
) -> int | None:
    """
    Compare latest delivery value against previous delivery history.
    Exclude latest value.
    Use up to previous 252 sessions.
    Return rounded percentile or None.
    """
```

Formula:

```text
percentile =
count(previous_values <= latest_value) / count(previous_values) * 100
```

---

### 3. Consecutive High-Delivery Days

Function:

```python
def consecutive_high_delivery_days(
    delivery_values: list[float],
    avg20_values: list[float],
    mult: float = 1.5
) -> int:
    """
    Count backward from latest session while:
    delivery >= prior_20_day_average * 1.5
    Stop on first non-spike day.
    """
```

Display only when count >= 2.

---

### 4. Delivery Visual Tag

Function:

```python
def delivery_visual_tag(symbol: str, trade_date: str) -> str:
    """
    Compose:
    DEL185% ▁▁▂▂▃▄▄▅▅▆▆▇▇██████ · 🔥4D · P98
    """
```

Rules:

- Show tag only when delivery qualifies as spike.
- Delivery spike:
  ```text
  latest_delivery >= delivery_avg20 * 1.5
  ```
- Add sparkline if available.
- Add `🔥nD` if consecutive days >= 2.
- Add `Pn` if percentile is available.

---

## Indicators

### Price

Calculate:

```text
EMA20
EMA50
EMA200
20-day high
52-week high
ATR14
20-day breakout
52-week breakout
```

### Volume

Calculate:

```text
avg_volume20
volume_ratio20
avg_turnover20
turnover_ratio20
```

### Money Flow

Calculate:

```text
CMF20
CMF positive persistence
OBV
OBV slope20
```

### Relative Strength

Primary benchmark:

```text
NIFTYMIDSML400
```

Calculate stock return divided by benchmark return over:

```text
20, 50, 100, 200 sessions
```

Then rank all stocks into `rs_percentile`.

Display:

```text
RS97↑
```

---

## Institutional Campaign Score

### Weights

```text
ICS =
30% Delivery Trend
20% Volume Quality
20% Price Structure
15% Money Flow
15% Relative Strength
```

---

### Delivery Score, 30 Points

| Condition | Points |
|---|---:|
| Latest delivery > 20-day average | 6 |
| Delivery ratio >= 1.5 | 6 |
| Delivery percentile >= 90 | 6 |
| Consecutive high delivery days >= 3 | 6 |
| 20-day delivery slope positive | 6 |

---

### Volume Score, 20 Points

| Condition | Points |
|---|---:|
| Volume ratio >= 1.5 | 6 |
| Turnover ratio >= 1.5 | 6 |
| Turnover >= configured minimum | 4 |
| Volume above average on up day | 4 |

---

### Price Score, 20 Points

| Condition | Points |
|---|---:|
| Close > EMA20 | 4 |
| Close > EMA50 | 4 |
| Close > EMA200 | 4 |
| 20-day breakout | 4 |
| Within 15% of 52-week high | 4 |

---

### Money Flow Score, 15 Points

| Condition | Points |
|---|---:|
| CMF20 > 0 | 5 |
| CMF positive for >= 3 days | 5 |
| OBV slope20 positive | 5 |

---

### Relative Strength Score, 15 Points

| Condition | Points |
|---|---:|
| RS percentile >= 90 | 8 |
| RS trend improving | 4 |
| Stock outperforming NIFTYMIDSML400 over 50 days | 3 |

---

## Rating

```text
95–100  ★★★★★ Elite Accumulation
85–94   ★★★★☆ Strong Institution
70–84   ★★★☆☆ Building Position
55–69   ★★☆☆☆ Watch
<55     ★☆☆☆☆ Ignore
```

---

## Lifecycle Stage

Assign one of:

```text
🟢 Seed
🌱 Building
🚀 Breakout
💰 Markup
⚠️ Distribution
```

Rules:

```text
Seed:
  delivery percentile >= 85
  price not yet in breakout

Building:
  ICS >= 70
  rising delivery slope
  CMF > 0
  no breakout yet

Breakout:
  breakout20 = true
  delivery percentile >= 90
  volume_ratio20 >= 1.5

Markup:
  close > EMA20
  close > EMA50
  RS percentile >= 90
  ICS >= 85

Distribution:
  price down
  volume_ratio20 >= 1.5
  CMF20 < 0
  OBV slope negative
```

---

## Reports

Generate Markdown and HTML for each report.

### Output Files

```text
docs/index.html
docs/index.md

docs/fresh.html
docs/fresh.md

docs/elite.html
docs/elite.md

docs/building.html
docs/building.md

docs/breakouts.html
docs/breakouts.md

docs/sectors.html
docs/sectors.md

docs/watchlist.html
docs/watchlist.md

docs/distribution.html
docs/distribution.md

docs/stocks/{SYMBOL}.html
docs/stocks/{SYMBOL}.md
```

---

## Mobile-First HTML Design

### Requirements

- Single-column layout.
- Dark mode default.
- Sticky top navigation.
- Stock cards instead of wide tables.
- No horizontal scrolling.
- Large font for symbol and ICS.
- Unicode sparklines.
- Search/filter by symbol using vanilla JavaScript.
- No React.
- No backend.
- GitHub Pages compatible.

### Navigation

```text
Dashboard | Fresh | Elite | Building | Breakouts | Sectors | Watchlist
```

---

## Stock Card Format

```text
★★★★★ BEL
ICS96 · 🚀 Breakout

RS97↑ · SEC95↑
EMA20 · EMA50 · HH20 · ↑CMF4D

DEL185% ▁▁▂▂▃▄▄▅▅▆▆▇▇██████ · 🔥4D · P98

Vol2.6× · ₹145Cr traded

Why:
Delivery P98, 4-day accumulation, 20-day breakout, RS leader
```

---

## Dashboard Report

Purpose:

```text
What happened today?
```

Sections:

```text
Market Health
Fresh Institutional Entries
Top Elite Accumulation
Building Positions
Breakouts with Delivery
Sector Rotation
Watchlist Changes
Distribution Warnings
```

---

## Fresh Report

Criteria:

```text
Today rating is ★★★★★ or ★★★★☆
Yesterday rating was lower
```

Sort:

```text
ICS DESC
```

---

## Elite Report

Criteria:

```text
ICS >= 95
```

Sort:

```text
ICS DESC
```

---

## Building Report

Criteria:

```text
70 <= ICS < 95
No breakout yet
Delivery slope positive
RS trend improving
```

---

## Breakouts Report

Criteria:

```text
breakout20 = true OR breakout52w = true
delivery_percentile252 >= 90
volume_ratio20 >= 1.5
```

---

## Sector Rotation Report

Group by sector.

Metrics:

```text
Average ICS
Number of elite stocks
Number of fresh entries
Average RS percentile
Sector trend
```

---

## Watchlist Report

Use symbols from config.

Show:

```text
ICS today
ICS last 5 sessions
Rating change
Lifecycle change
Delivery visual tag
Reason
```

Example:

```text
BEL

ICS:
72 → 79 → 84 → 91 → 96

Stage:
🌱 → 🌱 → 🚀
```

---

## Distribution Report

Criteria:

```text
volume_ratio20 >= 1.5
CMF20 < 0
OBV slope20 < 0
close < previous close
```

---

## Per-Stock Pages

Each stock page should contain:

```text
Symbol summary
Latest ICS
Rating
Lifecycle stage
Delivery visual tag
Reason
Price chart
Delivery % chart
Delivery percentile chart
ICS history chart
RS chart
CMF chart
Recent 30-day table
```

Use Plotly HTML fragments.

---

## Implementation

### Phase 1 – Project Skeleton

Create:

```text
src/
templates/
docs/
data/raw/
data/processed/
tests/
```

Add:

```text
requirements.txt
config.example.yaml
.gitignore
README.md
```

Acceptance criteria:

```text
python -m src.config
python -m src.database
```

run without error.

---

### Phase 2 – SQLite Database

Implement `src/database.py`.

Functions:

```python
def get_connection() -> sqlite3.Connection
def init_db() -> None
def upsert_dataframe(table: str, df: pd.DataFrame, keys: list[str]) -> None
def fetch_df(query: str, params: tuple = ()) -> pd.DataFrame
```

Acceptance criteria:

- All tables created.
- Indexes created.
- Re-running init is safe.

---

### Phase 3 – NSE Data Ingestion

Implement:

```text
src/download.py
src/import_data.py
```

Functions:

```python
def download_bhavcopy(trade_date: date) -> Path
def download_delivery_file(trade_date: date) -> Path
def parse_bhavcopy(path: Path) -> pd.DataFrame
def parse_delivery(path: Path) -> pd.DataFrame
def import_trade_date(trade_date: date) -> None
```

Acceptance criteria:

- One trading day can be imported.
- Duplicate import does not create duplicate rows.
- Missing files are logged clearly.

---

### Phase 4 – Indicators

Implement `src/indicators.py`.

Functions:

```python
def calculate_price_indicators(symbol: str) -> pd.DataFrame
def calculate_volume_indicators(symbol: str) -> pd.DataFrame
def calculate_money_flow(symbol: str) -> pd.DataFrame
def calculate_all_indicators(trade_date: date | None = None) -> None
```

Acceptance criteria:

- EMA20/50/200 generated.
- Volume ratio generated.
- CMF and OBV generated.
- Breakout flags generated.

---

### Phase 5 – Delivery Engine

Implement `src/delivery.py`.

Functions:

```python
def delivery_sparkline(values: list[float], lookback: int = 20) -> str
def delivery_percentile(values: list[float], lookback: int = 252, min_periods: int = 60) -> int | None
def consecutive_high_delivery_days(delivery: list[float], avg20: list[float], mult: float = 1.5) -> int
def delivery_visual_tag(symbol: str, trade_date: str) -> str
def calculate_delivery_indicators(trade_date: date | None = None) -> None
```

Acceptance criteria:

- Sparkline is exactly 20 chars when enough data exists.
- Equal values return 20 middle blocks.
- Percentile excludes latest value.
- `🔥nD` appears only when n >= 2.
- No delivery tag appears without delivery spike.

---

### Phase 6 – Relative Strength

Implement `src/relative_strength.py`.

Functions:

```python
def calculate_benchmark_returns() -> pd.DataFrame
def calculate_stock_rs(symbol: str) -> pd.DataFrame
def calculate_rs_percentiles(trade_date: date) -> None
```

Acceptance criteria:

- RS calculated versus NIFTYMIDSML400.
- RS percentile calculated across universe.
- RS trend shown as ↑, →, or ↓.

---

### Phase 7 – Scoring

Implement `src/scoring.py`.

Functions:

```python
def calculate_delivery_score(row) -> float
def calculate_volume_score(row) -> float
def calculate_price_score(row) -> float
def calculate_money_flow_score(row) -> float
def calculate_relative_strength_score(row) -> float
def calculate_ics(row) -> float
def assign_rating(ics: float) -> str
def generate_reason(row) -> str
def calculate_scores(trade_date: date) -> None
```

Acceptance criteria:

- ICS between 0 and 100.
- Rating assigned correctly.
- Reasons are human-readable.
- Scores persist in database.

---

### Phase 8 – Lifecycle

Implement `src/lifecycle.py`.

Functions:

```python
def assign_lifecycle(row) -> str
def update_first_elite_dates(trade_date: date) -> None
def days_in_elite(symbol: str, trade_date: date) -> int
```

Acceptance criteria:

- Fresh elite entries detected.
- Days in elite calculated.
- Lifecycle stage visible in reports.

---

### Phase 9 – Markdown Reports

Implement `src/reports.py`.

Functions:

```python
def generate_index_md(trade_date: date) -> None
def generate_fresh_md(trade_date: date) -> None
def generate_elite_md(trade_date: date) -> None
def generate_building_md(trade_date: date) -> None
def generate_breakouts_md(trade_date: date) -> None
def generate_sectors_md(trade_date: date) -> None
def generate_watchlist_md(trade_date: date) -> None
def generate_distribution_md(trade_date: date) -> None
def generate_all_markdown(trade_date: date) -> None
```

Acceptance criteria:

- All `.md` files generated.
- Markdown readable directly in GitHub.
- Stock cards are compact.
- Delivery visual tag appears correctly.

---

### Phase 10 – HTML Reports

Implement:

```text
src/html.py
src/charts.py
```

Functions:

```python
def render_html_report(report_name: str, data: dict) -> None
def generate_stock_page(symbol: str, trade_date: date) -> None
def generate_all_html(trade_date: date) -> None
def generate_plotly_chart(symbol: str, chart_type: str) -> str
```

Acceptance criteria:

- `docs/index.html` opens locally.
- Mobile layout works.
- Navigation links work.
- Stock pages generated.
- Charts render without backend.

---

### Phase 11 – Publish

Implement `src/publish.py`.

Functions:

```python
def git_status() -> str
def commit_reports(message: str) -> None
def push_reports() -> None
```

Acceptance criteria:

- Only `docs/` and code are committed.
- Database and raw data are not committed.
- GitHub Pages can serve `docs/index.html`.

---

### Phase 12 – Backtest

Implement `src/backtest.py`.

Functions:

```python
def evaluate_signal_returns(start_date: date, end_date: date) -> pd.DataFrame
def calculate_forward_returns(symbol: str, signal_date: date) -> dict
def generate_backtest_report() -> None
```

Metrics:

```text
5-day return
10-day return
20-day return
60-day return
MFE
MAE
Win rate
Median return
False positive rate
```

Acceptance criteria:

- Backtest report generated.
- Elite signals evaluated historically.
- Summary added to weekly report.

---

## CLI Commands

Create `src/main.py`.

```bash
python -m src.main init-db
python -m src.main import --date 2026-07-07
python -m src.main indicators --date 2026-07-07
python -m src.main score --date 2026-07-07
python -m src.main reports --date 2026-07-07
python -m src.main publish
python -m src.main run-daily --date 2026-07-07
```

`run-daily` should execute:

```text
import
indicators
delivery
relative strength
score
reports
html
```

---

## Testing Plan

### Unit Tests

Create tests for:

```text
delivery_sparkline
delivery_percentile
consecutive_high_delivery_days
assign_rating
assign_lifecycle
calculate_ics
```

### Required Edge Cases

- Fewer than 20 delivery values.
- All delivery values equal.
- Fewer than 60 percentile observations.
- Missing benchmark data.
- Missing delivery file.
- Duplicate import.
- Zero volume.
- Illiquid stock.

---

## Milestones

### Milestone 1 – Skeleton + DB

Deliverables:

```text
Project structure
SQLite schema
Config loader
CLI init-db
```

### Milestone 2 – Data Import

Deliverables:

```text
Bhavcopy import
Delivery import
Daily merged dataset
```

### Milestone 3 – Indicators

Deliverables:

```text
EMA
Volume ratio
CMF
OBV
Breakouts
RS vs NIFTYMIDSML400
```

### Milestone 4 – Delivery Engine

Deliverables:

```text
20-day sparkline
Delivery percentile
Consecutive days
Delivery visual tag
```

### Milestone 5 – Scoring

Deliverables:

```text
ICS
Rating
Lifecycle
Reason generation
Fresh entry detection
```

### Milestone 6 – Reports

Deliverables:

```text
Markdown reports
HTML reports
Mobile CSS
Stock pages
Charts
```

### Milestone 7 – Publish

Deliverables:

```text
GitHub Pages docs output
Publish script
README setup guide
```

### Milestone 8 – Backtest

Deliverables:

```text
Signal performance report
Forward return calculations
Accuracy metrics
```

---

## Gathering Results

Evaluate quality using:

```text
Number of fresh elite signals per week
20-day return after fresh elite signal
Median return by rating bucket
False positive rate
Sector hit rate
Average days from Building to Breakout
Distribution warning accuracy
```

Weekly report should answer:

```text
Are elite signals outperforming?
Which sectors are producing successful signals?
Are false positives concentrated in illiquid stocks?
Should delivery or RS weights be adjusted?
```

---

## Definition of Done

MVP is complete when:

```text
1. A user can run one command after market close.
2. Local SQLite DB updates successfully.
3. Delivery indicators are calculated.
4. ICS scores are generated.
5. Markdown and HTML reports are written to docs/.
6. GitHub Pages opens cleanly on mobile.
7. Database and raw data remain local.
8. Fresh, Elite, Building, Breakout, Sector, Watchlist, and Distribution reports exist.
9. Stock pages exist for top signals.
10. At least basic unit tests pass.
```

---

## Codex / Claude Code First Prompt

Use this as the first implementation prompt:

```text
Build the MVP skeleton for the NSE Institutional Footprint Dashboard.

Follow SPEC-1 exactly.

Start with:
1. repository structure,
2. config loader,
3. SQLite schema,
4. CLI entrypoint,
5. delivery.py with tested functions:
   - delivery_sparkline
   - delivery_percentile
   - consecutive_high_delivery_days

Do not implement NSE download yet.
Do not add web server or React.
Keep database local.
Generated reports must go under docs/.
Add pytest tests for delivery.py.
```
