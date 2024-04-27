# Generated by Django 4.2.9 on 2024-04-10 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_education_events_job_professionalexperience_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='title',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='linkedinuser',
            name='state',
            field=models.CharField(choices=[('US-PR', 'Puerto Rico'), ('US-AK', 'Alaska'), ('US-MS', 'Mississippi'), ('US-IA', 'Iowa'), ('US-RI', 'Rhode Island'), ('US-AL', 'Alabama'), ('US-MT', 'Montana'), ('US-ID', 'Idaho'), ('US-SC', 'South Carolina'), ('US-AR', 'Arkansas'), ('US-NC', 'North Carolina'), ('US-IL', 'Illinois'), ('US-SD', 'South Dakota'), ('US-AS', 'American Samoa'), ('US-ND', 'North Dakota'), ('US-IN', 'Indiana'), ('US-TN', 'Tennessee'), ('US-AZ', 'Arizona'), ('US-NE', 'Nebraska'), ('US-KS', 'Kansas'), ('US-TX', 'Texas'), ('US-CA', 'California'), ('US-NH', 'New Hampshire'), ('US-KY', 'Kentucky'), ('US-UM', 'United States Minor Outlying Islands'), ('US-CO', 'Colorado'), ('US-NJ', 'New Jersey'), ('US-LA', 'Louisiana'), ('US-UT', 'Utah'), ('US-CT', 'Connecticut'), ('US-NM', 'New Mexico'), ('US-MA', 'Massachusetts'), ('US-VA', 'Virginia'), ('US-DC', 'District of Columbia'), ('US-NV', 'Nevada'), ('US-MD', 'Maryland'), ('US-VI', 'Virgin Islands, U.S.'), ('US-DE', 'Delaware'), ('US-NY', 'New York'), ('US-ME', 'Maine'), ('US-VT', 'Vermont'), ('US-FL', 'Florida'), ('US-OH', 'Ohio'), ('US-MI', 'Michigan'), ('US-PA', 'Pennsylvania'), ('US-WA', 'Washington'), ('US-GA', 'Georgia'), ('US-OK', 'Oklahoma'), ('US-MN', 'Minnesota'), ('US-WI', 'Wisconsin'), ('US-GU', 'Guam'), ('US-OR', 'Oregon'), ('US-MO', 'Missouri'), ('US-WV', 'West Virginia'), ('US-HI', 'Hawaii'), ('US-MP', 'Northern Mariana Islands'), ('US-WY', 'Wyoming')], max_length=5),
        ),
    ]
