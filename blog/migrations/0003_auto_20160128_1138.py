# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_extract'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='extract',
            field=models.CharField(max_length=300, blank=True, default='Extract default. Favor de cambiar'),
        ),
    ]
