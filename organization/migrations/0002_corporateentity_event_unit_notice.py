# Generated by Django 4.1.7 on 2023-03-20 05:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CorporateEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
                ('archived_at', models.DateTimeField(blank=True, null=True)),
                ('rank', models.PositiveSmallIntegerField()),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('headed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='organization.salaryscale')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
                ('archived_at', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(max_length=100)),
                ('caption', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, null=True)),
                ('start_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('location', models.CharField(default='UNEB Kyambogo Offices', max_length=255)),
                ('attachment', models.FileField(upload_to='uploads/events/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
                ('archived_at', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('entity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='entity', to='organization.corporateentity')),
                ('parent_entity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parententity', to='organization.corporateentity')),
                ('parent_unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parentunit', to='organization.unit')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
                ('archived_at', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(max_length=100)),
                ('caption', models.CharField(max_length=255)),
                ('detail', models.TextField(blank=True, null=True)),
                ('date_published', models.DateField(blank=True, null=True)),
                ('attachment', models.FileField(upload_to='uploads/notices/')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.event')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
