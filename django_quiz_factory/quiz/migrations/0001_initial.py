# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('category', models.CharField(null=True, verbose_name='Category', unique=True, max_length=250, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'verbose_name': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('score', models.CommaSeparatedIntegerField(max_length=1024, verbose_name='Score')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name_plural': 'User progress records',
                'verbose_name': 'User Progress',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('figure', models.ImageField(upload_to='uploads/%Y/%m/%d', blank=True, null=True, verbose_name='Figure')),
                ('content', models.CharField(help_text='Enter the question text that you want displayed', max_length=1000, verbose_name='Question')),
                ('explanation', models.TextField(blank=True, help_text='Explanation to be shown after the question has been answered.', max_length=2000, verbose_name='Explanation')),
                ('category', models.ForeignKey(to='quiz.Category', null=True, blank=True, verbose_name='Category')),
            ],
            options={
                'ordering': ['category'],
                'verbose_name_plural': 'Questions',
                'verbose_name': 'Question',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Title')),
                ('description', models.TextField(blank=True, help_text='a description of the quiz', verbose_name='Description')),
                ('url', models.SlugField(help_text='a user friendly url', max_length=60, verbose_name='user friendly url')),
                ('random_order', models.BooleanField(default=False, help_text='Display the questions in a random order or as they are set?', verbose_name='Random Order')),
                ('max_questions', models.PositiveIntegerField(blank=True, help_text='Number of questions to be answered on each attempt.', null=True, verbose_name='Max Questions')),
                ('answers_at_end', models.BooleanField(default=False, help_text='Correct answer is NOT shown after question. Answers displayed at the end.', verbose_name='Answers at end')),
                ('exam_paper', models.BooleanField(default=False, help_text='If yes, the result of each attempt by a user will be stored. Necessary for marking.', verbose_name='Exam Paper')),
                ('single_attempt', models.BooleanField(default=False, help_text='If yes, only one attempt by a user will be permitted. Non users cannot sit this exam.', verbose_name='Single Attempt')),
                ('pass_mark', models.SmallIntegerField(validators=[django.core.validators.MaxValueValidator(100)], blank=True, default=0, help_text='Percentage required to pass exam.')),
                ('success_text', models.TextField(blank=True, help_text='Displayed if user passes.', verbose_name='Success Text')),
                ('fail_text', models.TextField(blank=True, help_text='Displayed if user fails.', verbose_name='Fail Text')),
                ('draft', models.BooleanField(default=False, help_text='If yes, the quiz is not displayed in the quiz list and can only be taken by users who can edit quizzes.', verbose_name='Draft')),
                ('category', models.ForeignKey(to='quiz.Category', null=True, blank=True, verbose_name='Category')),
            ],
            options={
                'verbose_name_plural': 'Quizzes',
                'verbose_name': 'Quiz',
            },
        ),
        migrations.CreateModel(
            name='Sitting',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('question_order', models.CommaSeparatedIntegerField(max_length=1024, verbose_name='Question Order')),
                ('question_list', models.CommaSeparatedIntegerField(max_length=1024, verbose_name='Question List')),
                ('incorrect_questions', models.CommaSeparatedIntegerField(blank=True, max_length=1024, verbose_name='Incorrect questions')),
                ('current_score', models.IntegerField(verbose_name='Current Score')),
                ('complete', models.BooleanField(default=False, verbose_name='Complete')),
                ('user_answers', models.TextField(blank=True, default='{}', verbose_name='User Answers')),
                ('start', models.DateTimeField(auto_now_add=True, verbose_name='Start')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='End')),
            ],
            options={
                'permissions': (('view_sittings', 'Can see completed exams.'),),
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('sub_category', models.CharField(blank=True, null=True, max_length=250, verbose_name='Sub-Category')),
                ('category', models.ForeignKey(to='quiz.Category', null=True, blank=True, verbose_name='Category')),
            ],
            options={
                'verbose_name_plural': 'Sub-Categories',
                'verbose_name': 'Sub-Category',
            },
        ),
        migrations.CreateModel(
            name='ExamSitting',
            fields=[
                ('sitting_ptr', models.OneToOneField(primary_key=True, to='quiz.Sitting', auto_created=True, serialize=False, parent_link=True)),
                ('current_question', models.IntegerField(default=0)),
            ],
            bases=('quiz.sitting',),
        ),
        migrations.AddField(
            model_name='sitting',
            name='quiz',
            field=models.ForeignKey(to='quiz.Quiz', verbose_name='Quiz'),
        ),
        migrations.AddField(
            model_name='sitting',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ManyToManyField(blank=True, to='quiz.Quiz', verbose_name='Quiz'),
        ),
        migrations.AddField(
            model_name='question',
            name='sub_category',
            field=models.ForeignKey(to='quiz.SubCategory', null=True, blank=True, verbose_name='Sub-Category'),
        ),
    ]
