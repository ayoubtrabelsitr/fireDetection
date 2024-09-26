from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt


model = YOLO('ComputerVision/best.pt')


results = model.predict(source=0, imgsz=640, conf=0.75, show=True)
