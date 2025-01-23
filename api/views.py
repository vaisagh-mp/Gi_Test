import csv
from io import StringIO
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User

class UploadCSVView(APIView):
    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        if not file or not file.name.endswith('.csv'):
            return Response({"error": "Only .csv files are allowed."}, status=status.HTTP_400_BAD_REQUEST)

        file_data = file.read().decode('utf-8')
        csv_reader = csv.DictReader(StringIO(file_data))

        valid_records = 0
        invalid_records = 0
        errors = []

        for row in csv_reader:
            serializer = UserSerializer(data=row)
            if serializer.is_valid():
                try:
                    serializer.save()
                    valid_records += 1
                except Exception as e:
                    errors.append({"row": row, "error": str(e)})
                    invalid_records += 1
            else:
                errors.append({"row": row, "error": serializer.errors})
                invalid_records += 1

        return Response({
            "message": "File processed.",
            "total_valid_records": valid_records,
            "total_invalid_records": invalid_records,
            "errors": errors,
        }, status=status.HTTP_200_OK)
