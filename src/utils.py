import numpy as np
import cv2
from collections import OrderedDict
import json

image_path = '/test-image/image5.jpg'
img = cv2.imread(image_path)


def analyze_colors(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    color_regions = [
        (0, 0, 10, 100),
        (10, 0, 20, 100),
        (20, 0, 30, 100),
        (30, 0, 40, 100),
        (40, 0, 50, 100),
        (50, 0, 60, 100),
        (60, 0, 70, 100),
        (70, 0, 80, 100),
        (80, 0, 90, 100),
        (90, 0, 100, 100)
    ]

    colors = []

    for region in color_regions:
        x, y, w, h = region
        color_region = image[y:y+h, x:x+w]
        mean_color = np.mean(color_region, axis=(0, 1))
        rgb = [int(channel) for channel in mean_color]
        colors.append(rgb)
    return colors


analyze_colors = analyze_colors(img)
color_names = ['URO', 'BIL', 'KET', 'BLD', 'PRO', 'NIT', 'LEU', 'GLU', 'SG', 'PH']
color_data = OrderedDict()
for index, name in enumerate(color_names):
    color_data[name] = analyze_colors[index]


json_data = json.dumps(color_data, sort_keys=False)
print(json_data)
