from django.db import models


class Phone(models.Model):
    price = models.IntegerField()
    oper_sys = models.CharField(max_length=50)
    lte_technology = models.CharField(default='-', max_length=10)
    display = models.CharField(max_length=10)
    cam_2 = models.CharField(default='-', max_length=10)
    ram = models.IntegerField(default=0)
    modul_nfc = models.CharField(default='-', max_length=10)


class Apple (models.Model):
    name_of_manufacture = models.CharField(max_length=10, default='Apple')
    name = models.CharField(max_length=20)
    phone = models.ForeignKey('Phone', on_delete=models.CASCADE)


class Digma (models.Model):
    name_of_manufacture = models.CharField(max_length=10, default='DIGMA')
    name = models.CharField(max_length=20)
    phone = models.ForeignKey('Phone', on_delete=models.CASCADE)


class Vertex (models.Model):
    name_of_manufacture = models.CharField(max_length=10, default='VERTEX')
    name = models.CharField(max_length=20)
    phone = models.ForeignKey('Phone', on_delete=models.CASCADE)
