# Generated by Django 3.2.2 on 2021-05-10 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_alter_photo_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='ratio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
    ]
