# Generated by Django 3.1.6 on 2021-02-19 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authtoken', '0003_tokenproxy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=25)),
                ('deleted', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15)),
                ('content', models.CharField(max_length=250)),
                ('post_time', models.DateTimeField()),
                ('image_url', models.CharField(max_length=50)),
                ('approved', models.BooleanField()),
                ('deleted', models.BooleanField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authtoken.token')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rareapi.category')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=25)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authtoken.token')),
            ],
        ),
        migrations.CreateModel(
            name='PostTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rareapi.post')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rareapi.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=25)),
                ('comment', models.CharField(max_length=250)),
                ('deleted', models.BooleanField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authtoken.token')),
            ],
        ),
    ]
