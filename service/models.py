from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField('内容')
    image = models.ImageField(upload_to='service')
    created_t = models.DateTimeField(auto_now_add=True)
    modified_t = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    # Below is partial code of /Users/llg/Documents/python/lights-g.com/lights/team/models.py:

    class Meta:
        db_table = 'service'
        verbose_name = '服务与支持'
        verbose_name_plural = '服务与支持'
        

    def __str__(self):
        return self.name

