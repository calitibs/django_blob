from django.db import models

# Create your models here.

class BlongModel(models.Model):
    title=models.CharField(max_length=100,blank=True,verbose_name='辩题')
    content=models.TextField()


    def __str__(self):
        return 'id=%s,title=%s,content=%s'%(self.id,self.title,self.content)