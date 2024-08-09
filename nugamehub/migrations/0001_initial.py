# Generated by Django 5.1 on 2024-08-09 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('file_path', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='games/')),
            ],
        ),
    ]
