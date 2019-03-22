# Generated by Django 2.1.5 on 2019-03-22 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=16)),
                ('type_of_user', models.CharField(choices=[('M', 'Manager'), ('C', 'Contractor')], max_length=1)),
            ],
        ),
    ]
