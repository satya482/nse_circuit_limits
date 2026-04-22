import requests
import datetime
from dateutil.relativedelta import relativedelta
import csv
import json
from bs4 import BeautifulSoup

def get_tv_watchlist(url):
    print(f"Fetching TradingView Watchlist...")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Failed to fetch TradingView watchlist")
        return []
    soup = BeautifulSoup(response.text, 'html.parser')
    meta = soup.find('meta', property='og:description')
    if not meta:
        print("No og:description found")
        return []
    
    content = meta.get('content', '')
    # Tickers are usually comma separated
    tickers = [t.strip() for t in content.split(',')]
    return tickers

def fetch_nse_data(from_date_str, to_date_str):
    url = f"https://www.nseindia.com/api/eqsurvactions?from_date={from_date_str}&to_date={to_date_str}&csv=true"
    print(f"Fetching from: {url}")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36',
        'Accept': '*/*, text/csv',
    }
    
    session = requests.Session()
    session.headers.update(headers)
    
    try:
        session.get("https://www.nseindia.com", timeout=10)
        response = session.get(url, timeout=10)
        if response.status_code == 200:
            with open("nse.csv", "wb") as f:
                f.write(response.content)
            return True
        return False
    except Exception as e:
        print(f"Error fetching API: {e}")
        return False

def parse_nse_csv(filepath):
    results = []
    try:
        with open(filepath, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Clean up keys which might have trailing spaces like 'SYMBOL '
                clean_row = {k.strip(): v.strip() for k, v in row.items()}
                results.append(clean_row)
    except Exception as e:
        print(f"Error parsing CSV: {e}")
    return results

def hex_color(from_val, to_val):
    if from_val == '20' and to_val == '10':
        return '#f1c40f' # Yellow
    elif from_val == '10' and to_val == '5':
        return '#e74c3c' # Red
    elif from_val == '5' and to_val == '10':
        return '#2ecc71' # Green
    elif from_val == '10' and to_val == '20':
        return '#3498db' # Blue
    return None

def main():
    today = datetime.date.today()
    three_months_ago = today - relativedelta(months=3)
    to_date_str = today.strftime("%d-%m-%Y")
    from_date_str = three_months_ago.strftime("%d-%m-%Y")

    print(f"Running for {from_date_str} to {to_date_str}")
    
    tv_url = "https://in.tradingview.com/watchlists/326037664/"
    watchlist = get_tv_watchlist(tv_url)
    print(f"Watchlist contains {len(watchlist)} symbols.")
    
    if fetch_nse_data(from_date_str, to_date_str):
        nse_data = parse_nse_csv('nse.csv')
        matches = []
        
        for item in nse_data:
            symbol = item.get('SYMBOL')
            from_val = item.get('FROM')
            to_val = item.get('TO')
            date_val = item.get('EFFECTIVE DATE')
            
            if not symbol or not from_val or not to_val:
                continue
            
            color = hex_color(from_val, to_val)
            if color and symbol in watchlist:
                matches.append({
                    'date': date_val,
                    'symbol': symbol,
                    'name': item.get('SECURITY NAME', ''),
                    'from': from_val,
                    'to': to_val,
                    'color': color
                })
        
        print(f"Found {len(matches)} matching circuit limit changes.")
        
        # Generate markdown
        md_content = f"# NSE Circuit Limit Dashboard\n\n_Last updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_\n\n"
        md_content += "Changes in your TradingView watchlist:\n\n"
        md_content += "| Date | Symbol | Name | From | To |\n"
        md_content += "|---|---|---|---|---|\n"
        
        # Sort by date descending (rough sort assuming it's already sorted by NSE or we can just parse)
        # Assuming NSE provides latest first
        for m in matches:
            # We can't easily color rows in standard github markdown, but we can add an emoji or text color hint if needed.
            if m['color'] == '#f1c40f': color_name = "🟨 Yellow"
            elif m['color'] == '#e74c3c': color_name = "🟥 Red"
            elif m['color'] == '#2ecc71': color_name = "🟩 Green"
            elif m['color'] == '#3498db': color_name = "🟦 Blue"
            else: color_name = ""
            
            tv = f"https://in.tradingview.com/chart/?symbol=NSE:{m['symbol']}"
            md_content += f"| {m['date']} | [**{m['symbol']}**]({tv}) | {m['name']} | {m['from']}% | {m['to']}% {color_name} |\n"
            
        with open("NSE_Circuit_Limits.md", "w", encoding='utf-8') as f:
            f.write(md_content)
            
        # Generate HTML Dashboard
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Circuit Limits Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-color: #0f172a;
            --card-bg: #1e293b;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --border-color: #334155;
        }}
        body {{
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-main);
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }}
        .header {{
            text-align: center;
            margin-bottom: 40px;
            width: 100%;
            max-width: 800px;
        }}
        .header h1 {{
            font-size: 2rem;
            margin-bottom: 10px;
            background: -webkit-linear-gradient(#fff, #94a3b8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .header p {{
            color: var(--text-muted);
            font-size: 0.9rem;
        }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 20px;
            width: 100%;
            max-width: 1000px;
        }}
        .card {{
            background-color: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            transition: transform 0.2s, box-shadow 0.2s;
            position: relative;
            overflow: hidden;
        }}
        .card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        }}
        .card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background-color: var(--accent);
        }}
        .symbol {{
            font-size: 1.5rem;
            font-weight: 700;
            margin: 0 0 5px 0;
        }}
        .name {{
            font-size: 0.85rem;
            color: var(--text-muted);
            margin: 0 0 15px 0;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}
        .limits {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            background-color: rgba(0,0,0,0.2);
            padding: 10px;
            border-radius: 8px;
        }}
        .limit-box {{
            text-align: center;
        }}
        .limit-val {{
            font-size: 1.25rem;
            font-weight: 700;
        }}
        .limit-label {{
            font-size: 0.75rem;
            color: var(--text-muted);
            text-transform: uppercase;
        }}
        .arrow {{
            color: var(--accent);
            font-size: 1.5rem;
            font-weight: bold;
        }}
        .date {{
            margin-top: 15px;
            font-size: 0.75rem;
            color: var(--text-muted);
            text-align: right;
        }}
        .empty-state {{
            text-align: center;
            color: var(--text-muted);
            padding: 40px;
            grid-column: 1 / -1;
            background: var(--card-bg);
            border-radius: 12px;
        }}
        @media (max-width: 600px) {{
            .grid {{
                grid-template-columns: 1fr;
            }}
        }}
        .controls {{
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 30px;
            gap: 10px;
            width: 100%;
            max-width: 1000px;
        }}
        .controls select {{
            padding: 8px 12px;
            border-radius: 8px;
            background-color: var(--card-bg);
            color: var(--text-main);
            border: 1px solid var(--border-color);
            font-family: inherit;
            cursor: pointer;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Circuit Limits Dashboard</h1>
        <p>Tracking Watchlist Limit Changes • Last updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </div>
    
    <div class="controls">
        <label for="sortSelect">Sort By: </label>
        <select id="sortSelect" onchange="sortCards()">
            <option value="date-desc">Date (Newest)</option>
            <option value="date-asc">Date (Oldest)</option>
            <option value="symbol-asc">Symbol (A-Z)</option>
            <option value="symbol-desc">Symbol (Z-A)</option>
            <option value="from-desc">From % (High-Low)</option>
            <option value="from-asc">From % (Low-High)</option>
            <option value="to-desc">To % (High-Low)</option>
            <option value="to-asc">To % (Low-High)</option>
        </select>
    </div>

    <div class="grid" id="cardGrid">
"""
        if not matches:
            html_content += f"""        <div class="empty-state">
            <h2>No Recent Changes</h2>
            <p>None of the symbols in your watchlist have changed limits in the tracked patterns recently.</p>
        </div>"""
        else:
            for m in matches:
                html_content += f"""        <div class="card" style="--accent: {m['color']};" data-date="{m['date']}" data-symbol="{m['symbol']}" data-from="{m['from']}" data-to="{m['to']}">
            <h2 class="symbol">{m['symbol']}</h2>
            <p class="name" title="{m['name']}">{m['name']}</p>
            <div class="limits">
                <div class="limit-box">
                    <div class="limit-label">From</div>
                    <div class="limit-val">{m['from']}%</div>
                </div>
                <div class="arrow">→</div>
                <div class="limit-box">
                    <div class="limit-label">To</div>
                    <div class="limit-val" style="color: {m['color']}">{m['to']}%</div>
                </div>
            </div>
            <div class="date">{m['date']}</div>
        </div>
"""
        html_content += """    </div>

    <script>
        function sortCards() {
            const grid = document.getElementById('cardGrid');
            if (!grid) return;
            const cards = Array.from(grid.querySelectorAll('.card'));
            const sortVal = document.getElementById('sortSelect').value;
            
            cards.sort((a, b) => {
                if (sortVal === 'date-desc') {
                    return new Date(b.dataset.date) - new Date(a.dataset.date);
                } else if (sortVal === 'date-asc') {
                    return new Date(a.dataset.date) - new Date(b.dataset.date);
                } else if (sortVal === 'symbol-asc') {
                    return a.dataset.symbol.localeCompare(b.dataset.symbol);
                } else if (sortVal === 'symbol-desc') {
                    return b.dataset.symbol.localeCompare(a.dataset.symbol);
                } else if (sortVal === 'from-desc') {
                    return parseFloat(b.dataset.from) - parseFloat(a.dataset.from);
                } else if (sortVal === 'from-asc') {
                    return parseFloat(a.dataset.from) - parseFloat(b.dataset.from);
                } else if (sortVal === 'to-desc') {
                    return parseFloat(b.dataset.to) - parseFloat(a.dataset.to);
                } else if (sortVal === 'to-asc') {
                    return parseFloat(a.dataset.to) - parseFloat(b.dataset.to);
                }
            });

            cards.forEach(card => grid.appendChild(card));
        }
        
        // Initial sort
        sortCards();
    </script>
</body>
</html>"""
        
        with open("index.html", "w", encoding='utf-8') as f:
            f.write(html_content)
            
        print("Dashboard generated successfully.")
    else:
        print("Failed to download or parse NSE data.")

if __name__ == "__main__":
    main()
