from django.db import models


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
    _license = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name


class People(models.Model):
    name = models.CharField(max_length=200)
    order = models.CharField(max_length=250)
    order_file = models.FileField(blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    _license = models.CharField(max_length=250)
    _license_file = models.FileField(blank=True)
    name_for_admin = str

    def __str__(self):
        return self.name + " " + self.company.name


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

    def __str__(self):
        return self.name


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
    customer_people = models.ForeignKey(People, on_delete=models.CASCADE, related_name="%(class)s_cust_people",
                                        blank=True)
    general_contractor_people = models.ForeignKey(People, on_delete=models.CASCADE,
                                                  related_name="%(class)s_contractor_people", blank=True)
    general_contractor_tech = models.ForeignKey(People, on_delete=models.CASCADE,
                                                related_name="%(class)s_general_contractor_tech_people", blank=True)
    designer_people = models.ForeignKey(People, on_delete=models.CASCADE, related_name="%(class)s_designer_people",
                                        blank=True)
    builder_people = models.ForeignKey(People, on_delete=models.CASCADE, related_name="%(class)s_builder_people",
                                       blank=True)

    class Meta:
        abstract = True


STATUS_CHOICES = [
    ("d", "Черновик"),
    ("p", "Распечатан"),
    ("w", "Подписан"),
]


class HiddenWorksSurveyCertificate(CommonFields):
    date_of_signature = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
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
