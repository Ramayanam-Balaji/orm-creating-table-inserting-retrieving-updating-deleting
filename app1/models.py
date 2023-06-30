from django.db import models

# Create your models here.
class Topic(models.Model):
    Topic_Name=models.CharField(max_length=100,primary_key=True)
    def __str__(self) -> str:
        return self.Topic_Name
class Webpage(models.Model):
    Topic_Name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    url=models.URLField()
    def __str__(self) -> str:
        return self.Name
class AccessRecord(models.Model):
    Name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.author