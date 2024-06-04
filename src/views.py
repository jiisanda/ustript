import json
from collections import OrderedDict

import cv2
import numpy as np
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .utils import analyze_colors


class TestStrip(APIView):
    """
    Response to the uploaded image
    """
    def get(self, request):
        return render(request, 'test-form.html')

    def post(self, request):
        print(request.FILES)
        image = request.FILES.get('file')
        print(image)
        if image:
            img = cv2.imdecode(np.frombuffer(image.read(), np.uint8), cv2.IMREAD_COLOR)
            colors = analyze_colors(img)
            labels = ['URO', 'BIL', 'KET', 'BLD', 'PRO', 'NIT', 'LEU', 'GLU', 'SG', 'PH']
            label_data = OrderedDict()
            for indx, label in enumerate(labels):
                label_data[label] = colors[indx]

            response_data = {
                'success': 'File uploaded successfully...',
                'body': label_data
            }

            json_data = json.dumps(response_data, sort_keys=False)
            return Response(json_data, status=200)
        else:
            return Response(
                {
                    'error': 'No file provided'
                },
                status=400
            )
