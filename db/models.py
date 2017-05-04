from django.db import models


class TestDb(models.Model):

    title = models.CharField(
        max_length = 20,
    )
    
    class Meta:
        
        db_table = "test"

