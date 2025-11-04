# Overview

I created this project to strengthen my data analysis skills while learning how to perform data preprocessing, analysis, and visualization using Python libraries, particularly Pandas. The program focuses on understanding how social media habits influence mental health. Through this project, I intend to identify meaningful patterns and create attractive visualizations that effectively tell the story behind the data.

The dataset used for this analysis contains information about individuals’ social media habits, including daily hours of use, platform preferences, demographics, and self-reported mental health metrics. It can be obtained from Kaggle: [Social Media and Mental Health Balance](https://www.kaggle.com/datasets/ayeshaimran123/social-media-and-mental-health-balance)

The software allows users to to analyze the following:

* The relationship between social media daily usage time and stress level based on user's age.
* The relationship between social media platform choice and stress level based on user's age.
* The influence of break days of social media in mental health metrics such as: happiness, stress, and sleep quality.


YouTube tutorial: [Data Analysis with Pandas](https://youtu.be/lEWP3q9PaNU)

# Data Analysis Results

1) Is there a relationship between the number of daily hours spent on social media and stress levels based on the user's age?

There is a clear positive correlation between daily social media usage and reported stress levels.This trend is most evident in users under 25, indicating that higher screen time is more strongly associated to greater stress within younger age groups.

2) Does the choice of social media platform influence stress level differently across age groups?

Yes, social media affects stress differently by age. For users under 25, Instagram causes the most stress and X the least, with other platforms at moderate levels. Ages 26–35 experience higher stress from TikTok, Facebook, and Instagram, while LinkedIn remains low and X rises. For users 36–45, differences between platforms are smaller, though LinkedIn and YouTube show slightly higher stress. Among those 46 and older, Facebook causes the most stress. Overall, users under 25 and over 45 are most affected by platform choice.


3) How does the amount of social media break days relate to users' overall mental health and well-being?

While stress and sleep quality remain largely similar across groups, happiness tends to increase as users take more frequent breaks, particularly more than 4 days. This suggests that taking regular breaks from social media may boost overall happiness.

# Development Environment

The software was developed in Visual Studio Code using Python 3.14.

Libraries used:
 
* pandas – for data preprocessing, aggregation, and analysis
* matplotlib – for creating visual graphs
* kagglehub – for downloading datasets directly from Kaggle
* seaborn - for statistical data visualization and improved aesthetics

To install libraries used, you can run the command: `pip install -r requirements.txt` 

# Useful Websites

* [W3Schools – Matplotlib Pyplot](https://www.w3schools.com/python/matplotlib_pyplot.asp)
* [Kaggle - Matplotlib Tutorial for Beginners](https://www.kaggle.com/code/prashant111/matplotlib-tutorial-for-beginners)
* [Analyst Builder – Pandas for Data Analysis](https://www.analystbuilder.com/courses/pandas-for-data-analysis)
* [Pandas - 10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
* [GeeksforGeeks – Pandas.cut() Method in Python](https://www.geeksforgeeks.org/python/pandas-cut-method-in-python/)
* [Visualizing Data in Python With Seaborn](https://realpython.com/python-seaborn/)


# Future Work

* Add an interactive menu with advanced options for users to choose variables for analysis.
* Integrate machine learning models to predict stress or anxiety based on social media habits.
* Automatically detect and handle missing or invalid data during analysis.