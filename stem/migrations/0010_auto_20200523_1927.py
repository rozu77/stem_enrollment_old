# Generated by Django 3.0.2 on 2020-05-23 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stem', '0009_auto_20200523_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_info',
            name='father_educ_attainment',
            field=models.CharField(blank=True, choices=[('', ''), ('Elementary Graduate', 'Elementary Graduate'), ('High School Graduate', 'High School Graduate'), ('College Graduate', 'College Graduate'), ('Vocational', 'Vocational'), ('Masters/Doctorate degree', 'Masters/Doctorate degree'), ('Did not attend school', 'Did not attend school')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student_info',
            name='grade_level_to_enroll',
            field=models.CharField(choices=[('Grade 11', 'Grade 11'), ('Grade 12', 'Grade 12')], max_length=50),
        ),
        migrations.AlterField(
            model_name='student_info',
            name='guardian_educ_attainment',
            field=models.CharField(blank=True, choices=[('', ''), ('Elementary Graduate', 'Elementary Graduate'), ('High School Graduate', 'High School Graduate'), ('College Graduate', 'College Graduate'), ('Vocational', 'Vocational'), ('Masters/Doctorate degree', 'Masters/Doctorate degree'), ('Did not attend school', 'Did not attend school')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student_info',
            name='mother_educ_attainment',
            field=models.CharField(blank=True, choices=[('', ''), ('Elementary Graduate', 'Elementary Graduate'), ('High School Graduate', 'High School Graduate'), ('College Graduate', 'College Graduate'), ('Vocational', 'Vocational'), ('Masters/Doctorate degree', 'Masters/Doctorate degree'), ('Did not attend school', 'Did not attend school')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student_info',
            name='strand',
            field=models.CharField(choices=[('', ''), ('Accountancy, Business and Management', 'ABM'), ('Humanities and Social Sciences', 'HUMSS'), ('Science, Technology, Engineering, and Mathematics', 'STEM'), ('General Academic Strand', 'GAS')], max_length=100),
        ),
    ]
