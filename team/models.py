from django.db import models

# Create your models here.
class Team(models.Model):

    id = models.AutoField(primary_key=True)
    image = models.ImageField('头像',upload_to='team',help_text='图片')
    name = models.CharField('姓名',max_length=200,help_text='团队成员')
    Job_position = models.CharField('职位',max_length=200,help_text='职位名称')
    rank = models.IntegerField('排序', default=0, help_text='数字越小越靠前')

    class Meta:
        db_table = 'team'
        verbose_name = '团队管理'
        verbose_name_plural = '团队管理'

    def __str__(self):
        return self.name
