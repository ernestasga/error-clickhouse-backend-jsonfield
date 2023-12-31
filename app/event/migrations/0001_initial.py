# Generated by Django 4.2.7 on 2023-11-28 15:42

import clickhouse_backend.models
from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', clickhouse_backend.models.GenericIPAddressField(default='::')),
                ('ipv4', clickhouse_backend.models.IPv4Field(default='127.0.0.1')),
                ('ip_nullable', clickhouse_backend.models.GenericIPAddressField(null=True)),
                ('port', clickhouse_backend.models.UInt16Field(default=0)),
                ('protocol', clickhouse_backend.models.StringField(default='', low_cardinality=True)),
                ('content', clickhouse_backend.models.JSONField(default=dict)),
                ('created_at', clickhouse_backend.models.DateTime64Field(auto_now_add=True)),
                ('action', clickhouse_backend.models.EnumField(choices=[(1, 'Pass'), (2, 'Drop'), (3, 'Alert')], default=1)),
            ],
            options={
                'indexes': [clickhouse_backend.models.Index(fields=['ip'], granularity=4, name='ip_set_idx', type=clickhouse_backend.models.Set(1000)), clickhouse_backend.models.Index(fields=['ipv4'], granularity=1, name='ipv4_bloom_idx', type=clickhouse_backend.models.BloomFilter(0.001))],
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('_overwrite_base_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddConstraint(
            model_name='event',
            constraint=models.CheckConstraint(check=models.Q(('port__gte', 0), ('port__lte', 65535)), name='port_range'),
        ),
    ]
