# Generated by Django 2.1.7 on 2019-02-22 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0002_auto_20190218_0016'),
    ]

    operations = [
        migrations.CreateModel(
            name='OCRText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, verbose_name='OCR text')),
                ('lang', models.TextField(default='EN', verbose_name='Language')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Create at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploader.ImageFile')),
            ],
            options={
                'verbose_name': 'OCRText',
                'verbose_name_plural': 'OCRTexts',
                'ordering': ['id'],
            },
        ),
    ]
