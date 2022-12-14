# Generated by Django 4.1.3 on 2022-12-06 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_dessert_dessert_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='photo',
            field=models.ImageField(null=True, upload_to='images/categories'),
        ),
        migrations.AlterField(
            model_name='dessert',
            name='photo',
            field=models.ImageField(null=True, upload_to='images/desserts'),
        ),
        migrations.AlterField(
            model_name='filling',
            name='photo',
            field=models.ImageField(null=True, upload_to='images/fillings'),
        ),
    ]
