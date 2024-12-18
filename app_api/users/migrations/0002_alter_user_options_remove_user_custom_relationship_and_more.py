# Generated by Django 5.1.2 on 2024-11-21 00:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='custom_relationship',
        ),
        migrations.RemoveField(
            model_name='user',
            name='personality',
        ),
        migrations.RemoveField(
            model_name='user',
            name='relationship_status',
        ),
        migrations.AddField(
            model_name='user',
            name='is_adult',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
        migrations.CreateModel(
            name='UserRelationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relationship_type', models.CharField(choices=[('Girlfriend', 'Girlfriend'), ('Boyfriend', 'Boyfriend'), ('Bestie', 'Bestie'), ('Best Friend', 'Best Friend'), ('Custom', 'Custom')], max_length=20)),
                ('personality_type', models.IntegerField()),
                ('custom_name', models.CharField(blank=True, max_length=50, null=True)),
                ('ai_name', models.CharField(help_text='Name of the AI companion', max_length=50)),
                ('bio', models.TextField(blank=True, help_text='Short biography or description of the AI companion', max_length=500, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relationships', to='users.user')),
            ],
            options={
                'verbose_name': 'User Relationship',
                'verbose_name_plural': 'User Relationships',
                'unique_together': {('user', 'relationship_type', 'personality_type')},
            },
        ),
        migrations.DeleteModel(
            name='UserVerification',
        ),
    ]
