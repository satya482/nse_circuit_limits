import requests
import datetime
from dateutil.relativedelta import relativedelta

def fetch_nse_data():
    today = datetime.date(2026, 4, 17) # mocked to today based on metadata
    three_months_ago = today - relativedelta(months=3)
    
    # Format dd-mm-yyyy
    to_date = today.strftime("%d-%m-%Y")
    from_date = three_months_ago.strftime("%d-%m-%Y")
    
    url = f"https://www.nseindia.com/api/eqsurvactions?from_date={from_date}&to_date={to_date}&csv=true"
    print(f"Fetching from: {url}")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Connection': 'keep-alive',
    }
    
    session = requests.Session()
    session.headers.update(headers)
    
    # First get the main page to populate cookies
    try:
        print("Fetching home page for cookies...")
        session.get("https://www.nseindia.com", timeout=10)
    except Exception as e:
        print(f"Error fetching home page: {e}")
        
    try:
        print("Fetching API...")
        response = session.get(url, timeout=10)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print("Successfully fetched!")
            # Save the CSV to a file to examine
            with open("nse.csv", "wb") as f:
                f.write(response.content)
            print("Saved to nse.csv")
            
            # Print first 5 lines
            lines = response.text.split('\n')
            for i in range(min(5, len(lines))):
                print(lines[i])
        else:
            print("Failed to fetch.")
            print(response.text[:200])
    except Exception as e:
        print(f"Error fetching API: {e}")

if __name__ == "__main__":
    fetch_nse_data()
