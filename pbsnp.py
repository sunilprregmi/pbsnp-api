import requests

def fetch_nepalese_pbs():
    url = "https://np4.sunilprasad.com.np/api"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return {"channels": []}

def save_api_data():
    output_file = "nepalese-pbs.json"
    
    # Fetch data directly from API
    api_data = fetch_nepalese_pbs()
    
    # Save/overwrite the data to file
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(api_data, f, indent=2, ensure_ascii=False)
    
    print(f"Data saved successfully to {output_file}")

if __name__ == "__main__":
    save_api_data()
