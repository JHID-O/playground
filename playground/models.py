from django.db import models

class DownloadNotification(models.Model):
    name = models.CharField(max_length=200)
    phil_no = models.CharField(max_length=50)
    date_hired = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    email = models.EmailField()
    download_date = models.DateTimeField(auto_now_add=True)
    doc_file = models.FileField(upload_to='notifications/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.phil_no} - {self.download_date.strftime('%Y-%m-%d %H:%M')}"
from django.db import models

class PlaygroundModel(models.Model):
    month = models.CharField(max_length=20)
    year = models.IntegerField()
    PHN = models.CharField(max_length=20)
    surname = models.CharField(max_length=100)
    given_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    ps = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    es = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.surname}, {self.given_name} ({self.PHN})"

    class Meta:
        verbose_name = "Playground Model"
        verbose_name_plural = "Playground Models"
        ordering = ['-year', 'month', 'surname']