import fastf1
from fastf1 import plotting

# Enable caching
fastf1.Cache.enable_cache('data/fastf1_cache')  # adjust path as needed

class DataFetcher:
    def __init__(self, year: int, gp_name: str):
        self.year = year
        self.gp_name = gp_name
        self.session = None

    def load_session(self, session_type: str):
        """
        Load a session from FastF1.
        """
        try:
            self.session = fastf1.get_session(self.year, self.gp_name, session_type)
            self.session.load()
            print(f"{session_type} session loaded for {self.gp_name} {self.year} ✅")
        except Exception as e:
            print(f"Error loading session: {e}")


if __name__ == "__main__":
    fetcher = DataFetcher(2025, "Azerbaijan Grand Prix")
    fetcher.load_session("Qualifying")
