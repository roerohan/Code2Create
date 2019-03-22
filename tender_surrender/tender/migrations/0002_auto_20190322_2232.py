# Generated by Django 2.1.5 on 2019-03-22 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('under_project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tender.Project')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='type_of_user',
            field=models.CharField(choices=[('m', 'Manager'), ('c', 'Contractor')], max_length=1),
        ),
    ]
