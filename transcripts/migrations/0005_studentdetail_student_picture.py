# Generated by Django 4.0.2 on 2022-02-26 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcripts', '0004_studentdetail_student_parent_contact_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdetail',
            name='student_picture',
            field=models.ImageField(blank=True, default='default-profilepic.svg', null=True, upload_to=''),
        ),
    ]
