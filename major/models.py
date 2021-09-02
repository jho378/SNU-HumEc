from django.db import models
from django.conf import settings


class MajorPost(models.Model):
    major = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # accounts.models.User 연결
    pin = models.BooleanField(default=False)

    title = models.CharField(max_length=100)
    contents = models.TextField()
    image = models.ImageField(blank=True, upload_to="major/image")  # settings.py MEDIA_ROOT 이하
    file = models.FileField(blank=True, upload_to="major/file")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hits = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.pk}: {self.title}"

    @property
    def click(self):  # 조회수
        self.hits += 1
        self.save()
