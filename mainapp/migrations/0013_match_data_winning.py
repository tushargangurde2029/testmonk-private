# Generated by Django 3.1.7 on 2021-05-11 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_auto_20210511_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='match_data',
            name='winning',
            field=models.CharField(default='None', max_length=70),
        ),
    ]