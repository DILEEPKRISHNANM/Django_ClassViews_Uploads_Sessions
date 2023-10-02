from django.db import models

# Create your models here.


class UserImage(models.Model):
    user_image = models.FileField(upload_to="images")


# To Work with images u need to set ImageField in th model and install some packages
# python3 -m pip install pillow
