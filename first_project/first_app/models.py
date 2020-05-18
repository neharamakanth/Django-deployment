from django.db import models

# Create your models here.
class Topic(models.Model):
    name=models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.name

class WebPage(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,unique=True)
    url=models.URLField(unique=True)

    def __str__(self):
        return self.name

class AcessRecord(models.Model):
      name=models.ForeignKey(WebPage,on_delete=models.CASCADE)
      date=models.DateField()

      def __str__(self):
          return str(self.date)
