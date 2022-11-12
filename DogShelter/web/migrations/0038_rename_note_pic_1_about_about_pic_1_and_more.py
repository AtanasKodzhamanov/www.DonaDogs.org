# Generated by Django 4.1.3 on 2022-11-12 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0037_rename_note_eng_about_section_desc_eng'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='note_pic_1',
            new_name='about_pic_1',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='note_pic_10',
            new_name='about_pic_10',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='note_pic_4',
            new_name='about_pic_3',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='note_pic_5',
            new_name='about_pic_4',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='note_pic_6',
            new_name='about_pic_5',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='note_pic_7',
            new_name='about_pic_6',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='note_pic_8',
            new_name='about_pic_7',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='note_pic_9',
            new_name='about_pic_8',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='note_bg',
            new_name='section_desc_bg',
        ),
        migrations.AddField(
            model_name='about',
            name='about_pic_9',
            field=models.URLField(blank=True, default='', max_length=300),
        ),
    ]
