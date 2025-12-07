AI-Driven Vehicle Behavior Analysis (YOLOv8)

Overview 

This repository contains a complete, four-stage Python pipeline developed for analyzing vehicle speed and movement from video footage. The system uses a specialized YOLOv8 implementation to generate clean, ML-ready time-series data for quantitative research.

This project was developed by Christos Perontsis under the supervision of Prof. Mohammad Shokrolah Shirazi at Marian University.

Key Outputs

Final Metric: Average speed and total tracking duration for every unique vehicle ID.

Data Structure: Clean, chronological time-series data suitable for advanced predictive models (LSTM/GRU).

🚀 Getting Started

Prerequisites

Environment Setup: Create a Python 3.10+ virtual environment and install dependencies (requirements.txt).

Model Weights: Ensure the YOLOv8 nano weights (yolov8n.pt) are downloaded and placed in the project root directory.

Execution Instructions (The 4-Step Pipeline)

The following scripts are located in the /Scripts/ directory and must be run sequentially.

Step

Script Name

Function

Output File

0. DATA COLLECTION

Object Detection Tracker.py

Runs YOLO, outputs raw data and video.

tracked_objects_data.csv

1. DATA PREPARATION

PrepareDataForML.py

Cleans & Sorts Data (Converts, sorts by ID/Frame).

ml_ready_tracking_data.csv

2. CALCULATION

speed_calculator.py

Per-Frame Speed (Calculates distance and speed/sec).

tracking_with_speed.csv

3. AGGREGATION

average_speed_analysis.py

Final Summary (Calculates the average speed per car ID).

car_average_speed_summary.csv

📊 Optional Data Formatting (Visualization)

The following utility script is optional and designed purely for visualization purposes. It converts the clean, vertical data into specialized horizontal formats.

Utility 1: Pivot Trajectories for Visualization

This script creates a unique horizontal file (horizontal_trajectories.csv) where each row is a single car ID followed by its entire chronological X, Y coordinate path. This is useful for plotting all car paths onto a single graph.

python Scripts/Transform_Updated.py


Output: horizontal_trajectories.csv (One row per car ID, showing all X, Y coordinates).
