# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_remove_quote_submitted_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='submitted_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 4, 20, 42, 39, 346206, tzinfo=utc)),
        ),
    ]
