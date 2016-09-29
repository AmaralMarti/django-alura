# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0002_remove_perfil_nome_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='nome_empresa',
            field=models.CharField(default=b'xxx', max_length=255),
            preserve_default=True,
        ),
    ]
