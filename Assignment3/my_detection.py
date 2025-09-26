import jetson.inference
import jetson.utils

INPUT_FILE = "/home/nvidia/Desktop/Capstone2025/Assignment3/image2.jpg"
OUTPUT_FILE = "/home/nvidia/Desktop/Capstone2025/Assignment3/output2.jpg"
# -------------------------
net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)

input_img = jetson.utils.videoSource(INPUT_FILE)

output_img = jetson.utils.videoOutput(OUTPUT_FILE)

img = input_img.Capture()

detections = net.Detect(img)

print("==============================================")
for detection in detections:
    print(detection)
    print("----------------------------------------------")

output_img.Render(img)

print(f"Detection finished.")
