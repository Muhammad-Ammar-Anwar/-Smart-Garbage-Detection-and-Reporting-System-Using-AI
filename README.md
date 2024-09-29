# Smart Garbage Detection and Reporting System Using AI

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
- Inference

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Muhammad-Ammar-Anwar/-Smart-Garbage-Detection-and-Reporting-System-Using-AI.git
   cd Garbage-Detection-System

## Install the required dependencies:
pip install opencv-python smtplib supervision
Set up your API key and email credentials in the code:

## Setting up Environment Variables
1. Create a `.env` file in your project directory.
2. Add the following variables to the `.env` file:
   api_key = "Your Roboflow API Key" sender_email = "your-email@example.com" receiver_email = "receiver-email@example.com" password = "your-email-password"

3. Make sure to replace the placeholder values with your actual credentials and API key.
4. The `.env` file should not be committed to version control to keep your credentials secure. Make sure to add `.env` to your `.gitignore` file.

## How to Use
Make sure your camera is connected or use a video file as input.

## Run the following command to start the detection:
python main.py
The system will display the video feed and capture images when both trash and a person are detected. After 8 images are captured, an email will be sent with the images attached.
