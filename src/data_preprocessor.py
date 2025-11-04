# data_cleaner.py

import pandas as pd

def preprocess_dataset(df):
    """
    Preprocess the dataset by:
    * Dropping columns that don't have analytical value
    * Renaming columns to make them easier to use in the code
    * Converting data types if needed
    * Adding group columns
    * Showing a short summary of the data

    Parameters
    ----------
    df : pandas.DataFrame
        The dataset to be preprocessed.    
    
    Returns
    -------
    pandas.DataFrame
        The preprocessed dataset.
    """
    
    print("\nCleaning dataset...")

    # Drop 'User_ID' as it doesn't provide analytical value
    df = df.drop(columns=["User_ID"])

    # Rename the columns to have shorter names and use lowercase with underscores
    df = df.rename(columns={
        "Age": "age",
        "Gender": "gender",
        "Daily_Screen_Time(hrs)": "daily_screen_time",
        "Sleep_Quality(1-10)": "sleep_quality",
        "Stress_Level(1-10)": "stress_level",
        "Days_Without_Social_Media": "days_without_social_media",
        "Exercise_Frequency(week)": "exercise_frequency",
        "Social_Media_Platform": "social_media_platform",
        "Happiness_Index(1-10)": "happiness_index"
    })

    # Ensure the numeric columns are read as actual numbers
    numeric_columns = [
        "age",
        "daily_screen_time",
        "sleep_quality",
        "stress_level",
        "days_without_social_media",
        "exercise_frequency",
        "happiness_index"
    ]

    for col in numeric_columns:
        # Convert to numeric type
        df[col] = pd.to_numeric(df[col])

    
    # Creates bins and labels for each age group
    bins = [0, 17, 25, 35, 45, 50]
    labels = ['<18', '18-25', '26-35', '36-45', '46-50']
        
    # Create a new column for age groups
    df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, right=True)

    # Define break days bins and labels
    bins = [0, 1, 4, 9]
    labels = ['No break', '1-4', '4+']

    # Create a new column for break days groups
    df['break_days_group'] = pd.cut(df['days_without_social_media'], bins=bins, labels=labels, right=True)

    print("Dataset cleaned and ready for analysis.")

    # Show a dataset summary
    print("\nShowing first 5 rows of the cleaned dataset:")
    print(f"\n{df.head()}")
    rows, cols = df.shape
    print(f"\nDataset: {rows} rows, {cols} columns\n")

    return df