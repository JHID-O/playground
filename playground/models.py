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