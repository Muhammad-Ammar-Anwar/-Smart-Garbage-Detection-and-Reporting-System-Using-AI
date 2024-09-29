# Garbage Detection System

This project utilizes a machine learning model trained on Roboflow to detect and capture images of individuals throwing garbage on the ground. It identifies both the person and trash in real-time, saving images locally. After collecting 8 images, it automatically sends an email with the captured images for review. The system integrates OpenCV for image processing and SMTP for email notifications.

## Features
- Real-time detection of a person and trash using a Roboflow-trained model.
- Captures and saves images locally when both a person and trash are detected.
- Automatically sends an email with attached images after collecting 8 instances.
- Uses OpenCV for image capture and annotation, and SMTP for email notifications.

## Requirements
- Python 3.x
- OpenCV
- Supervision (sv)
- Roboflow Inference API
- SMTP for email notifications

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/YourUsername/Garbage-Detection-System.git
   cd Garbage-Detection-System
Install the required dependencies:

bash
pip install opencv-python smtplib supervision
Set up your API key and email credentials in the code:

python
api_key = "Your Roboflow API Key"
sender_email = "your-email@example.com"
receiver_email = "receiver-email@example.com"
password = "your-email-password"

How to Use
Make sure your camera is connected or use a video file as input.

Run the following command to start the detection:

bash
python main.py
The system will display the video feed and capture images when both trash and a person are detected. After 8 images are captured, an email will be sent with the images attached.
