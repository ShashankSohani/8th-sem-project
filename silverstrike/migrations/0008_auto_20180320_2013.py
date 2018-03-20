# Generated by Django 2.0.1 on 2018-03-20 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('silverstrike', '0007_account_household'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='household',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='silverstrike.HouseHold'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='household',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='silverstrike.HouseHold'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recurringtransaction',
            name='household',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='silverstrike.HouseHold'),
            preserve_default=False,
        ),
    ]
