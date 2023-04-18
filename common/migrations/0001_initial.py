# Generated by Django 4.1.7 on 2023-03-24 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('constituency', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'County',
                'verbose_name_plural': 'Counties',
            },
        ),
        migrations.CreateModel(
            name='district',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('name', models.CharField(default=None, max_length=100)),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'District',
                'verbose_name_plural': 'Districts',
            },
        ),
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
                ('archived_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Parish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postcode', models.CharField(default=None, max_length=5)),
                ('code', models.CharField(default=None, max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Parish',
                'verbose_name_plural': 'Parishes',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
                ('archived_at', models.DateTimeField(blank=True, null=True)),
                ('code', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regions',
            },
        ),
        migrations.CreateModel(
            name='village',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=None, max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=False)),
                ('parish', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='common.parish')),
            ],
            options={
                'verbose_name': 'Village',
                'verbose_name_plural': 'Villages',
            },
        ),
        migrations.CreateModel(
            name='SubRegion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
                ('archived_at', models.DateTimeField(blank=True, null=True)),
                ('code', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('region', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='common.region')),
            ],
            options={
                'verbose_name': 'Sub Region',
                'verbose_name_plural': 'Sub Regions',
            },
        ),
        migrations.CreateModel(
            name='SubCounty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=None, max_length=20, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=False)),
                ('county', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='common.county')),
            ],
            options={
                'verbose_name': 'Sub County',
                'verbose_name_plural': 'Sub Counties',
            },
        ),
        migrations.AddField(
            model_name='parish',
            name='subcounty',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='common.subcounty'),
        ),
        migrations.CreateModel(
            name='LocalGovernment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_code', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('active', models.BooleanField(default=False)),
                ('district', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='common.district')),
            ],
            options={
                'verbose_name': 'Local Governments',
                'verbose_name_plural': 'Local Government',
            },
        ),
        migrations.AddField(
            model_name='district',
            name='sub_region',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='common.subregion'),
        ),
        migrations.AddField(
            model_name='county',
            name='district',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='common.district'),
        ),
        migrations.AddField(
            model_name='county',
            name='local_gov',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='common.localgovernment'),
        ),
    ]