# Generated by Django 4.2.9 on 2024-04-10 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_job_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='state',
            field=models.CharField(blank=True, choices=[('US-AR', 'Arkansas'), ('US-SD', 'South Dakota'), ('US-ND', 'North Dakota'), ('US-IN', 'Indiana'), ('US-AS', 'American Samoa'), ('US-TN', 'Tennessee'), ('US-NE', 'Nebraska'), ('US-KS', 'Kansas'), ('US-AZ', 'Arizona'), ('US-TX', 'Texas'), ('US-NH', 'New Hampshire'), ('US-KY', 'Kentucky'), ('US-CA', 'California'), ('US-UM', 'United States Minor Outlying Islands'), ('US-NJ', 'New Jersey'), ('US-LA', 'Louisiana'), ('US-CO', 'Colorado'), ('US-UT', 'Utah'), ('US-NM', 'New Mexico'), ('US-MA', 'Massachusetts'), ('US-CT', 'Connecticut'), ('US-VA', 'Virginia'), ('US-NV', 'Nevada'), ('US-MD', 'Maryland'), ('US-DC', 'District of Columbia'), ('US-VI', 'Virgin Islands, U.S.'), ('US-NY', 'New York'), ('US-ME', 'Maine'), ('US-DE', 'Delaware'), ('US-VT', 'Vermont'), ('US-OH', 'Ohio'), ('US-MI', 'Michigan'), ('US-FL', 'Florida'), ('US-WA', 'Washington'), ('US-OK', 'Oklahoma'), ('US-MN', 'Minnesota'), ('US-GA', 'Georgia'), ('US-WI', 'Wisconsin'), ('US-OR', 'Oregon'), ('US-MO', 'Missouri'), ('US-GU', 'Guam'), ('US-WV', 'West Virginia'), ('US-PA', 'Pennsylvania'), ('US-MP', 'Northern Mariana Islands'), ('US-HI', 'Hawaii'), ('US-WY', 'Wyoming'), ('US-PR', 'Puerto Rico'), ('US-MS', 'Mississippi'), ('US-IA', 'Iowa'), ('US-AK', 'Alaska'), ('US-RI', 'Rhode Island'), ('US-MT', 'Montana'), ('US-ID', 'Idaho'), ('US-AL', 'Alabama'), ('US-SC', 'South Carolina'), ('US-NC', 'North Carolina'), ('US-IL', 'Illinois')], max_length=5, null=True),
        ),
    ]
