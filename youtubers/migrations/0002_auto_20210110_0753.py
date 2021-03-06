# Generated by Django 3.1.4 on 2021-01-10 07:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Youtuber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('photo', models.ImageField(upload_to='media/youtubers/%Y/%m/%d/')),
                ('video_url', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('city', models.CharField(max_length=255)),
                ('crew', models.CharField(choices=[('solo', 'solo'), ('small', 'small'), ('large', 'large'), ('medium', 'medium')], max_length=255)),
                ('camera', models.CharField(choices=[('nikon', 'nikon'), ('cannon', 'cannon'), ('sony', 'sony'), ('fuji', 'fuji'), ('others', 'others')], max_length=255)),
                ('age', models.IntegerField()),
                ('hight', models.IntegerField()),
                ('subs_count', models.IntegerField()),
                ('catagory', models.CharField(choices=[('programming', 'programming'), ('cooking', 'cooking'), ('fliming', 'fliming'), ('cinema', 'cinema'), ('teaching', 'teaching'), ('comedy', 'comedy')], max_length=255)),
                ('is_featured', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.DeleteModel(
            name='Youtubers',
        ),
    ]
