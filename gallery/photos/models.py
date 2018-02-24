from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=30)

  def __str__(self):
      return self.name

  def save_category(self):
      self.save()

class Location(models.Model):
    place = models.CharField(max_length=30)

    def __str__(self):
        return self.place

class Meta:
    ordering = ['place']

    def save_location(self):
        self.save()
    

    @classmethod
    def search_by_category(cls, search_category):
        category = cls.objects.filter(category__icontains=search_category)
        return category

class Gallery(models.Model):
  image = models.ImageField(upload_to='gallery/', null=True, blank=True)
  image_name = models.CharField(max_length=25)
  description = models.TextField(max_length=100)
  location = models.ForeignKey(Location)
  category = models.ForeignKey(Category)

  def __str__(self):
      return self.image_name

  @classmethod
  def my_images(cls):
      images = cls.objects.all()
      return images

  def delete_images(self):
      self.remove()    

  def save_images(self):
      self.save()

  def search_image(category):
      pass 

  def filter_by_location(location):
      pass       

  def update_image(self, id):
      pass

  def get_image_by_id(id):
      pass

 

  