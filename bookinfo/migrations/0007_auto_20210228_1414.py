# Generated by Django 3.1.5 on 2021-02-28 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookinfo', '0006_book_votes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='votes',
            new_name='is_delete',
        ),
    ]