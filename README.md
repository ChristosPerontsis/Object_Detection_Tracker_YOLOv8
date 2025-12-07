AI-Driven Vehicle Behavior Analysis (YOLOv8)

Overview

This repository contains a complete, four-stage Python pipeline developed for analyzing vehicle speed and movement from video footage. The system uses a specialized YOLOv8 implementation to generate clean, ML-ready time-series data for quantitative research.

This project was developed by Christos Perontsis (CP) under the supervision of Prof. Mohammad Shokrolah Shirazi at Marian University.

Key Outputs

Final Metric: Average speed and total tracking duration for every unique vehicle ID.

Validation: Clean, chronological time-series data suitable for advanced predictive models (LSTM/GRU).

🚀 Getting Started

Prerequisites

Clone the Repository:

git clone [Your Repository URL Here]
cd [Your Repository Name]


Setup Environment: Create a Python 3.10+ virtual environment and install dependencies.

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


Model Weights: Ensure the YOLOv8 nano weights (yolov8n.pt) are downloaded and placed in the project root directory.

Execution Instructions (The 4-Step Pipeline)

The following scripts must be run sequentially from the root of the project directory.

Step 0: Data Collection & Raw Output

Runs the YOLOv8 tracker on the input video, generates the annotated video, and outputs the raw, unsorted data.

python Scripts/Object\ Detection\ Tracker.py


Output: tracked_objects_data.csv (Raw data)

Step 1: Data Cleaning & Sorting (ML Preparation)

This is the critical preprocessing step that converts data to numbers and sorts all vehicle observations chronologically (by ID then by Frame) for time-series analysis.

python Scripts/PrepareDataForML.py


Output: ml_ready_tracking_data.csv (Clean & Sorted)

Step 2: Per-Frame Speed Calculation

Calculates the pixel distance and instantaneous speed (pixels per second) for every single frame-to-frame movement in the video (using the 25 FPS rate).

python Scripts/speed_calculator.py


Output: tracking_with_speed.csv (Data with per-frame speed metrics)

Step 3: Final Metric Aggregation (The Research Result)

Calculates the final statistical summary: the average speed and total duration for each unique car ID.

python Scripts/average_speed_analysis.py


Final Output: car_average_speed_summary.csv (The conclusive report table)