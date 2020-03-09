from django.db import models

class Events(models.Model):
    title   = models.CharField(max_length=150)
    post    = models.TextField()
    Date    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Events"
    





