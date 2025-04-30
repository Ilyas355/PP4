from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
import requests


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default="https://res.cloudinary.com/hgn0zzxyf/image/upload/v1/media/default.jpg",
        upload_to='profile_pics'
    )

    def __str__(self):
        return f"{self.user.username} profile"

    # save method if the image is too big, Pillow for resizing


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Only process the image if it exists
        if self.image:
            try:
                # Download the image from the cloud storage
                response = requests.get(self.image.url, stream=True)
                response.raise_for_status()  # Raise an error for bad responses (e.g., 404)

                # Open the image
                img = Image.open(BytesIO(response.content))

                # Resize the image if it's too large
                if img.height > 300 or img.width > 300:
                    output_size = (300, 300)
                    img.thumbnail(output_size)

                    # Save the resized image back to the field
                    buffer = BytesIO()
                    img.save(buffer, format=img.format)
                    buffer.seek(0)
                    self.image.save(self.image.name, ContentFile(buffer.read()), save=False)
            except Exception as e:
                print(f"Error processing image: {e}")
