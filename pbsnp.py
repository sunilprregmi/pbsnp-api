import json
import requests

def fetch_nepalese_pbs():
    url = "https://np4.sunilprasad.com.np/api"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        data = response.json()
        
        output_file = "nepalese-pbs.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"Data saved successfully to {output_file}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    fetch_nepalese_pbs()
