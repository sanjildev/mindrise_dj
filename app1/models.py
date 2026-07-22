from django.db import models

# Create your models here.

class Todolist(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    status=models.BooleanField(default=False)
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
