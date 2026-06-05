from django.db import models
# from ckeditor.fields import RichTextField

# Create your models here.
class About_us(models.Model):
    id = models.AutoField(primary_key=True)
    development_history_time = models.CharField('发展时间',max_length=20,help_text='填写年份')
    development_history_content = models.TextField('发展历程')

    class Meta:
        db_table = 'about_us'
        verbose_name = '关于我们'
        verbose_name_plural = '关于我们'

class Partner(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField('客户logo',upload_to='partner',help_text='最佳尺寸:')
    name = models.CharField('客户名称',max_length=20,help_text='合作伙伴')

    class Meta:
        db_table = 'partner'
        verbose_name = '合作伙伴'
        verbose_name_plural = '合作伙伴'

    def __str__(self):
        return self.name