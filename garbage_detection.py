import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from inference import InferencePipeline
from inference.core.interfaces.camera.entities import VideoFrame
import cv2
import os
import uuid
import supervision as sv

def send_email(sender_email, receiver_email, subject, body, password, attachment_paths):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    for attachment_path in attachment_paths:
        with open(attachment_path, "rb") as attachment:
            part = MIMEApplication(attachment.read(), Name=os.path.basename(attachment_path))
            part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_path)}"'
            message.attach(part)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)

        server.sendmail(sender_email, receiver_email, message.as_string())

    print("Email sent successfully!")

save_dir = "detected_images"
os.makedirs(save_dir, exist_ok=True)

image_count = 0
attachment_paths = []

def capture_and_save_image(image):
    global image_count, attachment_paths

    filename = str(uuid.uuid4()) + ".jpg"
    filepath = os.path.join(save_dir, filename)
    cv2.imwrite(filepath, image)
    print("Image saved:", filepath)

    image_count += 1
    attachment_paths.append(filepath)

    if image_count == 8:
        send_email(sender_email, receiver_email, subject, body, password, attachment_paths)
        image_count = 0
        attachment_paths = []

def my_custom_sink(predictions: dict, video_frame: VideoFrame):
    conf_threshold = 0.3

    print("threshold=> ", conf_threshold)

    filtered_predictions = [p for p in predictions["predictions"] if p["confidence"] >= conf_threshold]

    labels = [p["class"] for p in filtered_predictions]

    if "trash" in labels:
        if "person" in labels:
            print("Trash and person both detected! Capturing and saving image...")
            capture_and_save_image(video_frame.image)
        else:
            print("Trash detected, but no person found.")

    detections = sv.Detections.from_inference(predictions)
    image = annotator.annotate(
        scene=video_frame.image.copy(), detections=detections, labels=labels
    )
    cv2.imshow("Predictions", image)
    cv2.waitKey(1)

annotator = sv.BoxAnnotator()
pipeline = InferencePipeline.init(
    model_id="garbage-detection-ogn92/2",
    video_reference=1, 
    on_prediction=my_custom_sink,
    api_key="Your Api Key"
)

sender_email = "Sender Mail"
receiver_email = "Reciever Mail"
subject = "Detected Images"
body = "Detected images are attached."
password = "Password"


pipeline.start()
pipeline.join()

