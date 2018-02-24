from django.test import TestCase
from .models import Location,Gallery

# Create your tests here.

class GalleryTestClass(TestCase):
    def setUp(self):
        self.photos=Gallery(image='image',image_name='name',description='describe')
#Testign instance
    def test_instance(self):
        self.assertTrue(isinstance(self.photos,Gallery))






