import cv2
from ultralytics import YOLO
import csv

model = YOLO("yolov8n.pt")

video_path = "/Users/christosperontsis/Desktop/Python YOLO/pictures and videos/CarsMoving.mp4"
cap = cv2.VideoCapture(video_path)

# Get properties of the input video
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Define the codec and create a VideoWriter object
output_video_path = 'tracked_car_video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4 files
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

# Create the list for the tracking data
all_tracked_objects = []
frame_counter = 0

# Loop through the video frames
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_counter += 1

    # Class 2 means track only cars
    results = model.track(frame, persist=True, conf=0.60, verbose=False, classes=[2])

    # Process the results from the current frame
    if results[0].boxes.id is not None:
        # Loop through each detected and tracked object in the frame
        for box in results[0].boxes:
            track_id = int(box.id.item())
            x_center = int(box.xywh[0][0].item())
            y_center = int(box.xywh[0][1].item())

            # Store the object's information, including the frame number
            object_info = (frame_counter, track_id, x_center, y_center)
            all_tracked_objects.append(object_info)

    annotated_frame = results[0].plot()

    # Write the annotated frame to the output video
    out.write(annotated_frame)

    cv2.imshow("YOLO Tracking", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Cleanup
cap.release()
out.release()
cv2.destroyAllWindows()

# Write the data to the CSV file
output_file = 'tracked_objects_data.csv'

with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Frame", "ID", "Center_X", "Center_Y"])
    writer.writerows(all_tracked_objects)

print(f"\nData successfully exported to {output_file}")
print(f"Annotated video successfully exported to {output_video_path}")