# Generated by Django 2.0.4 on 2018-06-27 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20180628_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertype',
            name='navbar_template',
            field=models.CharField(blank=True, db_index=True, max_length=250, null=True),
        ),
    ]