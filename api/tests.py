from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import User


class UploadCSVViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_upload_valid_csv(self):
        csv_content = b"name,email,age\nJohn Doe,john@example.com,30\nJane Doe,jane@example.com,25"
        csv_file = SimpleUploadedFile("test.csv", csv_content, content_type="text/csv")
        response = self.client.post('/api/upload-csv/', {'file': csv_file}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 2)

    def test_upload_invalid_csv(self):
        csv_content = b"name,email,age\nInvalid,rgre,150\n"
        csv_file = SimpleUploadedFile("test.csv", csv_content, content_type="text/csv")
        response = self.client.post('/api/upload-csv/', {'file': csv_file}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 0)
        self.assertIn('errors', response.data)
