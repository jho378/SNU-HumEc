from django.db import models
from django.conf import settings


class Notice(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pin = models.BooleanField(default=False)

    title = models.CharField(max_length=100)
    contents = models.TextField()
    image = models.ImageField(blank=True, upload_to="notice/image")  # settings.py MEDIA_ROOT 이하
    file = models.FileField(blank=True, upload_to="notice/file")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hits = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.pk}: {self.title}"

    @property
    def click(self):  # 조회수
        self.hits += 1
        self.save()
