from transformers import DetrImageProcessor, DetrForObjectDetection
import torch
from PIL import Image
import requests


def prediction(url):
    image = Image.open(requests.get(url, stream=True).raw)

    processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50", revision="no_timm")
    model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50", revision="no_timm")

    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)

    target_sizes = torch.tensor([image.size[::-1]])
    results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.9)[0]

    detection_results = []

    for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
        box = [round(i, 2) for i in box.tolist()]

        # Формирование строки с результатом
        result_str = (
            f"Detected {model.config.id2label[label.item()]} with confidence "
            f"{round(score.item(), 3)} at location {box}"
        )

        # Добавление строки в список результатов
        detection_results.append(result_str)

    # Возвращение результатов в виде кортежа
    return detection_results

