# Generated by Django 4.2 on 2023-04-26 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_usuario_rename_arquivo_audio_archive_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Row',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('row', models.CharField(max_length=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='audio',
            name='row',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.DO_NOTHING, related_name='row_audios', to='core.row'),
            preserve_default=False,
        ),
    ]
