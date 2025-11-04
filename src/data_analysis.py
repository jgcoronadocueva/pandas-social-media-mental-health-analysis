# data_analysis.py

import pandas as pd

def analyze_usage_vs_stress_by_age_group(df):
    """
    Question 1: Is there a relationship between the number of daily hours spent on 
    social media and stress levels based on the user's age?

    Calculate and prints average daily usage, average stress, and correlation between usage 
    and stress for each age group.

    Parameters
    ----------
    df : pandas.DataFrame
        The preprocessed dataset.
    """
    print("\n--- Daily Social Media Usage vs Stress by Age Groups ---")

    # List of columns needed for this analysis
    usage_col = 'daily_screen_time'
    stress_col = 'stress_level'
    age_group_col = 'age_group'

    
    # Group by each age group and iterates over each
    for age_group, subset in df.groupby(age_group_col):
        avg_usage = round(subset[usage_col].mean(), 2)
        avg_stress = round(subset[stress_col].mean(),2)
        # Measures the correlation between the daily usage and the stress
        correlation = subset[usage_col].corr(subset[stress_col])
        print(f"\nAge group: {age_group}")
        print(f"  Average daily usage: {avg_usage} hours")
        print(f"  Average stress level: {avg_stress}")
        print(f"  Correlation between usage and stress: {round(correlation,2)}")


def analyze_platform_vs_stress_by_age_group(df):
    """
    Question 2: Does the choice of social media platform influence stress level 
    differently across age groups?

    Calculates and prints the average stress for each social media platform within each age group.

    Parameters
    ----------
    df : pandas.DataFrame
        The preprocessed dataset.
    """
    print("\n--- Stress Level by Age Group and Social Media Platform ---")

    # Define relevant column names
    platform_col = 'social_media_platform'
    stress_col = 'stress_level'
    age_group_col = 'age_group'

    # Group by age group first
    for age_group, subset in df.groupby(age_group_col):
        print(f"\nAge Group: {age_group}")
        # Within each age group, group by social media platform
        platform_avg = round(subset.groupby(platform_col)[stress_col].mean(), 2)
        for platform, stress in platform_avg.items():
            print(f"  {platform}: Average stress = {stress}")


def analyze_breaks_vs_health_metrics(df):
    """
    Question 3: How does the amount of social media break days relate 
    to users' overall mental health and well-being?

    Calculates and prints average stress, sleep quality, and happiness for each break days group.

    Parameters
    ----------
    df : pandas.DataFrame
        The preprocessed dataset.
    """
    print("\n--- Mental Health Metrics by Break Days Groups ---")

    # List of columns needed for this analysis
    stress_col = 'stress_level'
    sleep_col = 'sleep_quality'
    happiness_col = 'happiness_index'
    break_days_col = 'break_days_group'

    # Group by break days group and iterates over each
    for break_days_group, subset in df.groupby(break_days_col):
        mid_stress = subset[stress_col].median()
        mid_sleep = subset[sleep_col].median()
        mid_happiness = subset[happiness_col].median()

        print(f"\nBreak days group: {break_days_group}")
        print(f"  Median stress: {mid_stress}")
        print(f"  Median sleep quality: {mid_sleep}")
        print(f"  Median happiness: {mid_happiness}")