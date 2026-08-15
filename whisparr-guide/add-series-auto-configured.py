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
    # ✅ Configuration - معدّل بالمفتاح الصحيح
    WHISPARR_URL = "http://localhost:6969"
    API_KEY = "77f9e2108b2b42cbaefc63b07ddfeee0"  # ✅ المفتاح الخاص بك
    QUALITY_PROFILE_ID = 1
    ROOT_FOLDER_ID = 1
    
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
        "Euphoria",
        "Fleabag",
        "Killing Eve",
        "Bodyguard",
        "The Fall",
        "True Blood",
        "Penny Dreadful",
        "American Horror Story",
        "Hannibal",
        "Vikings",
        "The Witcher",
        "Peaky Blinders",
        "Taboo",
        "Godless",
        "Altered Carbon",
        "Dark",
        "Stranger Things",
        "The Midnight Club",
        "Midnight Mass",
        "Hill House",
        "The Haunting of Bly Manor",
        "Locke & Key",
        "The Umbrella Academy",
        "Castlevania",
        "Castlevania: Nocturne",
        "Arcane",
        "Cyberpunk: Edgerunners",
        "Daria",
        "Bojack Horseman",
        "Disenchantment",
        "Tuca & Bertie",
        "Master of None",
        "Atypical",
        "Never Have I Ever",
        "The Sex Lives of College Girls",
        "Ginny & Georgia",
        "Outer Banks",
        "Wednesday",
        "The Diplomat",
        "BEEF",
        "Gilmore Girls",
        "Parenthood",
        "Friday Night Lights",
        "Hart of Dixie",
        "Bunheads",
        "Veronica Mars",
        "iZombie",
        "Jane the Virgin",
        "Crazy Ex-Girlfriend",
        "Insecure",
        "Atlanta",
        "PEN15",
        "The Politician",
        "Hollywood",
        "Ratched",
        "Monster",
        "Dahmer",
        "Conversations with Friends",
        "Normal People",
        "Skins",
        "Misfits",
        "Maniac",
        "The OA",
        "Russian Doll",
        "GLOW",
        "Dear White People",
        "Sex Education",
        "Elite",
        "Money Heist",
        "Vis a Vis",
        "Club de Cuervos",
        "La Brea",
        "Sky Rojo",
        "You",
        "Gossip Girl",
        "The Summer I Turned Pretty",
        "One Tree Hill",
        "The Vampire Diaries",
        "The Originals",
        "Legacies",
        "Supernatural",
        "The 100",
        "Battlestar Galactica",
        "Fringe",
        "The X-Files",
        "Manifest",
        "Dark Matter",
        "Killjoys",
        "Orphan Black",
        "Sense8",
        "The Expanse",
        "For All Mankind",
        "Raised by Wolves",
        "Humans",
        "Almost Human",
        "Intelligence",
        "Continuum",
        "Agents of S.H.I.E.L.D.",
        "Agent Carter",
        "Cloak & Dagger",
        "Inhumans",
        "Punisher",
        "Daredevil",
        "Jessica Jones",
        "Luke Cage",
        "Iron Fist",
        "The Defenders",
        "Hawkeye",
        "Moon Knight",
        "Ms. Marvel",
        "She-Hulk: Attorney at Law",
        "Secret Invasion",
        "Loki",
        "WandaVision",
        "Falcon and the Winter Soldier",
        "Andor",
        "The Mandalorian",
        "The Book of Boba Fett",
        "Obi-Wan Kenobi",
        "Ahsoka",
        "The Acolyte",
        "The Last of Us",
        "The Rings of Power",
        "House of the Dragon",
        "The Wheel of Time",
        "Shadow and Bone",
        "Bling Empire",
        "Love is Blind",
        "The Circle",
        "Ultimatum",
        "Single's Inferno",
        "Love Island",
        "Too Hot to Handle",
        "Dating Around",
        "Love on the Spectrum",
        "Indian Matchmaking",
        "Love Virtually",
        "Love Never Lies",
        "Love, Death & Robots",
        "Aggretsuko",
        "Natsume's Book of Friends",
        "Demon Slayer",
        "Jujutsu Kaisen",
        "Chainsaw Man",
        "My Hero Academia",
        "Attack on Titan",
        "Tokyo Ghoul",
        "Death Note",
        "Code Geass",
        "The Promised Neverland",
        "Made in Abyss",
        "Ergo Proxy",
        "Texhnolyze",
        "Serial Experiments Lain",
        "Paranoia Agent",
        "Ghost in the Shell: SAC",
        "Cowboy Bebop",
        "Samurai Champloo",
        "Carole & Tuesday",
        "Erased",
        "Steins;Gate",
        "Psycho-Pass",
        "Darker than Black",
        "Monster",
        "Hellsing",
        "Hellsing Ultimate",
        "Trigun",
        "Rurouni Kenshin",
        "Inuyasha",
        "Fullmetal Alchemist",
        "Fullmetal Alchemist: Brotherhood",
        "Bleach",
        "Naruto",
        "Naruto Shippuden",
        "Boruto",
        "One Piece",
        "One Punch Man",
        "Mob Psycho 100",
        "The Disastrous Life of Saiki K.",
        "Assassination Classroom",
        "Food Wars",
        "High School DxD",
        "Is It Wrong to Try to Pick Up Girls in a Dungeon",
        "Re:Zero",
        "That Time I Got Reincarnated as a Spider",
        "The Rising of the Shield Hero",
        "Sword Art Online",
        "Log Horizon",
        "Overlord",
        "No Game No Life",
        "Konosuba",
        "How Not to Summon a Demon Lord",
        "In Another World With My Smartphone",
        "Sekirei",
        "Trinity Seven",
        "Infinite Stratos",
        "Freezing",
        "Gakusen Toshi Asterisk",
        "Chivalry of a Failed Knight",
        "The Master's Sun",
        "Tomorrow",
        "Descendants of the Sun",
        "Goblin",
        "Doom at Your Service",
        "Alchemy of Souls",
        "Black",
        "Tale of the Nine-Tailed",
        "My Name",
        "Hellbound",
        "Squid Game",
        "Strangers",
        "Extracurricular",
        "Itaewon Class",
        "Taxi Driver",
        "My Mister",
        "Something About 1%",
        "About Time",
        "When the Weather is Fine",
        "Crash Landing on You",
        "Mr. Sunshine",
        "Abyss",
        "Perfume",
        "Jealousy Incarnate",
        "Bring It On Ghost",
        "Oh My Ghost",
        "Please Come Back Mister",
        "The Legend",
        "The Time I've Loved You",
        "Ghost",
        "Go Back Couple",
        "My Shy Boss",
        "Because This is My First Life",
        "Clean with Passion for Now",
        "Search: WWW",
        "Encounter",
        "Her Private Life",
        "Start-Up",
        "Hospital Playlist",
        "Navillera",
        "Move to Heaven",
        "Hometown Cha-Cha-Cha",
        "Business Proposal",
        "Twenty Five Twenty One",
        "Our Blues",
        "Extraordinary Attorney Woo",
        "My Liberation Notes",
        "Something in the Rain",
        "One Spring Night",
        "Moment at Thirty",
        "Meow the Secret Boy",
        "Red Sleeve",
        "Mr. Queen",
        "River Where the Moon Rises",
        "100 Days My Prince",
        "Romance is a Bonus Book",
        "Hyena",
        "The Uncanny Counter",
        "Sweet Munchies",
        "Hot Stove League",
        "The Uncanny Counter",
        "Sweet Munchies",
        "My School 2021",
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
