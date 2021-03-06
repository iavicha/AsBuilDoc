from django.test import TestCase
from .models import Job


class JobTest(TestCase):

    def setUp(self) -> None:
        Job.objects.create(name='Работа', start_date="2021-02-21", end_date="2021-02-22")

    def test_job_name(self):
        job_name = Job.objects.get(name='Работа')
        self.assertEqual(str(job_name.start_date), "2021-02-21")
