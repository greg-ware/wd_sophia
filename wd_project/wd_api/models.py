# Data model
#
# See https://docs.djangoproject.com/en/3.2/topics/db/models/

from django.db import models

class Zone(models.Model):
    """ Waste zone
    """
    id = models.BigAutoField("id",primary_key=True)
    name = models.CharField("name", max_length=240)
    created = models.DateField("created",auto_now_add=True)
    updated = models.DateField("updated",auto_now=True)
    geometry = models.JSONField("geometry")

    def __str__(self):
        " Short string representation, id and name "
        return f"[{self.id}]: {self.name}"

class Report(models.Model):
    """ Waste Report model object
    """
    WASTE_TYPES = (
        ('JK','Junk'),
        ('VG','Vegetal'),
        ('CM','Construction Material'),
        ('VP','Vehicle parts'),
    )

    id = models.BigAutoField("id",primary_key=True)
    created = models.DateField("created",auto_now_add=True)
    updated = models.DateField("updated",auto_now=True)
    waste_type = models.CharField("waste_type",max_length=50, choices=WASTE_TYPES)
    location = models.JSONField("location")
    reported_by = models.EmailField("reported_by")

    def __str__(self):
        " Short string representation, id and waste type "
        return f"[{self.id}]: {self.waste_type}"