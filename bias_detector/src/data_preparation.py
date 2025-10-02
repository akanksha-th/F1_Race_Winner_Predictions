import os
import pandas as pd


class DataPreparation:
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.data = None

    def load_data(self) -> pd.DataFrame:
        # Keep your downloaded dataset in the /.data/ folder
        if not os.path.exists(self.data_path):
            raise FileNotFoundError("No data file found at the location.")
        self.data = pd.read_csv(self.data_path)
        return self.data
        
    def data_preprocessing(self) -> pd.DataFrame:
        self.data.columns = [col.lower().replace(" ", "_") for col in self.data.columns]
        pass


if __name__ == "__main__":
    data_path = "C:/Users/aktkr/healthcare-projects/bias_detector/.data/allergenchipchallenge-data-corrected-final-hdh-sfa.csv"
    loader = DataPreparation(data_path)
    pass