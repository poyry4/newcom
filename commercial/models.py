from django.db import models

class categorys(models.Model):
    categoryName = models.CharField(max_length=40)

    def __str__(self):
        return self.categoryName

class imageCommercial(models.Model):
     imges = models.ImageField(default='default.png', blank=True)

class commercial(models.Model):
    price = models.IntegerField(null=False)
    description = models.CharField(max_length=25)
    productName = models.TextField(null=True)
    img = models.ForeignKey(imageCommercial, on_delete=models.CASCADE, default=None)
    cat = models.ForeignKey(categorys, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.productName    

     

