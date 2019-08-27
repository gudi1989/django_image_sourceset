import os

import webp
from PIL import Image
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create Webp in Static'

    def handle(self, *args, **options):
        for relative_root, dirs, files in os.walk(os.path.join(settings.STATIC_ROOT, 'images')):
            for file_ in files:
                if '.png' in file_ or '.jpg' in file_ or '.gif' in file_:
                    try:
                        file_path = os.path.join(relative_root, file_)
                        file_webp_path = file_path.rsplit('.', 1)[0] + ".webp"
                        print(file_path)
                        webp.save_image(Image.open(file_path), file_webp_path, quality=80)
                    except:
                        pass
