"""
This module is responsible for processing the data.  Each function in this module will take a list of reviews,
process it and return the desired result.
"""

"""
Task 16 - 20: Write suitable functions to process the data.

Each of the functions below should follow the pattern:
- Take a list of reviews (where each review is a list of data values) as a parameter.
- Process the list of reviews appropriately.  You may use the module 'tui' to retrieve any additional information 
required from the user to complete the processing.
- Return a suitable result

The required functions are as follows:
- Retrieve the total number of reviews that have been loaded.
- Retrieve the reviews for a hotel where the hotel name is specified by the user.
- Retrieve the reviews for the dates specified by the user.
- Retrieve all the reviews grouped by the reviewer’s nationality.
- Retrieve a summary of all the reviews. This should include the following information for each date in ascending order:
    - the total number of negative reviews on that date
    - the total number of positive reviews on that date
    - the average rating on that date
"""
import tui
import json


def total_reviews(reviews):
    """
    Task 16: Retrieve the total number of reviews that have been loaded.
    """
    return len(reviews)

def reviews_for_hotel(reviews, hotel_name):
    """
    Task 17: Retrieve the reviews for a hotel where the hotel name is specified by the user.
    """
    progress = 0
    total_len = total_reviews(reviews)

    return_value = []
    tui.progress("Reviews for Hotel",f"{progress/total_len*100:.2f}%")
    for review in reviews:

        # update progress based on the number of reviews processed in percentage
        # (value/total value)×100%
        tui.progress("Reviews for Hotel",f"{progress/total_len*100:.2f}%")
        progress += 1

        if review[1] == hotel_name:
            return_value.append(review)
    tui.progress("Reviews for Hotel", f"100.00%")
    return return_value

def reviews_for_dates(reviews, dates):
    """
    Task 18: Retrieve the reviews for the dates specified by the user.
    """
    progress = 0
    total_len = total_reviews(reviews)
    return_value = []
    tui.progress("Reviews for Dates",f"{progress/total_len*100:.2f}%")
    for review in reviews:
        # update progress based on the number of reviews processed in percentage
        # (value/total value)×100%
        tui.progress("Reviews for Dates",f"{progress/total_len*100:.2f}%")
        progress += 1

        if review[0] in dates:
            return_value.append(review)
    tui.progress("Reviews for Dates", f"100.00%")
    return return_value

def reviews_by_nationality(reviews):
    """
    Task 19: Retrieve all the reviews grouped by the reviewer’s nationality.
    """
    grouped_reviews = {}
    progress = 0
    total_len = total_reviews(reviews)
    tui.progress("Reviews for Nationality",f"{progress/total_len*100:.2f}%")
    for review in reviews:
        # update progress based on the number of reviews processed in percentage
        tui.progress("Reviews for Nationality",f"{progress/total_len*100:.2f}%")

        nationality = review[2]
        if nationality not in grouped_reviews:
            grouped_reviews[nationality] = []
        grouped_reviews[nationality].append(review)
        progress += 1
    tui.progress("Reviews for Nationality",f"{progress/total_len*100:.2f}%")
    return grouped_reviews

def reviews_summary(reviews):
    """
    Task 20: Retrieve a summary of all the reviews.
    """
    summary = {}
    progress = 0
    total_len = total_reviews(reviews)
    tui.progress("Reviews Summary",f"{progress/total_len*100:.2f}%")
    for review in reviews:

        # update progress based on the number of reviews processed in percentage
        tui.progress("Reviews Summary",f"{progress/total_len*100:.2f}%")
        date = review[0]
        rating = float(review[5])  # Convert the rating to a float
        if date not in summary:
            summary[date] = {'negative': 0, 'positive': 0, 'total_rating': 0.0, 'count': 0}
        
        if rating <= 5:
            summary[date]['negative'] += 1
        else:
            summary[date]['positive'] += 1
        summary[date]['total_rating'] += rating
        summary[date]['count'] += 1
        progress += 1

    for date, data in summary.items():
        data['average_rating'] = data['total_rating'] / data['count']
    
    tui.progress("Reviews Summary",f"{progress/total_len*100:.2f}%")

    return summary



def export_reviews_to_json(reviews, filename):
    """
    Task 25a: Export all reviews to a JSON file.

    This function exports all reviews to a JSON file specified by the user.

    :param reviews: List of reviews data
    :param filename: Name of the JSON file to export to
    """
    try:
        with open(filename, 'w') as json_file:
            # Write the reviews data to the JSON file
            json.dump(reviews, json_file, indent=4)
        print(f"Reviews exported to {filename}.")
    except Exception as e:
        print(f"Error exporting reviews: {str(e)}")

def export_reviews_by_hotel_to_json(reviews, hotelname, filename):
    """
    Task 25b: Export reviews for a specific hotelname to a JSON file.

    This function exports reviews for a specific hotelname to a JSON file specified by the user.

    :param reviews: List of reviews data
    :param hotelname: hotelname for filtering reviews
    :param filename: Name of the JSON file to export to
    """
    filtered_reviews = reviews_for_hotel(reviews, hotelname)

    try:
        with open(filename, 'w') as json_file:
            # Write the filtered reviews data to the JSON file
            json.dump(filtered_reviews, json_file, indent=4)
        print(f"Reviews for {hotelname} exported to {filename}.")
    except Exception as e:
        print(f"Error exporting reviews: {str(e)}")
