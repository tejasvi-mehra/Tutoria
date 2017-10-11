# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 18:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutoria', '0002_tutor_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('tutor', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=0, default=0, max_digits=3)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutoria.Student')),
            ],
        ),
        migrations.AddField(
            model_name='tutor',
            name='student',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='transactions',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutoria.Tutor'),
        ),
    ]