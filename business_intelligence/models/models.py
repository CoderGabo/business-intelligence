from django.db import models

# Create your models here.
class Vehicle(models.Model):
    vin = models.CharField(max_length=50, primary_key=True)
    licensePlate = models.CharField(max_length=50)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()

    class Meta:
        db_table = 'vehicle'

class Servicio(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    class Meta:
        db_table = 'service'

# Modelo de cita (anteriormente mantenimiento)
class Cita(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, to_field='vin')
    scheduleDate = models.CharField(max_length=20)
    status = models.CharField(max_length=50)

    class Meta:
        db_table = 'appointment'

class Mantenimiento(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, to_field='vin')
    date = models.DateField()
    status = models.CharField(max_length=50)
    appointment = models.ForeignKey(Cita, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'maintenance'

class ServicioCita(models.Model):
    appointment = models.ForeignKey(Cita, on_delete=models.CASCADE) 
    service = models.ForeignKey(Servicio, on_delete=models.CASCADE)  

    class Meta:
        db_table = 'service_appointment'

class Detail(models.Model):
    maintenance = models.ForeignKey(Mantenimiento, on_delete=models.CASCADE)
    description = models.TextField()
    cost = models.IntegerField()

    class Meta:
        db_table = 'detail'