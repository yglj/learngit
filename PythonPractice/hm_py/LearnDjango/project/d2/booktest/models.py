from django.db import models
from tinymce.models import HTMLField
# Create your models here.


class BookInfoAdmin(models.Manager):
    def all(self):
        return super().all().filter(isDelete=False)

    # @classmethod
    def create_book(self, name, pub_date):
        models_name = self.model
        book = models_name()
        book.b_title = name
        book.pub_date = pub_date
        book.read = 0
        book.comment = 0
        book.save()
        return book


class BookInfo(models.Model):
    b_title = models.CharField(max_length=40)
    pub_date = models.DateField()
    read = models.IntegerField(default=0)
    comment = models.CharField(max_length=128, default="")
    isDelete = models.BooleanField(default=False)
    objects = BookInfoAdmin()

    class Meta:
        db_table = 'booktest_bookinfo'  # 元选项，指定模型类的数据库表名


class RoleInfo(models.Model):
    r_name = models.CharField(max_length=40)
    render = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo)
    comment = models.CharField(max_length=128)
    isDelete = models.BooleanField(default=0)


class FieldExercise(models.Model):
    # one = models.AutoField()  # 自动增长的整型
    two = models.NullBooleanField()  # 支持NULL, True, False
    there = models.TextField()  # 大文本, 超过4000字符
    four = models.DecimalField(max_digits=4, decimal_places=2)  # 十进制浮点数，精确度高 max表示总位，decimal表示小数位
    five = models.FloatField()
    six = models.DateField()  # auto_now 保存时设置为当前时间，auto_now_add 第一次创建保存为当前时间
    seven = models.ImageField(db_column='img', null=True, blank=True)  # 继承FileField，对上传的内容进行校验
    # 字段约束 primary_key(主键) , unique(唯一值) , db_index(创建索引) , db_column(指定字段名)
    # null(允许为空) , blank(允许为空白值) , default(默认值)
    # blank,default 不影响表结构


"""
1.关联关系
一对多：models.ForeignKey(), 放在多类
多对多：models.ManyToManyField()
一对一：models.OneToOneField()
2.关联查询
多类查询：一类对象.多类名小写__set.all()
一类查询：多类对象.关联属性
        多类对象.关联属性_id
        查询函数（模型类关联属性名__模型类属性名__条件运算符=值）
        
3.自查询（表内关系字段指向自身主键）
"""


class AreaInfo(models.Model):
    title = models.CharField(max_length=128)
    parentNode = models.ForeignKey('self', null=True, blank=True)

    def __str__(self):
        return self.title

    def child(self):
        return self.title

    def parent(self):
        if self.parentNode is None:
            return ''
        return self.parentNode.title

    child.admin_order_field = 'title'  # 列排序
    parent.admin_order_field = 'title'
    child.short_description = '地区'  # 列标题
    parent.short_description = '上级地区'


class FileTest(models.Model):
    img = models.ImageField(verbose_name='上传图片', upload_to='booktest/')

    def __str__(self):
        return self.img


class HtmlTest(models.Model):
    ahtml = HTMLField()

    def __str__(self):
        return str(self.id)