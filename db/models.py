from django.db import models


class TestDb(models.Model):

    title = models.CharField(
        max_length = 20,
    )

