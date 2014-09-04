from django.db import models


# Create your models here.
class TestObj(models.Model):
    name = models.CharField(max_length=64)


class Group(models.Model):
    name = models.CharField(max_length=64)

    @property
    def progress(self):
        aggregate = self.documents.all().aggregate(models.Avg('price'))
        return aggregate['progress__avg']


class File(models.Model):
    path = models.CharField(max_length=64, unique=True)


class Document(models.Model):
    number = models.CharField(max_length=16)
    name = models.CharField(max_length=64)
    description = models.TextField()
    progress = models.PositiveSmallIntegerField(default=0)
    group = models.ForeignKey(Group, related_name='documents')
    files = models.ManyToManyField(File)
