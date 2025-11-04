# main.py

from data_handler import load_kaggle_dataset, save_cleaned_data
from data_preprocessor import preprocess_dataset
from data_analysis import (
    analyze_usage_vs_stress_by_age_group,
    analyze_platform_vs_stress_by_age_group,
    analyze_breaks_vs_health_metrics
)
from data_visualization import (
    plot_usage_vs_stress_by_age_group,
    plot_platform_vs_stress_by_age_group,
    plot_breaks_vs_health_metrics
)

def main():
    print("SOCIAL MEDIA AND MENTAL HEALTH ANALYSIS\n")

    # Step 1: Load dataset
    dataframe = load_kaggle_dataset(
        "ayeshaimran123/social-media-and-mental-health-balance",
        "Mental_Health_and_Social_Media_Balance_Dataset.csv"
    )

    # Step 2: Clean and preprocess dataset
    dataframe = preprocess_dataset(dataframe)

    # Step 3: Perform analysis
    analyze_usage_vs_stress_by_age_group(dataframe)
    analyze_platform_vs_stress_by_age_group(dataframe)
    analyze_breaks_vs_health_metrics(dataframe)

    # Step 4: Generate visualizations
    plot_usage_vs_stress_by_age_group(dataframe)
    plot_platform_vs_stress_by_age_group(dataframe)
    plot_breaks_vs_health_metrics(dataframe)

    # Step 5: Save the cleaned dataset for later use
    save_cleaned_data(dataframe)

    print("\nAnalysis complete. All results has been displayed.")

if __name__ == "__main__":
    main()
