# Generated by Django 4.2.7 on 2023-11-28 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('posicion', models.CharField(max_length=100)),
                ('version', models.IntegerField(default=1)),
                ('superior_jerarquico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.empleado')),
            ],
        ),
    ]