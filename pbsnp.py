import requests

def fetch_and_save_api_data():
    url = "https://np4.sunilprasad.com.np/api"
    output_file = "nepalese-pbs.json"
    
    try:
        response = requests.get(url, timeout=10, headers={"User-Agent": "PBS-Scraper/1.0"})
        response.raise_for_status()
        api_text = response.text
        
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(api_text)
        
        print(f"Successfully saved API response to {output_file}")
        return True
        
    except requests.exceptions.Timeout:
        print("Error: API request timed out after 10 seconds")
        return False
    except requests.exceptions.RequestException as e:
        print(f"Error fetching API data: {e}")
        return False
    except IOError as e:
        print(f"Error writing to file {output_file}: {e}")
        return False

if __name__ == "__main__":
    success = fetch_and_save_api_data()
    exit(0 if success else 1)
