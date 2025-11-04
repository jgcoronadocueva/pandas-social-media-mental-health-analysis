# data_visualization.py

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_usage_vs_stress_by_age_group(df):
    """
    Plots the relationship between daily social media usage and stress level by age groups.

    Parameters
    ----------
    df : pandas.DataFrame
        The preprocessed dataset.
    """
    print("\nPlotting Daily Usage vs Stress Level by Age Groups...")

    # Set the style for this plot and the others until value is changed
    sns.set_theme(style="whitegrid")

    # Create the scatterplot
    plt.figure(figsize=(12, 6))
    sns.scatterplot(
        x='daily_screen_time',
        y='stress_level',
        hue='age_group',
        data=df,
        palette='pastel', #color theme
        s=60,  # size of each point in the plot
        edgecolor='black' # black border for each point
    )

    # Add title, labels and legend
    plt.title('Daily Social Media Usage vs Stress Level by Age Group')
    plt.xlabel('Daily Screen Time (hours)')
    plt.ylabel('Stress Level (1–10)')
    plt.legend(title='Age Group')
    
    # Adjusts the spacing between elements in the plot
    plt.tight_layout()
    
    # Saves and displays the plot
    plt.savefig("./graphs/Daily Usage vs Stress Level by Age Groups Correlation.png")
    plt.show()
    


def plot_platform_vs_stress_by_age_group(df):
    """
    Plots the average stress level for each age group across social media platforms.

    Parameters
    ----------
    df : pandas.DataFrame
        The preprocessed dataset.
    """
    print("\nPlotting Stress by Age Group and Social Media Platform...")

    # Gets average stress per age group and platform
    avg_stress = df.groupby(['age_group', 'social_media_platform'])['stress_level'].mean().reset_index()

    # Set the size and style of the plot
    plt.figure(figsize=(12, 6))
    sns.set_theme(style="whitegrid")

    # Create the barplot
    sns.barplot(
        x= 'age_group',
        y= 'stress_level',
        hue= 'social_media_platform',
        data= avg_stress,
        # Platforms are placed side by side, not stacked.
        dodge= True
    )

    # Add titles and labels
    plt.title('Average Stress Level by Age Group and Social Media Platform')
    plt.xlabel('Age Group')
    plt.ylabel('Average Stress (1–10)')

    # Move legend outside the plot
    plt.legend(
        title='Social Media Platform',
        bbox_to_anchor=(1.05, 1),
        loc='upper left',
        borderaxespad=0
    )

    # Adjusts the spacing between elements in the plot
    plt.tight_layout()

    # Saves and displays the plot
    plt.savefig("./graphs/Average Stress Level by Age Group and Social Media Platform.png")
    plt.show()
    

def plot_breaks_vs_health_metrics(df):
    """
    Plots the relationship between the amount break days and mental health metrics:
    stress, sleep quality, and happiness.

    Parameters
    ----------
    df : pandas.DataFrame
        The preprocessed dataset.
    """
    print("\nPlotting Mental Health Metrics by Break Days Groups...")

    metrics = ['stress_level', 'sleep_quality', 'happiness_index']
    titles = ['Stress', 'Sleep Quality', 'Happiness']

    # Creates three plots of the same figure
    fig, axes = plt.subplots(1, 3, figsize=(14,6))

    # Gets average for each metric per break days group
    for i, metric in enumerate(metrics):
        mid_metric = df.groupby('break_days_group')[metric].median().reset_index()
        
        sns.barplot(
            x='break_days_group', 
            y=metric, 
            data=mid_metric, 
            ax=axes[i])
        axes[i].set_title(titles[i])
        axes[i].set_xlabel('Break Days Group')
        axes[i].set_ylabel('Score (1–10)')
        axes[i].set_ylim(0, 10)
        # Show grid lines
        axes[i].grid(True)

    # Adjusts the spacing between elements in the plot
    plt.tight_layout()

    # Saves and displays the plot
    plt.savefig("./graphs/Mental Health Metrics by Break Days Groups.png")
    plt.show()