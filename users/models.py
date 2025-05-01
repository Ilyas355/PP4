from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
import requests


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default="../default_u4dioc.jpg",
        upload_to='profile_pics'
    )

    def __str__(self):
        return f"{self.user.username} profile"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.image or 'default.jpg' in str(self.image):
            return

        try:
            response = requests.get(self.image.url, stream=True)
            response.raise_for_status()

            img = Image.open(BytesIO(response.content))

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)

                buffer = BytesIO()
                img.save(buffer, format=img.format)
                buffer.seek(0)
                self.image.save(self.image.name, ContentFile(buffer.read()), save=False)
                super().save(*args, **kwargs)

        except Exception as e:
            print(f"[Image Resize Error] {e}")