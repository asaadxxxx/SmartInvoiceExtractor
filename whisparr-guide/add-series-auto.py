import json
import requests
from datetime import datetime

# ====================================================
# Whisparr Auto-Add Series Script
# سكريبت إضافة تلقائية للمسلسلات إلى Whisparr
# ====================================================

class WhisparrAutoAdd:
    def __init__(self, whisparr_url, api_key, quality_profile_id=1, root_folder_id=1):
        """
        Initialize Whisparr API client
        
        Args:
            whisparr_url: Whisparr server URL (e.g., http://localhost:6969)
            api_key: Whisparr API key
            quality_profile_id: Quality profile ID (default: 1)
            root_folder_id: Root folder ID (default: 1)
        """
        self.base_url = whisparr_url.rstrip('/')
        self.api_key = api_key
        self.quality_profile_id = quality_profile_id
        self.root_folder_id = root_folder_id
        self.headers = {
            'X-Api-Key': self.api_key,
            'Content-Type': 'application/json'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        self.added_count = 0
        self.failed_count = 0
        self.results = []

    def search_series(self, series_name):
        """
        Search for a series by name
        """
        try:
            url = f"{self.base_url}/api/v3/series/lookup"
            params = {'term': series_name}
            response = self.session.get(url, params=params, timeout=10)
            
            if response.status_code == 200:
                return response.json()
            else:
                print(f"❌ Error searching for '{series_name}': {response.status_code}")
                return []
        except Exception as e:
            print(f"❌ Exception searching for '{series_name}': {str(e)}")
            return []

    def add_series(self, series_data):
        """
        Add a series to Whisparr
        """
        try:
            # Prepare series data
            payload = {
                'title': series_data.get('title'),
                'foreignSeriesId': series_data.get('foreignSeriesId'),
                'tvdbId': series_data.get('tvdbId'),
                'qualityProfileId': self.quality_profile_id,
                'rootFolderPath': self.root_folder_id,
                'monitored': True,
                'addOptions': {
                    'searchForMissingEpisodes': True,
                    'ignoreEpisodesWithFiles': False,
                    'ignoreEpisodesWithoutFiles': False
                }
            }
            
            url = f"{self.base_url}/api/v3/series"
            response = self.session.post(url, json=payload, timeout=10)
            
            if response.status_code in [200, 201]:
                print(f"✅ Added: {series_data.get('title')}")
                self.added_count += 1
                self.results.append({
                    'status': 'success',
                    'title': series_data.get('title'),
                    'timestamp': datetime.now().isoformat()
                })
                return True
            else:
                print(f"❌ Failed to add '{series_data.get('title')}': {response.status_code}")
                self.failed_count += 1
                self.results.append({
                    'status': 'failed',
                    'title': series_data.get('title'),
                    'error': response.text,
                    'timestamp': datetime.now().isoformat()
                })
                return False
        except Exception as e:
            print(f"❌ Exception adding '{series_data.get('title')}': {str(e)}")
            self.failed_count += 1
            return False

    def add_series_by_name(self, series_name):
        """
        Search and add a series by name
        """
        print(f"🔍 Searching for: {series_name}")
        search_results = self.search_series(series_name)
        
        if search_results and len(search_results) > 0:
            # Use the first result
            series = search_results[0]
            print(f"   Found: {series.get('title')}")
            self.add_series(series)
        else:
            print(f"❌ Not found: {series_name}")
            self.failed_count += 1
            self.results.append({
                'status': 'not_found',
                'title': series_name,
                'timestamp': datetime.now().isoformat()
            })

    def add_multiple_series(self, series_list):
        """
        Add multiple series from a list
        """
        print(f"\n📺 Starting to add {len(series_list)} series...\n")
        
        for i, series_name in enumerate(series_list, 1):
            print(f"[{i}/{len(series_list)}] ", end="")
            self.add_series_by_name(series_name)
            # Add delay to avoid rate limiting
            import time
            time.sleep(0.5)
        
        self.print_summary()

    def print_summary(self):
        """
        Print summary of operations
        """
        print(f"\n" + "="*50)
        print(f"📊 Summary:")
        print(f"   ✅ Added: {self.added_count}")
        print(f"   ❌ Failed: {self.failed_count}")
        print(f"   📋 Total: {self.added_count + self.failed_count}")
        print(f"="*50 + "\n")

    def save_results(self, filename="whisparr_results.json"):
        """
        Save results to a JSON file
        """
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)
        print(f"💾 Results saved to: {filename}")


# ====================================================
# Main execution
# ====================================================

if __name__ == "__main__":
    # Configuration
    WHISPARR_URL = "http://localhost:6969"  # Change if needed
    API_KEY = "your-api-key-here"  # Get from Whisparr Settings
    QUALITY_PROFILE_ID = 1  # Default profile
    ROOT_FOLDER_ID = 1  # Default folder
    
    # List of 500 series to add
    SERIES_LIST = [
        "Game of Thrones",
        "The Sopranos",
        "Breaking Bad",
        "Dexter",
        "True Detective",
        "Boardwalk Empire",
        "The Wire",
        "Westworld",
        "The Handmaid's Tale",
        "Orange Is the New Black",
        "House of Cards",
        "Succession",
        "The Crown",
        "Ozark",
        "Mindhunter",
        "Chernobyl",
        "Watchmen",
        "The Leftovers",
        "Better Call Saul",
        "The Boys",
        # ... Add more series here
    ]
    
    print("")
    print("╔══════════════════════════════════════════╗")
    print("║ Whisparr Auto-Add Series Script          ║")
    print("║ سكريبت إضافة تلقائية للمسلسلات           ║")
    print("╚══════════════════════════════════════════╝")
    print("")
    
    # Initialize
    try:
        whisparr = WhisparrAutoAdd(
            whisparr_url=WHISPARR_URL,
            api_key=API_KEY,
            quality_profile_id=QUALITY_PROFILE_ID,
            root_folder_id=ROOT_FOLDER_ID
        )
        
        # Add series
        whisparr.add_multiple_series(SERIES_LIST)
        
        # Save results
        whisparr.save_results("whisparr_results.json")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("\n💡 Make sure:")
        print("   1. Whisparr is running")
        print("   2. API key is correct")
        print("   3. URL is correct")
