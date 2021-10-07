# Generated by Django 2.2.17 on 2021-09-14 19:49

import crashmanager.models
from django.db import migrations, models
import django.db.models.deletion


def add_crash_bucket_hits(apps, schema_editor):
    BucketHit = apps.get_model('crashmanager', 'BucketHit')
    CrashEntry = apps.get_model('crashmanager', 'CrashEntry')

    bucket_hits = {}
    crashes = CrashEntry.objects.filter(bucket__isnull=False)
    for bucket, tool, created in crashes.values_list("bucket_id", "tool_id", "created"):
        bucket_hits.setdefault((bucket, tool), {})
        begin = created.replace(microsecond=0, second=0, minute=0)
        bucket_hits[(bucket, tool)].setdefault(begin, 0)
        bucket_hits[(bucket, tool)][begin] += 1

    for (bucket, tool), hits in bucket_hits.items():
        for begin, count in hits.items():
            obj, _ = BucketHit.objects.get_or_create(bucket_id=bucket, tool_id=tool, begin=begin)
            obj.count += count
            obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('crashmanager', '0006_auto_20210913_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='BucketHit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin', models.DateTimeField(default=crashmanager.models.buckethit_default_range_begin)),
                ('count', models.IntegerField(default=0)),
                ('bucket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crashmanager.Bucket')),
                ('tool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crashmanager.Tool')),
            ],
        ),

        migrations.RunPython(
            add_crash_bucket_hits,
            reverse_code=migrations.RunPython.noop,
        ),

    ]
