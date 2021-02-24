# Generated by Django 3.1.7 on 2021-02-23 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('details', models.CharField(max_length=300)),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ExecutiveScheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('_next', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('certificate', models.CharField(max_length=200)),
                ('certificate_file', models.FileField(max_length=200, upload_to='')),
                ('date_certificate_start', models.DateField()),
                ('date_certificate_emd', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Trials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database_app.object')),
                ('builder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='template_builder', to='database_app.company')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='template_customer', to='database_app.company')),
                ('designer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='template_designer', to='database_app.company')),
                ('general_contractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='template_contractor', to='database_app.company')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('order', models.CharField(max_length=250)),
                ('order_file', models.FileField(upload_to='')),
                ('_license', models.CharField(max_length=250)),
                ('_license_file', models.FileField(upload_to='')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database_app.company')),
            ],
        ),
        migrations.CreateModel(
            name='HiddenWorksSurveyCertificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_signature', models.DateField()),
                ('number', models.CharField(max_length=40)),
                ('other_people', models.CharField(max_length=200)),
                ('_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database_app.object')),
                ('builder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hiddenworkssurveycertificate_builder', to='database_app.company')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hiddenworkssurveycertificate_customer', to='database_app.company')),
                ('designer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hiddenworkssurveycertificate_designer', to='database_app.company')),
                ('general_contractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hiddenworkssurveycertificate_contractor', to='database_app.company')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database_app.job')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database_app.material')),
                ('schemas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database_app.executivescheme')),
                ('trials', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database_app.trials')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
