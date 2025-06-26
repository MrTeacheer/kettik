import io
from django.core.files.base import ContentFile
from django.db.models import ImageField
from PIL import Image


async def compress_image(image_stream: io.BytesIO, quality: int) -> bytes:
    with Image.open(image_stream) as img:
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        compressed_image_stream = io.BytesIO()

        img.save(compressed_image_stream, format="JPEG", quality=quality, optimize=True)

    return compressed_image_stream.getvalue()


class CompressedImageFieldFile(ImageField.attr_class):
    async def compress_and_save(self, name, content, save=True, quality=75):
        image_bytes = await compress_image(io.BytesIO(content.read()), quality)
        compressed_file = ContentFile(image_bytes, name=name)
        self.save(name, compressed_file, save=save)


class CompressedImageField(ImageField):
    attr_class = CompressedImageFieldFile
