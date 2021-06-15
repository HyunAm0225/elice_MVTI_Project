# Generated by Django 3.1.7 on 2021-04-12 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0002_character_character_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='character_img_url',
            field=models.URLField(default='', null=True, verbose_name='character img url'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='content',
            field=models.TextField(null=True, verbose_name='choice_content'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='character.question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='content',
            field=models.TextField(null=True, verbose_name='question_content'),
        ),
        migrations.AlterField(
            model_name='sentiment',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='sentiment name'),
        ),
        migrations.AlterField(
            model_name='sentimentcharacter',
            name='character',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='character.character'),
        ),
        migrations.AlterField(
            model_name='sentimentcharacter',
            name='rate',
            field=models.FloatField(null=True, verbose_name='rate'),
        ),
        migrations.AlterField(
            model_name='sentimentcharacter',
            name='sentiment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='character.sentiment'),
        ),
        migrations.AlterField(
            model_name='sentimentchoice',
            name='choice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='character.choice'),
        ),
        migrations.AlterField(
            model_name='sentimentchoice',
            name='sentiment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='character.sentiment'),
        ),
    ]
