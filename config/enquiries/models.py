from django.db import models


class Enquiries(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=20)
    email = models.EmailField()
    enquiry = models.TextField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-time']
        verbose_name = 'Enquiries'

    def __str__(self):
        return f"{self.name} - {self.enquiry}"

