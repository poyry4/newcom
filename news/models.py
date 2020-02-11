from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class CatNews(models.Model):
    category = models.CharField( max_length=50)

    def __str__(self):
        return self.category
 
# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(null=False)
    date = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    cat = models.ForeignKey(CatNews, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'
