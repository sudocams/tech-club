from django.db import models

TEAM_CHOICES = [
    ('INDIVIDUAL', 'INDIVIDUAL'),
    ('TEAM', 'TEAM'),
]


LANGUAGES_CHOICES = [
    ('PYTHON', 'PYTHON'),
    ('JAVA', 'JAVA'),
    ('NODE', 'NODE'),
    ('ANGULAR', 'ANGULAR'),
    ('ARDUINO', 'ARDUINO'),
    ('PHP', 'PHP'),
    ('REACT', 'REACT'),
    ('HTML', 'HTML'),
    ('SECURITY', 'SECURITY'),
    ('NETWORKS', 'NETWORKS'),
    ('DATASCIENCE', 'DATASCIENCE'),
     
]

class Applications(models.Model):
    name        = models.CharField(max_length=200)
    number      = models.IntegerField(default = 0)
    email       = models.EmailField()
    admin_no    = models.CharField(max_length=40)
    langauges   = models.CharField(max_length=50, choices=LANGUAGES_CHOICES)
    team        = models.CharField(max_length = 60, choices=TEAM_CHOICES)
    idea        = models.FileField(upload_to='documents/')
    bio         = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Applications"
    
