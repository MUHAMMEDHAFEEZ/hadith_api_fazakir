# hadiths/views.py

import os
import json
import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class RandomBukhariHadithView(APIView):
    def get(self, request):
        bukhari_folder = 'bukhari'
        files = os.listdir(bukhari_folder)
        json_files = [file for file in files if file.endswith('.json')]

        if not json_files:
            return Response({'error': 'No JSON files found in the directory'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        selected_file = random.choice(json_files)
        file_path = os.path.join(bukhari_folder, selected_file)

        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        hadiths = data.get('hadiths', [])
        if not hadiths:
            return Response({'error': 'No hadiths found in the selected file'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        random_hadith = random.choice(hadiths)
        metadata = data.get('metadata', {})
        hadith_text = random_hadith.get('text', '')
        reference = random_hadith.get('reference', {})

        response_data = {
            "metadata": metadata,
            "hadith": {
                "text": hadith_text,
                "reference": reference
            }
        }

        return Response(response_data, status=status.HTTP_200_OK)
