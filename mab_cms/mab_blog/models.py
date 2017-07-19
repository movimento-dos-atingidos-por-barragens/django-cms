from django.db import models
from django.db.models import permalink
from filer.fields.image import FilerImageField
from djangocms_text_ckeditor.fields import HTMLField
from taggit.managers import TaggableManager

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    hat = models.CharField(max_length=64, blank=True, null=True)
    author = models.CharField(max_length=64, blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = HTMLField(blank=True, null=True)
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('mab_blog.Category')
    tags = TaggableManager(blank=True)
    cover_image = FilerImageField(blank=True, null=True)

    def __str__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, {
                                        'slug': self.slug,
                                        'year': self.posted.year,
                                        'month': '{0:02d}'.format(self.posted.month),
                                        'day': '{0:02d}'.format(self.posted.day) })

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })
