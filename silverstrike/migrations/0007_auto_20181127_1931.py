# Generated by Django 2.1.3 on 2018-11-27 19:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('silverstrike', '0006_auto_20181025_2240'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecurringSplit',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField(default=datetime.date.today)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                              related_name='silverstrike_recurringsplit_incoming_transactions', to='silverstrike.Account')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                               related_name='silverstrike_recurringsplit_splits', to='silverstrike.Category')),
                ('opposing_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                       related_name='silverstrike_recurringsplit_outgoing_transactions', to='silverstrike.Account')),
            ],
            options={
                'ordering': ['-date', 'title'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='recurringtransaction',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recurringtransaction',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='split',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='silverstrike_split_incoming_transactions', to='silverstrike.Account'),
        ),
        migrations.AlterField(
            model_name='split',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='silverstrike_split_splits', to='silverstrike.Category'),
        ),
        migrations.AlterField(
            model_name='split',
            name='opposing_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='silverstrike_split_outgoing_transactions', to='silverstrike.Account'),
        ),
        migrations.AddField(
            model_name='recurringsplit',
            name='transaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='splits', to='silverstrike.RecurringTransaction'),
        ),
    ]
