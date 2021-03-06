# Generated by Django 2.2.4 on 2021-03-05 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApartsnsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('images', models.ImageField(upload_to='')),
                ('good', models.IntegerField(blank=True, default=0, null=True)),
                ('read', models.IntegerField(blank=True, default=0, null=True)),
                ('readtext', models.CharField(blank=True, default='a', max_length=100, null=True)),
            ],
        ),
    ]
