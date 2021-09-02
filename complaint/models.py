from django.db import models
from django.conf import settings


class Complaint(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    contents = models.TextField()
    image = models.ImageField(blank=True, upload_to="complaint/image")
    file = models.FileField(blank=True, upload_to="complaint/file")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hits = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.pk}: {self.title}"

    @property
    def click(self):  # 조회수
        self.hits += 1
        self.save()


class ComplaintComment(models.Model):
    post = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pk}: {self.contents}"
