from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Invoice(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    buyer_name = models.CharField(max_length=255, default='John Doe') 
    buyer_email = models.EmailField(default='example@example.com')
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return f"Invoice #{self.id} - {self.service.name}"
    
class InvoiceModel(models.Model):
    # Your model fields here

    def __str__(self):
        return f"Invoice {self.id}"

    # Add other fields for the invoice   

# Create your models here.
