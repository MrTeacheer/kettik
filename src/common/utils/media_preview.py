from django.utils.html import format_html


class MediaPreview:

    @classmethod
    def video_preview(cls, obj):
        if obj.video:
            return format_html(
                '<video width="200" height="200" controls>'
                '<source src="{}" type="video/mp4">'
                "Your browser does not support the video tag."
                "</video>",
                obj.video.url,
            )
        return "No video"

    @classmethod
    def image_preview(cls, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-width:200px; max-height:200px"/>'.format(
                    obj.image.url
                )
            )
        return "No photo"

    @classmethod
    def map_preview(self, obj):
        if obj.map:
            return format_html(
                '<iframe width="400" height="300" src="{}" frameborder="0" style="border:0" allowfullscreen></iframe>',
                obj.map,
            )
        return "No map"
