# Generated by Django 3.2.16 on 2022-11-29 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filling',
            fields=[
                ('filling_id', models.AutoField(primary_key=True, serialize=False)),
                ('filling_name', models.CharField(max_length=50)),
                ('filling_description', models.CharField(max_length=500)),
                ('photo', models.ImageField(null=True, upload_to='images/')),
            ],
            options={
                'ordering': ['filling_name'],
            },
        ),
    ]
