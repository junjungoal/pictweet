# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('text', models.TextField(verbose_name='ツイート内容')),
                ('image', models.TextField(verbose_name='画像')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
