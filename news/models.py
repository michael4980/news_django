from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    description = models.CharField(max_length=255)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    is_displayed = models.BooleanField(default=True)

    def __str__(self):
        return self.title
