from django.db import models

# Create your models here.
class Logger(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    employee_id = models.CharField(max_length = 200)
    time_log = models.DateField(auto_now=True)

    def __str__(self):
        self.employee_id