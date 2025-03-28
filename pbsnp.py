import json
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

def merge_json_files():
    input_file = "./openiptv.json"
    output_file = "nepalese-pbs.json"
    
    nepalese_pbs_data = fetch_nepalese_pbs()
    
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            openiptv_data = json.load(f)
    except FileNotFoundError:
        print(f"File {input_file} not found. Using empty list.")
        openiptv_data = {"channels": []}
    
    merged_channels = nepalese_pbs_data["channels"] + openiptv_data["channels"]
    
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump({"channels": merged_channels}, f, indent=2, ensure_ascii=False)
    
    print(f"Merged data saved successfully to {output_file}")

if __name__ == "__main__":
    merge_json_files()
