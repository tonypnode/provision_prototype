from django.test import TestCase

# Create your tests here.
class HTMLPageTest(TestCase):
    """
    Validates templates and redirects

    """
    def check_html(self, url, correct_template, correct_status_code):
        response = self.client.get(url)
        self.assertTemplateUsed(response, correct_template)
        self.assertEqual(str(response.status_code), correct_status_code)

    def test_home_page_returns_correct_template(self):
        """
        Test proper template for home page

        """
        self.check_html('/', 'home.html', '200')
