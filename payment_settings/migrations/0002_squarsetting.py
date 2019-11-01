# Generated by Django 2.2.6 on 2019-11-01 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SquarSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('is_live_mode', models.BooleanField(blank=True, default=False)),
                ('access_token', models.CharField(default='', max_length=100)),
                ('description', models.TextField(blank=True, default='', max_length=600)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'SquarSetting',
                'verbose_name_plural': 'SquarSetting',
                'ordering': ('name', 'updated_at'),
                'managed': True,
                'unique_together': {('access_token',)},
            },
        ),
    ]
