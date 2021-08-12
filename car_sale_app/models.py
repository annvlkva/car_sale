from django.db import models

# Car model
class Car(models.Model):
    id = models.AutoField(primary_key=True)
    vin = models.CharField(max_length=17)
    make = models.TextField()
    model = models.TextField()
    year = models.IntegerField()
    dealer = models.ForeignKey('Dealer', related_name='cars', on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.vin

    class Meta:
        db_table = "car"


# Dealer model
class Dealer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    phone = models.CharField(max_length=11)
    address = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "dealer"
