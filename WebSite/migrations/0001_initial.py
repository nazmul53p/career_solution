# Generated by Django 3.0.8 on 2020-08-24 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BranchesName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branches_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='InstitutionsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institutions_category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StudyLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study_level_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjects_category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institutions', models.CharField(max_length=100)),
                ('icon', models.ImageField(upload_to='university_icon/')),
                ('website', models.URLField(blank=True, max_length=300)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='university_category', to='WebSite.Category')),
                ('institutions_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='university_institutionscategory', to='WebSite.InstitutionsCategory')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='university_location', to='WebSite.Location')),
                ('types', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='university_types', to='WebSite.Types')),
            ],
        ),
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branches_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches_branchesname', to='WebSite.BranchesName')),
                ('degree', models.ManyToManyField(to='WebSite.Degree')),
                ('study_level', models.ManyToManyField(to='WebSite.StudyLevel')),
                ('subjects_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches_institutionscategory', to='WebSite.SubjectsCategory')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches_university', to='WebSite.University')),
            ],
        ),
    ]
