# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-03 17:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dasso', '0008_ressource_any_authenticated'),
    ]

    operations = [
        migrations.RenameModel('Ressource', 'Resource')
    ]
