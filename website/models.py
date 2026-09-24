from django.db import models


class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    destination = models.CharField(max_length=150)
    travel_date = models.DateField()
    travellers = models.PositiveIntegerField()

    vehicle = models.CharField(
        max_length=50,
        choices=[
            ('Car', 'Car'),
            ('Tempo Traveller', 'Tempo Traveller'),
            ('Tourist Bus', 'Tourist Bus'),
        ]
    )

    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.destination}"