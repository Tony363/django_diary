from django.db import models

# Create your models here.
class Question(models.Model):
    ID = models.IntegerField(primary_key=True)
    Date = models.DateField(auto_now_add=True)
    Question = models.CharField(blank=True,null=True)

    def __str__(self):
        return self.Question