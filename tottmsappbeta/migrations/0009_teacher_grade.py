# Generated by Django 4.2.5 on 2023-10-07 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tottmsappbeta', '0008_teacher_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='grade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tottmsappbeta.workergrade'),
        ),
    ]