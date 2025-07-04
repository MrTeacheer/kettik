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
    def save(self, name, content, save=True, quality=75):
        # Считываем содержимое (если еще не считано)
        content.seek(0)
        original_bytes = content.read()

        # Сжимаем изображение
        compressed_bytes = compress_image(io.BytesIO(original_bytes), quality)

        # Создаем Django ContentFile
        compressed_file = ContentFile(compressed_bytes, name=name)

        # Вызываем оригинальный save из базового класса
        super().save(name, compressed_file, save=save)


class CompressedImageField(ImageField):
    attr_class = CompressedImageFieldFile
    