from django.db import models
from django.db.models import permalink
from filer.fields.image import FilerImageField
from djangocms_text_ckeditor.fields import HTMLField

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = HTMLField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('mab_blog.Category')
    background_image = FilerImageField(null=True, blank=True)

    def __str__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })