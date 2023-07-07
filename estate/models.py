from django.db import models

class PropertyModel(models.Model):
    name = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    image = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey('PropertyCategory', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class PropertyCategory(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Property categories'

class Email(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
