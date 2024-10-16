# Generated by Django 5.1.1 on 2024-10-16 16:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_permission_userpermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='userpermission',
            options={},
        ),
        migrations.AlterField(
            model_name='userpermission',
            name='allowed',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='userpermission',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_specific_permissions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=50)),
                ('action', models.CharField(choices=[('view', 'View'), ('add', 'Add'), ('change', 'Change'), ('delete', 'Delete')], max_length=10)),
            ],
            options={
                'unique_together': {('model_name', 'action')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='userpermission',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='user',
            name='individual_permissions',
            field=models.ManyToManyField(blank=True, related_name='users_with_permissions', through='api.UserPermission', to='api.permission'),
        ),
        migrations.AddField(
            model_name='userpermission',
            name='permission',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_permissions', to='api.permission'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='userpermission',
            unique_together={('user', 'permission')},
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='api.role'),
        ),
        migrations.RemoveField(
            model_name='userpermission',
            name='action',
        ),
        migrations.RemoveField(
            model_name='userpermission',
            name='model_name',
        ),
        migrations.CreateModel(
            name='RolePermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allowed', models.BooleanField(default=True)),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='api.permission')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='permissions', to='api.role')),
            ],
            options={
                'unique_together': {('role', 'permission')},
            },
        ),
    ]
