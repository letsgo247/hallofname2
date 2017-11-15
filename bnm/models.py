from django.db import models

# Create your models here.

class 사전(models.Model):
    단어 = models.CharField(max_length=20)
    품사 = models.CharField(max_length=10, null=True, blank=True)
    품사2 = models.CharField(max_length=10, null=True, blank=True)
    국적 = models.CharField(max_length=10, null=True, blank=True)
    Tag = models.CharField(max_length=10, null=True, blank=True)
    출처 = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.단어


class Algorithm(models.Model):
    이름 = models.CharField(max_length=20)
    설명 = models.TextField()
    내용 = models.TextField(null=True, blank=True)
    Votes = models.IntegerField(default=100)