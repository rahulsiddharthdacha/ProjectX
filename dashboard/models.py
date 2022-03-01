from pyexpat import model
from django.db import models

# Create your models here.
class WMS(models.Model):
    timestamp=models.DateTimeField(default=None)
    ambient_temp=models.FloatField()
    solar_irradation=models.FloatField()
    module_temp=models.FloatField()
    wind_speed=models.FloatField()

    def __str__(self):
        return str(self.timestamp)



class DCmeter(models.Model):
    timestamp=models.DateTimeField(default=None)
    DcBusVoltage=models.FloatField()
    DcEnergy1=models.FloatField()
    DcEnergy2=models.FloatField()
    DcEnergy3=models.FloatField()
    DcEnergy4=models.FloatField()
    Inputcurrent1=models.FloatField()
    Inputcurrent2=models.FloatField()
    Inputcurrent3=models.FloatField()
    Inputcurrent4=models.FloatField()

    def __str__(self):
        return str(self.timestamp)
