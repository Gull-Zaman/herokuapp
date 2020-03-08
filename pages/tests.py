from django.test import SimpleTestCase

class SimpleTests(SimpleTestCase):
    def check_home_page_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def check_about_page_status(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

