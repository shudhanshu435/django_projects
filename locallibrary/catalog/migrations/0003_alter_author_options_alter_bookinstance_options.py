# Generated by Django 5.0.1 on 2024-02-28 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_language_alter_book_options_bookinstance_borrower_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name']},
        ),
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
    ]
