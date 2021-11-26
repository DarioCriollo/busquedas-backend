from django.db import models

class Inquiries(models.Model):
    word = models.CharField(max_length=300)
    number_searches = models.IntegerField()
    number_results = models.IntegerField()

    def __str__(self):
        return self.word

