# data_handler.py

import pandas as pd
import kagglehub
from kagglehub import KaggleDatasetAdapter

def load_kaggle_dataset(kaggle_dataset, file_path):
    """
    Loads a Kaggle dataset and returns it as a Pandas DataFrame.

    Parameters
    ----------
    kaggle_dataset : str
        The name of the Kaggle dataset to load.
    path : str
        Path to the specific file in the Kaggle dataset.

    
    Returns
    -------
    pandas.DataFrame
        The dataset loaded into a Pandas DataFrame.
    """

    print(f"Loading '{file_path}' from the dataset '{kaggle_dataset}'...")
    
    # Loads the latest version of the dataset
    df = kagglehub.load_dataset(
        KaggleDatasetAdapter.PANDAS,
        kaggle_dataset,
        file_path
    )

    print(f"'{file_path}' successfully loaded.")

    return df

def save_cleaned_data(df, path="./data/social_media_and_mental_health_balance.csv"):
    """
    Saves a pandas DataFrame to a CSV file.

    Parameters
    ----------
    df : pandas.DataFrame
        The dataset to save.
    path : str, optional
        File path where the CSV will be saved. Default is './data/social_media_and_mental_health_balance.csv'.
    """
    # Saves the DataFrame without the row index to a CSV file
    df.to_csv(path, index=False)

    # Informs the user that the file has been saved and show the path
    print(f"Cleaned dataset saved at {path}")