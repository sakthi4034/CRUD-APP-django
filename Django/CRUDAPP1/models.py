from django.db import models


class product(models.Model):
    product_name=models.CharField(max_length=50,null=True)
    product_code=models.CharField(max_length=50,null=True)
    price=models.FloatField(default=0)
    gst=models.IntegerField(default=0)
    count=models.IntegerField(default=0)
    
    def __str__(self):
        return self.product_name + " " + self.product_code  
    