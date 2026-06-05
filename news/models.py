from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField  # 支持上传

# Create your models here.
class Category(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField('分类',max_length=10,help_text='分类名称')

    class Meta:
        db_table = 'category'
        verbose_name = '分类管理'
        verbose_name_plural = '分类管理'
    
    def __str__(self):
        return self.name


class News(models.Model):
    id = models.AutoField(primary_key=True)
    cover = models.ImageField('封面',upload_to='news',blank=True,null=True,help_text='最佳尺寸:')
    title = models.CharField('标题',max_length=100,help_text='资讯')
    content = RichTextUploadingField(verbose_name='正文')
    # 表的关联
    category = models.ForeignKey(Category,on_delete= models.CASCADE,verbose_name='分类')
    creat_at = models.DateTimeField('创建时间',auto_now_add=True,editable=True)
    update_at = models.DateTimeField('修改时间',auto_now_add=True,editable=True) 

    class Meta:
        db_table = 'news'
        verbose_name = '资讯'
        verbose_name_plural = '资讯'
    
    def __str__(self):
        return self.title

    