# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProvCity',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('abittle', models.CharField(max_length=20)),
                ('aid', models.ForeignKey(blank=True, null=True, to='booktest.ProvCity')),
            ],
            options={
                'db_table': 'booktest_areainfo',
            },
        ),
    ]
