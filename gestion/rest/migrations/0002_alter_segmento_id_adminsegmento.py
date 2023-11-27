# Generated by Django 4.2.6 on 2023-11-27 20:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='segmento',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='AdminSegmento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('segmento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rest.segmento')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]