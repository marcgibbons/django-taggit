# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taggeditem',
            name='content_type',
            field=models.ForeignKey(related_name='taggit_taggeditem_tagged_items', db_constraint=False, verbose_name='Content type', to='contenttypes.ContentType'),
        ),
    ]
