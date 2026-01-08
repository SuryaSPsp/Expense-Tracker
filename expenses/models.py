from django.db import models

# Create your models here.
class Expense(models.Model):
    expense_id = models.AutoField(primary_key=True)
    date = models.DateField()
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    payment_mode = models.CharField(max_length=50)
    merchant_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    created_by = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.category} - {self.amount}"
