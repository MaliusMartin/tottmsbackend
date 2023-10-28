# Generated by Django 4.2.5 on 2023-10-16 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tottmsappbeta', '0011_transferreasons_transferapplication_reasons_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transferapplication',
            name='RequestedDistrictID',
        ),
        migrations.AddField(
            model_name='transferapplication',
            name='FromRegionID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='from_region', to='tottmsappbeta.region'),
        ),
        migrations.AddField(
            model_name='transferapplication',
            name='ToRegionID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_region', to='tottmsappbeta.region'),
        ),
        migrations.AlterField(
            model_name='transferapplication',
            name='ApplicationDate',
            field=models.DateField(auto_now_add=True),
        ),
    ]
