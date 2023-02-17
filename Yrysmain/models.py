from django.db import models

class Player(models.Model):
    COLOR_CHOICES = [
        ('shatura','Шатура'),
        ('ormatek','Орматек'),
    ]
    username = models.CharField(max_length=100)
    score = models.IntegerField()
    color = models.CharField(max_length=7, choices=COLOR_CHOICES, blank=True, null=False)

    def __str__(self):
        return self.username

