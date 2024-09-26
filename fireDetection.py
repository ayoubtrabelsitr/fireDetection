from ultralytics import YOLO
import os
import matplotlib.pyplot as plt


model = YOLO('ComputerVision/best.pt')


results = model.predict(source='ComputerVision/fire2.mp4', imgsz=640, conf=0.75, save=True)
#results = model.predict(source=0, imgsz=640, conf=0.75, show=True)