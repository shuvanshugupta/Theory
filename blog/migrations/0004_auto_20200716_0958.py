# Generated by Django 3.0.8 on 2020-07-16 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_words_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='words',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
