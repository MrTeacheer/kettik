import io
from django.core.files.base import ContentFile
from django.db.models import ImageField, FileField
from PIL import Image


def compress_image(image_stream: io.BytesIO, quality: int = 75) -> bytes:
    with Image.open(image_stream) as img:
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        compressed_image_stream = io.BytesIO()
        img.save(
            compressed_image_stream,
            format="JPEG",
            quality=quality,
            optimize=True
        )

    return compressed_image_stream.getvalue()


class CompressedImageFieldFile(ImageField.attr_class):
    def save(self, name, content, save=True, quality=60):
        content.seek(0)
        original_bytes = content.read()

        compressed_bytes = compress_image(io.BytesIO(original_bytes), quality)

        compressed_file = ContentFile(compressed_bytes, name=name)

        super().save(name, compressed_file, save=save)


class CompressedImageField(ImageField):
    attr_class = CompressedImageFieldFile
