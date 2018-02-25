from django.test import TestCase
from .models import Location,Gallery

# Create your tests here.

class GalleryTestClass(TestCase):
    def setUp(self):
        self.photos=Gallery(image='image',image_name='name',description='describe')
#Testign instance
    def test_instance(self):
        self.assertTrue(isinstance(self.photos,Gallery))

#Testing save Method
def test_save_method(self):
    self.photos.save_images()
    gallery = Gallery.objects.all()
    self.assertTrue(len( gallery)> 0)






