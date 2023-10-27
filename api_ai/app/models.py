from django.db import models

# Create your models here.

class Reports(models.Model):
    hacker_id = models.IntegerField()
    program_id = models.IntegerField()
    asset_id = models.IntegerField()
    vuln_id = models.IntegerField()
    severity = models.CharField(max_length=255)
    rating = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    impact = models.TextField()
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'reports'

    def __str__(self):
        return self.name