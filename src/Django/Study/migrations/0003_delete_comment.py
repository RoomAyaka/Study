# Generated by Django 4.1.4 on 2023-01-04 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Study', '0002_alter_article_options_remove_article_titile_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]