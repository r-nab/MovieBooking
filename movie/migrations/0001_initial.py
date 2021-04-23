# Generated by Django 3.2 on 2021-04-22 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('year', models.PositiveIntegerField()),
                ('length_mins', models.PositiveIntegerField()),
            ],
            options={
                'unique_together': {('name', 'year')},
            },
        ),
    ]
