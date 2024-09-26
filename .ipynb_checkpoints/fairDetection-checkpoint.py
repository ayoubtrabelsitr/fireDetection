from ultralytics import YOLO




model = YOLO('ComputerVision/best.pt')


results = model.predict(source=0, imgsz=640, conf=0.72, show=True)

