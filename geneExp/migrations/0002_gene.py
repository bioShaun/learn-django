# Generated by Django 2.2.4 on 2019-08-29 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geneExp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gene_id', models.CharField(max_length=200)),
            ],
        ),
    ]