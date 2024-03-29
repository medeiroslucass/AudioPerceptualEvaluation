# Generated by Django 4.2 on 2023-04-28 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_row_audio_row'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='row',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='row_audios', to='core.row'),
        ),
        migrations.AlterField(
            model_name='row',
            name='row',
            field=models.CharField(max_length=3),
        ),
    ]
