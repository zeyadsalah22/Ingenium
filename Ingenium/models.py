from django.db import models

class high(models.Model):
    order = models.IntegerField()
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    info = models.TextField()

    def __str__(self):
        return f"{self.name} is the {self.position}"


class images(models.Model):
    order = models.IntegerField()
    image = models.CharField(max_length=64)
    category = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.category} image: {self.image}"

class questions(models.Model):
    order = models.IntegerField()
    question = models.TextField()
    answer = models.TextField()
    category = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.category} question no.: {self.order}"