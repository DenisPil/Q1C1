from django.db import models


class Property(models.Model):

    property = models.IntegerField(blank=False, verbose_name='property')
    building_id = models.IntegerField(blank=False, verbose_name='building_id')
    owner_acquisition_date = models.DateTimeField(max_length=64,
                                                  verbose_name="owner_date")
    street1 = models.CharField(max_length=64, verbose_name="street")
    city = models.CharField(max_length=64, verbose_name="city")
    zip = models.IntegerField(blank=False, verbose_name='zip')
    last_name = models.CharField(max_length=64, verbose_name="last_name")
    first_name = models.CharField(max_length=64, verbose_name="first_name")
    email = models.EmailField(max_length=64, verbose_name="email")
    floor = models.IntegerField(default='0', verbose_name='floor')
    surface = models.IntegerField(default='0', verbose_name='surface')

    class Meta:
        verbose_name_plural = "Properties"
