from django.db import models

# Create your models here.
class 임시사전(models.Model):
    단어 = models.CharField(max_length=20)
    품사 = models.CharField(max_length=10, null=True, blank=True)
    품사2 = models.CharField(max_length=10, null=True, blank=True)
    국적 = models.CharField(max_length=10, null=True, blank=True)
    Tag = models.CharField(max_length=10, null=True, blank=True)
    출처 = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.단어