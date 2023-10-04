"""
This module is responsible for visualising the data using Matplotlib.
"""

"""
Task 22 - 24: Write suitable functions to visualise the data as follows:

- Display a pie chart showing the total number of positive and negative reviews for a specified hotel.
- Display the number of reviews per the nationality of a reviewer. This should by ordered by the number of reviews, highest first, and should show the top 15 + “Other” nationalities.
- Display a suitable animated visualisation to show how the number of positive reviews, negative reviews and the average rating change over time.

Each function should visualise the data using Matplotlib.
"""


import matplotlib.pyplot as plt
import pandas as pd
import ast
from matplotlib.animation import FuncAnimation
from datetime import datetime, timedelta
import tui
from process import reviews_for_hotel

def positive_negative_pie_chart(reviews_data,hotel_name):
    """
    Task 22: Create a pie chart to visualize the distribution of positive and negative reviews.

    :param reviews_data: List of reviews data
    :return: None
    """
    positive_count = 0
    negative_count = 0
    reviews_data =  reviews_for_hotel(reviews_data,hotel_name)
    for review in reviews_data:
            if float(review[5]) >= 5:
                positive_count += 1
            else:
                negative_count += 1

    # Create a pie chart
    labels = 'Positive', 'Negative'
    sizes = [positive_count, negative_count]
    colors = ['green', 'red']
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Display the pie chart
    plt.title("Distribution of Positive and Negative Reviews")
    plt.show()

def reviews_per_nationality_chart(reviews_data):
    """
    Create an animated bar chart to visualize the number of reviews per nationality.

    :param reviews_data: List of reviews data
    :return: None
    """
    # Initialize an empty dictionary to store nationality counts
    nationality_counts = {}
    progress = 0
    total_len = len(reviews_data)
    tui.progress("Reviews per Nationality",f"{progress/total_len*100:.2f}%")
    for row in reviews_data:
        # update progress based on the number of reviews processed in percentage
        tui.progress("Reviews per Nationality",f"{progress/total_len*100:.2f}%")

        # Extract the nationality row
        nationality = row[4]
        
        # Update the nationality counts
        if nationality in nationality_counts:
            nationality_counts[nationality] += 1
        else:
            nationality_counts[nationality] = 1
    
    tui.progress("Reviews per Nationality",f"{progress/total_len*100:.2f}%")

    # Sort the nationality counts by the number of reviews (descending)
    sorted_nationalities = sorted(nationality_counts.items(), key=lambda x: x[1], reverse=True)

    # Select the top 15 nationalities and combine the rest as 'Other'
    top_15_nationalities = sorted_nationalities[:15]
    other_count = sum(count for _, count in sorted_nationalities[15:])
    top_15_nationalities.append(('Other', other_count))

    # Unzip the list of tuples into two separate lists for plotting
    nationalities, review_counts = zip(*top_15_nationalities)

    # Create a figure and axis for the bar chart
    fig, ax = plt.subplots(figsize=(20, 8))
    
    # Function to update the animation
    def animate(frame):
        # Clear the previous bars and labels
        ax.clear()
        ax.bar(nationalities, review_counts)
        ax.set_xlabel('Nationality')
        ax.set_ylabel('Number of Reviews')
        ax.set_title('Number of Reviews per Nationality (Top 15 + Other)')
        ax.set_xticks(range(len(nationalities)))
        ax.set_xticklabels(nationalities, rotation=45)
    
    # Create the animation to very slowly update the bar chart
    anim = FuncAnimation(fig, animate, interval=100, frames=1)
    
    # Display the animation
    plt.show()

        
def reviews_summary(reviews_data):
    dates = []
    review_scores = []
    positive_reviews = []
    negative_reviews = []


    for data in reviews_data:
        review_date = datetime.strptime(data[0], '%m/%d/%Y')  # Adjust the date format here
        dates.append(review_date)
        
        reviewer_score = float(data[5])
        review_scores.append(reviewer_score)
        
        if reviewer_score >= 5:
            positive_reviews.append(1)
            negative_reviews.append(0)
        else:
            positive_reviews.append(0)
            negative_reviews.append(1)

    # Group the data by date and calculate the average Reviewer_Score, positive, and negative reviews
    average_review_scores = []
    positive_review_counts = []
    negative_review_counts = []

    unique_dates = list(set(dates))
    unique_dates.sort()

    for date in unique_dates:
        total_score = 0
        pos_count = 0
        neg_count = 0

        for i in range(len(dates)):
            if dates[i] == date:
                total_score += review_scores[i]
                pos_count += positive_reviews[i]
                neg_count += negative_reviews[i]

        avg_score = total_score / (pos_count + neg_count)

        average_review_scores.append(avg_score)
        positive_review_counts.append(pos_count)
        negative_review_counts.append(neg_count)

    # Create the plot
    plt.figure(figsize=(15, 8))
    plt.plot(unique_dates, average_review_scores, label='Average Review Score')
    plt.plot(unique_dates, positive_review_counts, label='Positive Reviews')
    plt.plot(unique_dates, negative_review_counts, label='Negative Reviews')
    plt.xlabel('Date')
    plt.ylabel('Count / Score')
    plt.title('Average Review Score and Review Counts by Date')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()



def animated_summary(reviews_data):
    """
    Task 24: Create an animated summary of reviews.

    :param reviews_data: List of reviews data
    :return: None
    """
    dates = []
    review_scores = []
    positive_reviews = []
    negative_reviews = []


    for data in reviews_data:
        review_date = datetime.strptime(data[0], '%m/%d/%Y')  # Adjust the date format here
        dates.append(review_date)
        
        reviewer_score = float(data[5])
        review_scores.append(reviewer_score)
        
        if reviewer_score >= 5:
            positive_reviews.append(1)
            negative_reviews.append(0)
        else:
            positive_reviews.append(0)
            negative_reviews.append(1)

    # Create a list of unique months
    unique_months = list(set((date.year, date.month) for date in dates))
    unique_months.sort()

    # Initialize lists to store monthly data
    monthly_dates = []
    monthly_avg_review_scores = []
    monthly_positive_review_counts = []
    monthly_negative_review_counts = []

    # Extract data for each month
    for year, month in unique_months:
        month_start = datetime(year, month, 1)
        month_end = datetime(year, month, 1) + timedelta(days=32)
        
        monthly_dates.append(month_start)
        
        total_score = 0
        pos_count = 0
        neg_count = 0
        
        for i in range(len(dates)):
            if month_start <= dates[i] < month_end:
                total_score += review_scores[i]
                pos_count += positive_reviews[i]
                neg_count += negative_reviews[i]
        
        avg_score = total_score / (pos_count + neg_count)
        
        monthly_avg_review_scores.append(avg_score)
        monthly_positive_review_counts.append(pos_count)
        monthly_negative_review_counts.append(neg_count)

    # Create the initial plot
    fig, ax = plt.subplots(figsize=(15, 8))
    line1, = ax.plot([], [], label='Average Review Score')
    line2, = ax.plot([], [], label='Positive Reviews')
    line3, = ax.plot([], [], label='Negative Reviews')
    ax.set_xlabel('Date')
    ax.set_ylabel('Count / Score')
    ax.set_title('Average Review Score and Review Counts by Month')
    ax.legend()
    ax.grid(True)
    ax.set_xticks([md for md in monthly_dates])
    ax.set_xticklabels([md.strftime('%b %Y') for md in monthly_dates], rotation=45)
    plt.tight_layout()

    # Animation function
    def animate(frame):
        line1.set_data(monthly_dates[:frame], monthly_avg_review_scores[:frame])
        line2.set_data(monthly_dates[:frame], monthly_positive_review_counts[:frame])
        line3.set_data(monthly_dates[:frame], monthly_negative_review_counts[:frame])
        return line1, line2, line3

    # Create the animation
    ani = FuncAnimation(fig, animate, frames=len(monthly_dates), repeat=False, blit=True)
    plt.show()

