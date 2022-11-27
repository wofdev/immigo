from django.db import models

# Create your models here.

class Author(models.Model):

    name = models.CharField(max_length=200, blank=True, null=True)
    url = models.CharField(max_length=2000, blank=True, null=True)
    avatar = models.CharField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.name


class Attachment(models.Model):
    url = models.CharField(max_length=2000,blank=True,null=True)
    title = models.CharField(max_length=2000,blank=True,null=True)
    mime_type = models.CharField(max_length=2000,blank=True,null=True)
    duration_in_seconds = models.CharField(max_length=10,blank=True,null=True)
    news = models.ForeignKey('News',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'{self.title} - {self.news}'


class Tag(models.Model):

    tag = models.CharField(max_length=200,blank=True, null=True)
    news = models.ForeignKey('News',on_delete=models.CASCADE, related_name='tags')
    def __str__(self):
        return self.tag

class News(models.Model):

    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=2000,blank=True, null=True)
    url = models.CharField(max_length=2000,blank=True, null=True)
    content_html = models.CharField(max_length=2000,blank=True, null=True)
    summary =models.CharField(max_length=2000,blank=True, null=True)
    date_published =models.CharField(max_length=2000,blank=True, null=True)
    date_modified = models.CharField(max_length=2000, blank=True, null=True)
    image =models.CharField(max_length=2000,blank=True, null=True)
    author =models.ForeignKey(Author,on_delete=models.CASCADE,related_name='authors',blank=True,null=True)

    def __str__(self):
        return f'{self.title} - {self.author}'
