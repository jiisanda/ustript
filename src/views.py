import json
from collections import OrderedDict

import cv2
import numpy as np
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .utils import analyze_colors


class Home(APIView):
    """
    Home View
    """
    def get(self, request):
        return render(request, 'home.html')


class TestStrip(APIView):
    """
    Response to the uploaded image
    """
    def get(self, request):
        return render(request, 'test-form.html')

    def post(self, request):
        image = request.FILES.get('file')
        if image:
            img = cv2.imdecode(np.frombuffer(image.read(), np.uint8), cv2.IMREAD_COLOR)
            colors = analyze_colors(img)
            labels = ['URO', 'BIL', 'KET', 'BLD', 'PRO', 'NIT', 'LEU', 'GLU', 'SG', 'PH']
            label_data = OrderedDict()
            for indx, label in enumerate(labels):
                label_data[label] = colors[indx]

            # json_data = json.dumps(response_data, sort_keys=False)
            return Response(label_data, status=200)
        else:
            return Response(
                {
                    'error': 'No file provided'
                },
                status=400
            )
