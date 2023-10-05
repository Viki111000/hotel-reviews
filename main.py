"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done using the appropriate functions in the module 'tui'
        any processing should be done using the appropriate functions in the module 'process'
        any visualisation should be done using the appropriate functions in the module 'visual'
"""

# Task 11: Import required modules and create an empty list named 'reviews_data'.
# This will be used to store the data read from the source data file.

# Importing required modules
import os
import tui
import process
import visual

# Creating an empty list to store reviews data
reviews_data = []

def run():
    # Task 12: Call the function welcome of the module 'tui'.
    # This will display our welcome message when the program is executed.
    # Displaying a welcome message to the user
    tui.welcome()

    # Task 13: Load the data.
    # - Use the appropriate function in the module 'tui' to display a message to indicate that the data loading
    # operation has started.
    # - Load the data. Each line in the file should represent a review in the list 'reviews_data'.
    # You should appropriately handle the case where the file cannot be found or loaded.
    # - Use the appropriate functions in the module 'tui' to display a message to indicate how many reviews have
    # been loaded and that the data loading operation has completed.
    

    # Load data from the CSV file in the data folder
    data_file_path = "./data/hotel_reviews.csv"

    # Check if the file exists before attempting to open it
    if os.path.exists(data_file_path):
        with open(data_file_path, 'r') as file:
            # Skip the header row if it exists
            header = next(file, None)

            # Read the remaining rows and store them in the reviews_data list
            for line in file:
                row = line.strip().split(',')
                reviews_data.append(row)
    else:
        print(f"File not found: {data_file_path}")

    while True:
        # Task 14: Using the appropriate function in the module 'tui', display the main menu
        # Assign the value returned from calling the function to a suitable local variable
        # Displaying the main menu and getting the user's choice
        user_choice = tui.main_menu()

        # Task 15: Check if the user selected the option for processing data.  If so, then do the following:
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has started.
        # - Process the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has completed.
        #
        # To process the data, do the following:
        # - Use the appropriate function in the module 'tui' to display a sub-menu of options for processing the data
        # (menu variant 1).
        # - Check what option has been selected
        #
        #   - If the user selected the option to retrieve reviews by hotel name then
        #       - Use the appropriate function in the module 'tui' to indicate that the review retrieval process
        #       has started.
        #       - Use the appropriate function in the module 'process' to retrieve the review and then appropriately
        #       display it.
        #       - Use the appropriate function in the module 'tui' to indicate that the review retrieval process has
        #       completed.
        #
        #   - If the user selected the option to retrieve reviews by review dates then
        #       - Use the appropriate function in the module 'tui' to indicate that the reviews retrieval
        #       process has started.
        #       - Use the appropriate function in the module 'process' to retrieve the reviews
        #       - Use the appropriate function in the module 'tui' to display the retrieved reviews.
        #       - Use the appropriate function in the module 'tui' to indicate that the reviews retrieval
        #       process has completed.
        #
        #   - If the user selected the option to group reviews by nationality then
        #       - Use the appropriate function in the module 'tui' to indicate that the grouping
        #       process has started.
        #       - Use the appropriate function in the module 'process' to group the reviews
        #       - Use the appropriate function in the module 'tui' to display the groupings.
        #       - If required, you may add a suitable function to the module 'tui' to display the groupings
        #       - Use the appropriate function in the module 'tui' to indicate that the grouping
        #       process has completed.
        #
        #   - If the user selected the option to summarise the reviews then
        #       - Use the appropriate function in the module 'tui' to indicate that the summary
        #       process has started.
        #       - Use the appropriate function in the module 'process' to summarise the reviews.
        #       - Add a suitable function to the module 'tui' to display the summary
        #       - Use your function in the module 'tui' to display the summary
        #       - Use the appropriate function in the module 'tui' to indicate that the summary
        #       process has completed.
        if user_choice == 1:
            # Displaying the data processing sub-menu and getting the user's choice
            processing_choice = tui.sub_menu(variant=1)

            # Check what processing option has been selected
            if processing_choice == 1:
                # Task 16: Retrieve and display a review by hotel name
                hotel_name = tui.hotel_name()
                hotel_reviews=process.reviews_for_hotel(reviews_data, hotel_name)
                tui.display_reviews(hotel_reviews)
            elif processing_choice == 2:
                # Task 17: Retrieve and display reviews by review dates
                date_list = tui.review_dates()
                hotel_reviews=process.reviews_for_dates(reviews_data, date_list)
                tui.display_reviews(hotel_reviews)
            elif processing_choice == 3:
                # Task 18: Group and display reviews by nationality
                hotel_reviews=process.reviews_by_nationality(reviews_data)
                tui.display_reviews(hotel_reviews)
            elif processing_choice == 4:
                # Task 19: Summarize and display reviews
                hotel_reviews_summary=process.reviews_summary(reviews_data)
                # Print the summary in the specified format
                for date, data in sorted(hotel_reviews_summary.items()):
                    print(f"Date: {date} | Negative Reviews: {data['negative']} | Positive Reviews: {data['positive']} | "
                            f"Total Rating: {data['total_rating']} | Average Rating: {data['average_rating']:.2f}")

            else:
                # Handle invalid processing choice
                tui.error("Invalid processing option. Please select a valid option.")

        # Task 21: Check if the user selected the option for visualizing data.
        # If so, then do the following:
        # - Use the appropriate function in the module 'tui' to indicate that the data visualization operation
        # has started.
        # - Visualize the data by doing the following:
        #   - call the appropriate function in the module 'tui' to determine what visualization is to be done.
        #   - call the appropriate function in the module 'visual' to display the visual
        # - Use the appropriate function in the module 'tui' to display a message to indicate that the
        # data visualization operation has completed.
        if user_choice == 2:
            # Displaying the data visualization sub-menu and getting the user's choice
            visualization_choice = tui.sub_menu(variant=2)

            if visualization_choice == 1:
                # Task 22: Create a pie chart to visualize the distribution of positive and negative reviews
                # Ask the user to enter the hotel name
                hotel_name = tui.hotel_name()
                visual.positive_negative_pie_chart(reviews_data, hotel_name)
            elif visualization_choice == 2:
                # Task 23: Create a bar chart to visualize the number of reviews per nationality
                visual.reviews_per_nationality_chart(reviews_data)
            elif visualization_choice == 3:
                # Task 24: Create an animated summary of reviews
                visual.reviews_summary(reviews_data)
            else:
                # Handle invalid visualization choice
                tui.error("Invalid visualization option. Please select a valid option.")

        # Task 25: Check if the user selected the option for exporting reviews.  If so, then do the following:
        # - Use the appropriate function in the module 'tui' to retrieve what reviews are to be exported.
        # - Check what option has been selected
        #
        # - Use the appropriate function in the module 'tui' to indicate that the export operation has started.
        # - Export the reviews (see below)
        # - Use the appropriate function in the module 'tui' to indicate that the export operation has completed.
        #
        # To export the reviews, you should demonstrate the application of OOP principles including the concepts of
        # abstraction and inheritance.  You should create suitable classes with appropriate methods.
        # You should use these to write the reviews (either all or only those for a specific country/region) to a JSON file.
        if user_choice == 3:
            # Task 25: Export Reviews
            export_option = tui.sub_menu(variant=3)

            if export_option == 1:
                # Task 25a: Export all reviews to a JSON file
                filename = tui.file_name()
                # if the file name does not end with .json, then append it
                if not filename.endswith(".json"):
                    filename += ".json"
                process.export_reviews_to_json(reviews_data, filename)
                tui.display_message(f"Reviews exported to {filename}.")
            elif export_option == 2:
                # Task 25b: Export reviews for a specific nationality to a JSON file
                hotel_name = tui.hotel_name()
                filename = tui.file_name()
                # if the file name does not end with .json, then append it
                if not filename.endswith(".json"):
                    filename += ".json"
                process.export_reviews_by_hotel_to_json(reviews_data, hotel_name, filename)
                tui.display_message(f"Reviews for {hotel_name} exported to {filename}.")
            elif export_option == 3:
                # Task 26: Check if the user selected the option for exiting the program.
                # If so, then break out of the loop
                tui.display_message("Exiting the program.")
                break
            else:
                # Handle invalid export option
                tui.error("Invalid export option. Please select a valid option.")

        # Task 27: If the user selected an invalid option then use the appropriate function of the
        # module tui to display an error message
        if user_choice not in [1, 2, 3, 4]:
            tui.error("Invalid choice. Please select a number between 1 and 4.")
            continue  # Continue the loop to allow the user to try again

if __name__ == "__main__":
    run()
