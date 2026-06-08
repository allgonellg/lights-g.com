from django.db import models
from django.utils.text import slugify

# Create your models here.
class Slide(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField('幻灯片', upload_to='slide', blank=True, null=True,help_text='最佳尺寸:1920*1080')
    title = models.CharField('主标题',max_length=200,help_text='主标题')
    content = models.TextField('一级标题',help_text='一级标题',default='')
    content_next = models.TextField('二级标题',help_text='二级标题',default='')


    class Meta:
        db_table = 'slide'
        verbose_name = '幻灯片管理'
        verbose_name_plural= '幻灯片管理'

