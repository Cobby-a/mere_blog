# Generated by Django 4.2.4 on 2023-10-23 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_alter_posts_date"),
    ]

    operations = [
        migrations.RenameField(
            model_name="posts",
            old_name="heading",
            new_name="title",
        ),
    ]
