from django.db import models

# Create your models here.
class formData(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    no_of_family = models.PositiveIntegerField(default=0)
    raised_amount = models.DecimalField(default=0.0, decimal_places=2, max_digits=10)
    fund_breakdown = models.TextField()
    family_in_egypt = models.BooleanField()
    fund_url = models.CharField(max_length=255)
    comments = models.TextField()
    approval = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"
