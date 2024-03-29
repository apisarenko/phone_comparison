# Generated by Django 2.1.1 on 2019-08-21 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_manufacture', models.CharField(default='Apple', max_length=10)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Digma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_manufacture', models.CharField(default='DIGMA', max_length=10)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('oper_sys', models.CharField(max_length=50)),
                ('lte_technology', models.CharField(default='-', max_length=10)),
                ('display', models.CharField(max_length=10)),
                ('cam_2', models.CharField(default='-', max_length=10)),
                ('ram', models.IntegerField(default=0)),
                ('modul_nfc', models.CharField(default='-', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Vertex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_manufacture', models.CharField(default='VERTEX', max_length=10)),
                ('name', models.CharField(max_length=10)),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phones.Phone')),
            ],
        ),
        migrations.AddField(
            model_name='digma',
            name='phone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phones.Phone'),
        ),
        migrations.AddField(
            model_name='apple',
            name='phone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phones.Phone'),
        ),
    ]
