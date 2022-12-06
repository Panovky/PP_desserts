# Generated by Django 4.1.3 on 2022-12-06 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_firstname', models.CharField(max_length=50)),
                ('user_lastname', models.CharField(max_length=50)),
                ('user_photo', models.ImageField(null=True, upload_to='images/users_photos')),
                ('review_description', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('photo_1', models.ImageField(blank=True, null=True, upload_to='images/reviews')),
                ('photo_2', models.ImageField(blank=True, null=True, upload_to='images/reviews')),
                ('photo_3', models.ImageField(blank=True, null=True, upload_to='images/reviews')),
                ('photo_4', models.ImageField(blank=True, null=True, upload_to='images/reviews')),
                ('photo_5', models.ImageField(blank=True, null=True, upload_to='images/reviews')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]