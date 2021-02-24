from django.db import models
from django.contrib import admin


class Object(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    details = models.CharField(max_length=300)
    date_from = models.DateField()
    date_to = models.DateField()

    def __str__(self):
        return self.name


class People(models.Model):
    name = models.CharField(max_length=200)
    order = models.CharField(max_length=250)
    order_file = models.FileField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    _license = models.CharField(max_length=250)
    _license_file = models.FileField()

    def __str__(self):
        return self.name


class Job(models.Model):
    name = models.CharField(max_length=200)
    _next = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name


class Documents(models.Model):
    name = models.CharField(max_length=200)
    file = models.FileField()
    date_certificate_start = models.DateField(blank=True)
    date_certificate_emd = models.DateField(blank=True)


class Material(models.Model):
    name = models.CharField(max_length=200)
    documents = models.ManyToManyField(Documents)

    def __str__(self):
        return self.name


class ExecutiveScheme(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    file = models.FileField()

    def __str__(self):
        return self.name


class Trials(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    file = models.FileField()

    def __str__(self):
        return self.name


class CommonFields(models.Model):
    _object = models.ForeignKey(Object, on_delete=models.CASCADE)
    customer = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="%(class)s_customer")
    general_contractor = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="%(class)s_contractor")
    designer = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="%(class)s_designer")
    builder = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="%(class)s_builder")

    class Meta:
        abstract = True


class HiddenWorksSurveyCertificate(CommonFields):
    date_of_signature = models.DateField()
    number = models.CharField(max_length=40)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    material = models.ManyToManyField(Material)
    schemas = models.ManyToManyField(ExecutiveScheme)
    trials = models.ManyToManyField(Trials)
    other_people = models.CharField(max_length=200)

    def __str__(self):
        return self.job.name


class Template(CommonFields):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name