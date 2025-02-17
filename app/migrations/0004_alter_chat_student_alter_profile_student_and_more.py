# Generated by Django 4.2.10 on 2024-03-22 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_chat_student_alter_profile_student_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='student',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.student'),
        ),
        migrations.AlterField(
            model_name='takeattendance',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student'),
        ),
    ]
