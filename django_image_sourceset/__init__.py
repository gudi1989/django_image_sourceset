# -*- coding: utf-8 -*-
import webp
from PIL import Image
from django.dispatch import receiver

try:
    from easy_thumbnails.signals import thumbnail_created

    @receiver(thumbnail_created)
    def thumbnail_created_callback(sender, **kwargs):
        try:
            file_path = sender.path
            file_webp_path = file_path.rsplit('.', 1)[0] + ".webp"
            webp.save_image(Image.open(file_path), file_webp_path, quality=80)
        except:
            pass
except ImportError:
    pass
