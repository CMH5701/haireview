# Generated by Django 4.0.4 on 2022-11-28 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hashtag',
            name='r_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='review.review'),
        ),
    ]
