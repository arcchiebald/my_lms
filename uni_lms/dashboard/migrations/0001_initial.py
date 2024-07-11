# Generated by Django 4.2.13 on 2024-07-11 00:09

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_remove_lmsuser_firstname_remove_lmsuser_lastname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('lmsuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('faculty', models.CharField(max_length=50)),
                ('gpa', models.DecimalField(decimal_places=2, help_text='GPA must be between 0.00 and 4.00', max_digits=3, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(4.0)])),
                ('current_semester', models.IntegerField(choices=[(6, '6'), (3, '3'), (8, '8'), (7, '7'), (2, '2'), (4, '4'), (5, '5'), (1, '1')], default=1)),
                ('subjects', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(code='invalid-subjects', message="Enter a list of subjects separated by symbol '/'. Example: i2i/mnsc/calc/fop/db", regex='^([a-zA-Z0-9-]+\\/)*[a-zA-Z0-9-]+$')])),
                ('gpa_history', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(code='invalid-gpahistory', message="Enter a list of gpa's per semester separated by symbol '/'. Example: 3.40/2/2.5/1.95", regex='^([a-zA-Z0-9-]+\\/)*[a-zA-Z0-9-]+$')])),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('users.lmsuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
