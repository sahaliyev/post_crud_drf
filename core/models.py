from re import T
from django.db import models
# would be greate to exted User model.
# Due to luck of time I skip this step for now
from django.contrib.auth.models import User
# Create your models here.
from django.template.defaultfilters import slugify


class News(models.Model):
    title = models.CharField(max_length=300)
    link = models.SlugField(blank=True),
    vote_count = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = "news"
        verbose_name_plural = "News"
        
    def save(self, *args, **kwargs):
        if not self.link:
            title_and_id = f"{self.title} {self.id}"
            self.link = slugify(title_and_id)
        super().save(*args, **kwargs)

class Comments(models.Model):
    post = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.content[:30]}..."

    class Meta:
        db_table = "comments"
        verbose_name_plural = "Comments"

