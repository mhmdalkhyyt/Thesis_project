from ultralytics import YOLO


model = YOLO('/home/a20muhal/Thesis_project/training/runs/detect/yolov8_tva_trad_v14/weights/best.pt')

#model = YOLO('yolov8n_custom.yaml')

results = model.train(
    data='/home/a20muhal/Thesis_project/training/till_exjobbare/datasets/annoterat/ds_multi/images/train.yaml',
    #    data='./Tva_trad/data.yaml',
    imgsz=640,
    epochs=100,
    batch=10,
    name='yolov8_tva_trad_combi',
    
)

