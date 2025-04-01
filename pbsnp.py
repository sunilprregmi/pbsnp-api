import requests
import os
from datetime import datetime

def fetch_nepalese_pbs():
    """Fetch channel data from Nepalese PBS API."""
    url = "https://np4.sunilprasad.com.np/api"
    headers = {
        "User-Agent": "GitHub-Nepalese-PBS-Updater/1.0"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("Error: API request timed out after 10 seconds")
        return {"channels": []}
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return {"channels": []}

def save_api_data(output_dir=""):
    """Save API data to file with timestamp in metadata."""
    # Construct output path
    output_file = os.path.join(output_dir, "nepalese-pbs.json")
    
    # Fetch data
    api_data = fetch_nepalese_pbs()
    
    # Add metadata
    metadata = {
        "last_updated": datetime.utcnow().isoformat() + "Z",
        "source": "https://np4.sunilprasad.com.np/api",
        "channel_count": len(api_data.get("channels", []))
    }
    output_data = {
        "metadata": metadata,
        "channels": api_data.get("channels", [])
    }
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        print(f"Data saved successfully to {output_file}")
        print(f"Channels fetched: {metadata['channel_count']}")
        return True
    except IOError as e:
        print(f"Error writing to file {output_file}: {e}")
        return False

def main():
    """Main execution function."""
    # Allow output directory to be set via environment variable
    output_dir = os.environ.get("OUTPUT_DIR", "")
    success = save_api_data(output_dir)
    
    # Exit with appropriate code for CI/CD
    exit(0 if success else 1)

if __name__ == "__main__":
    main()
