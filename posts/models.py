from django.db import models
from datetime import datetime

# Create your models here.
class Posts(models.Model):
  title = models.CharField(max_length=200)
  body = models.TextField()
  author = models.CharField(max_length=200)
  created_at = models.DateTimeField(default=datetime.now, blank=True)

  def __str__(self):
    return self.title

  class Meta:
    verbose_name_plural = "Posts"

class Comments(models.Model):
  post = models.ForeignKey(Posts, on_delete=models.CASCADE)
  text = models.TextField()
  pub_date = models.DateTimeField(default = datetime.now, blank=True)

  def __str__(self):
    return self.text

  class Meta:
    verbose_name_plural = "Comments"