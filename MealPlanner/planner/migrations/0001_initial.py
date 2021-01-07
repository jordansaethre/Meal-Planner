# Generated by Django 3.1.5 on 2021-01-07 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_title', models.CharField(max_length=100)),
                ('meal_type', models.CharField(blank=True, choices=[('B', 'Breakfast'), ('L', 'Lunch'), ('D', 'Dinner')], max_length=10)),
            ],
        ),
    ]