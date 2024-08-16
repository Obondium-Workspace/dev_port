# Generated by Django 5.0.7 on 2024-07-22 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='portfolio/')),
                ('category', models.CharField(choices=[('app', 'App'), ('card', 'Card'), ('web', 'Web')], max_length=20)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='service',
            name='color',
            field=models.CharField(choices=[('#007bff', 'Blue'), ('#28a745', 'Green'), ('#ffc107', 'Yellow'), ('#dc3545', 'Red'), ('#17a2b8', 'Teal'), ('#fd7e14', 'Orange'), ('#6f42c1', 'Purple'), ('#20c997', 'Cyan'), ('#0073aa', 'Dark Blue')], default='#17a2b8', max_length=7),
        ),
    ]
