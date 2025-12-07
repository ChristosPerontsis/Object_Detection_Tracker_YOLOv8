import csv
from collections import defaultdict
import operator

def prepare_data_for_ml(input_filepath, output_filepath):
    """
    Reads the vertical tracking data (Frame, ID, X, Y), and prepares it
    for Machine Learning by ensuring consistent sorting (by ID, then by Frame).
    """
    try:
        with open(input_filepath, 'r', newline='') as infile:
            reader = csv.reader(infile)
            # Read all rows, skipping the header
            data = list(reader)[1:]

        if not data:
            print("The input CSV file is empty. No data to process.")
            return

        # 1. Convert Frame, ID, X, Y to appropriate types for sorting
        processed_data = []
        for row in data:
            try:
                processed_data.append((
                    int(row[0]),  # Frame
                    int(row[1]),  # ID
                    int(row[2]),  # Center_X
                    int(row[3])   # Center_Y
                ))
            except ValueError:
                print(f"Skipping malformed row: {row}")
                continue

        # 2. Sort the data: Group by ID (index 1), then sort by Frame (index 0)
        processed_data.sort(key=operator.itemgetter(1, 0))


        # 3. Write the ML-ready data to a new CSV file
        with open(output_filepath, 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(["Frame", "ID", "Center_X", "Center_Y"])
            writer.writerows(processed_data)

        print(f"ML-ready data successfully saved to {output_filepath}")

    except FileNotFoundError:
        # NOTE: This error now indicates the YOLO script was NOT run correctly first.
        print(f"Error: The file at '{input_filepath}' was not found. Please run the YOLO script first.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # CORRECTED PATH: The input file is in the main Python YOLO folder.
    input_csv_file = '/Users/christosperontsis/Desktop/Python YOLO/Scripts/tracked_objects_data.csv'
    
    # OUTPUT PATH: Saving the result to the Scripts folder
    output_csv_file = '/Users/christosperontsis/Desktop/Python YOLO/Scripts/ml_ready_tracking_data.csv'

    prepare_data_for_ml(input_csv_file, output_csv_file)
