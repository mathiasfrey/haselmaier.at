from django.db import models


class BlogAuthor(models.Model):
    
    name = models.CharField(max_length=40)
    job_title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_author/')

    def __str__(self):
        return self.name
    
    
class BlogEntry(models.Model):
    
    GROUP = 'GR'
    TISCHLEREI = 'TI'
    WOHNART = 'WA'
    LEITSTELLEN = 'LS'
    ETECHNIK = 'ET'
    BLOG = 'BL'
    PG8 = 'P8'
    
    BRAND_CHOICES = (
        (GROUP, 'Group'),
        (TISCHLEREI, 'Tischlerei'),
        (WOHNART, 'Wohn-Art'),
        (LEITSTELLEN, 'Leitstellen'),
        (ETECHNIK, 'E-Technik'),
        (BLOG, 'Blog'),
        (PG8, 'pg8'),
    )
    
    MARKDOWN = 'MD'
    HTML5 = 'H5'
    
    RENDERER_CHOICES = (
        (MARKDOWN, 'Markdown'),
        (HTML5, 'HTML5'),
    )
    
    
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique = True)
    
    title_image = models.ImageField(upload_to='blog/')
    
    body = models.TextField()
    
    publish = models.BooleanField(default=True)
    created = models.DateTimeField()
    modified = models.DateTimeField(auto_now = True)
    
    brand = models.CharField(max_length=2,
                             choices=BRAND_CHOICES,
                             default=GROUP)
    
    renderer = models.CharField(max_length=2,
                                choices=RENDERER_CHOICES,
                                default=MARKDOWN)
    
    tags = models.ManyToManyField("BlogTag")
    author = models.ForeignKey(BlogAuthor)
    

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]

class BlogTag(models.Model):
    name = models.CharField(max_length=30, unique=True)
    
    def __str__(self):
        return self.name

class BlogImage(models.Model):
    
    name = models.CharField(max_length=30, unique=True)
    image = models.ImageField(upload_to='blog/')
    
    def __str__(self):
        return str(self.image)
