# myproject/custom_storages.py

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from whitenoise.storage import CompressedManifestStaticFilesStorage


class MediaStorage(FileSystemStorage):
    location = settings.MEDIA_ROOT
    base_url = settings.MEDIA_URL


class StaticStorage(CompressedManifestStaticFilesStorage):
    location = settings.STATIC_ROOT
    base_url = settings.STATIC_URL
