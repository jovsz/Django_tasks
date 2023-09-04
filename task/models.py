from django.db import models

# Create your models here.
class Task(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField(blank=True)
  done = models.BooleanField(default=False)
  
  
  def des(self):
    return {"id": self.id ,"title": self.title, "description": self.description, "done": self.done}