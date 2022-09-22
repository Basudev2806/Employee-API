from django.db import models

class Employee(models.Model):
    Name = models.CharField(max_length=100, blank=False)
    EID = models.CharField(max_length=100, blank=False)
    Salary = models.CharField(max_length=100, blank=False, primary_key=True)

    def __str__(self) -> str:
        return self.Name
