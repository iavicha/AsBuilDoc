from django.test import TestCase

from database_app.models import Job, Material, HiddenWorksSurveyCertificate


class JobTest(TestCase):
    def setUp(self) -> None:
        Job.objects.create(name="Работа", start_date="2021-02-21", end_date="2021-02-22")

    def test_job_name(self):
        job_name = Job.objects.get(name="Работа")
        self.assertEqual(str(job_name.start_date), "2021-02-21")
        self.assertIsNotNone(job_name.name)
        self.assertIsNotNone(job_name.end_date)


class MaterialTest(TestCase):
    def setUp(self) -> None:
        Material.objects.create(name='Проверочное имя создания материала')

    def test_material_name(self):
        material_test = Material.objects.get(name='Проверочное имя создания материала')
        self.assertEqual(str(material_test.name), 'Проверочное имя создания материала')
        self.assertIsNotNone(material_test.documents)
