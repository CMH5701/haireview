# Generated by Django 4.0.4 on 2022-11-28 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('free', '0001_initial'),
        ('QnA', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('p_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='free.free')),
                ('qna_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='QnA.question')),
            ],
        ),
    ]
