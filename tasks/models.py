from django.db import models

# Create your models here.
class Status(models.TextChoices):
  UNSTARTED = 'u' , "Not Started Yet"
  ONGOING = 'o' , " Ongoing"
  FINISHED  = 'f', "Finished"

class Task(models.Model):
  name  = models.CharField(verbose_name="Task name", max_length=65 , unique=True)
  status = models.CharField(verbose_name="Task status", max_length=1,choices=Status.choices) 
  
  def __str__(self) -> str:
    return self.name
 

 