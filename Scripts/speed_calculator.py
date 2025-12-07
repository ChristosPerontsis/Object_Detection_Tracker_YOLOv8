import csv
import math
from collections import defaultdict

# Define the Frame Rate (FPS) of the video
# We use 25.0 FPS, based on the calculation of 1173 frames / 47 seconds.
FPS = 25.0
# Time interval between frames in seconds (1 / FPS)
TIME_INTERVAL = 1.0 / FPS


def calculate_pixel_speed(input_filepath, output_filepath):
    """
    Reads sorted tracking data, calculates distance and pixel speed (px/s)
    between consecutive frames for each unique object ID.
    """
    try:
        with open(input_filepath, 'r', newline='') as infile:
            reader = csv.reader(infile)
            header = next(reader)  # Read and store the header row
            data_rows = list(reader)

        if not data_rows:
            print("The input file is empty. Cannot calculate speed.")
            return

        # Dictionary to store the last known position for each ID
        last_position = defaultdict(lambda: {'frame': 0, 'x': 0, 'y': 0})

        # List to hold the output rows with speed data
        output_data = []

        # New header will include the speed columns
        output_header = header + ["Pixel_Distance", "Pixel_Speed_PS"]

        # Iterate through the data, ensuring objects are processed by ID and Frame
        for row in data_rows:
            try:
                frame_num = int(row[0])
                track_id = int(row[1])
                x = int(row[2])
                y = int(row[3])
            except ValueError:
                print(f"Skipping row due to malformed data: {row}")
                continue

            # Get the previous position for this specific ID
            prev = last_position[track_id]

            # --- Calculation ---

            # Distance only calculated if this is the next consecutive frame for this ID
            if prev['frame'] != 0 and (frame_num == prev['frame'] + 1):
                # Euclidean distance formula: sqrt((x2-x1)^2 + (y2-y1)^2)
                # [Image of Euclidean distance formula]
                dist_pixels = math.sqrt(
                    (x - prev['x']) ** 2 + (y - prev['y']) ** 2
                )

                # Speed = Distance / Time_Interval (in pixels/second)
                speed_ps = dist_pixels / TIME_INTERVAL

                # Append the results to the current row (formatted to 2 decimal places)
                output_data.append(row + [f"{dist_pixels:.2f}", f"{speed_ps:.2f}"])
            else:
                # If this is the first frame for this ID, or a dropped frame,
                # we cannot calculate speed, so use placeholder values.
                output_data.append(row + ["", ""])

            # --- Update the last known position for this ID ---
            last_position[track_id] = {'frame': frame_num, 'x': x, 'y': y}

        # Write the final result to the output file
        with open(output_filepath, 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(output_header)
            writer.writerows(output_data)

        print(f"\n✅ Speed data calculated and saved to {output_filepath}")

    except FileNotFoundError:
        print(f"\n❌ Error: Input file not found. Ensure '{input_filepath}' exists and is correct.")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Input file is the CLEANED and SORTED data from prepare_data_for_ml.py
    input_csv_file = '/Users/christosperontsis/Desktop/Python YOLO/Scripts/ml_ready_tracking_data.csv'

    # Output file will contain the speed data
    output_csv_file = '/Users/christosperontsis/Desktop/Python YOLO/Scripts/tracking_with_speed.csv'

    calculate_pixel_speed(input_csv_file, output_csv_file)