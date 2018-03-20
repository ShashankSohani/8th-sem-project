# Generated by Django 2.0.1 on 2018-03-20 20:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('silverstrike', '0004_auto_20180203_2257'),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseHold',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='importconfiguration',
            name='default_account',
            field=models.ForeignKey(blank=True, limit_choices_to={'account_type': 1}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='silverstrike.Account'),
        ),
    ]
