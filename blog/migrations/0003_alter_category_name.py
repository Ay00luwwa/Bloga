# Generated by Django 4.2.5 on 2023-10-04 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_category_name_blogimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Tech', 'Tech'), ('Agriculture', 'Agriculture'), ('Health', 'Health and Fitness'), ('Food', 'Food'), ('Travel', 'Travel'), ('Sports', 'Sports'), ('Science', 'Science'), ('Gaming', 'Gaming'), ('Books', 'Books'), ('Media', 'Media'), ('TV', 'TV'), ('Religion', 'Religion'), ('Pets', 'Pets'), ('Animals', 'Animals'), ('Cars', 'Cars'), ('Fashion', 'Fashion'), ('Anime', 'Anime'), ('History', 'History'), ('Others', 'Others')], max_length=100, unique=True),
        ),
    ]
