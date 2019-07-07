# Generated by Django 2.2 on 2019-06-29 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Salt', models.CharField(blank=True, max_length=100, null=True)),
                ('Company', models.CharField(blank=True, max_length=100, null=True)),
                ('MRP', models.PositiveIntegerField()),
                ('Shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicines', to='shop_app.Profile')),
            ],
        ),
    ]