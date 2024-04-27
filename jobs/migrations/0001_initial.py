# Generated by Django 4.2.9 on 2024-04-10 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0006_remove_job_postedby_linkedinuser_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=30, null=True)),
                ('description', models.CharField(max_length=300)),
                ('deadline_date', models.DateField()),
                ('postedby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.linkedinuser')),
            ],
        ),
    ]
