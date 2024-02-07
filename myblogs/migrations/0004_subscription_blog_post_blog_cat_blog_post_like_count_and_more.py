# Generated by Django 5.0.1 on 2024-02-06 06:59

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblogs', '0003_blog_post'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_email', models.EmailField(max_length=254)),
                ('u_membership', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='blog_post',
            name='blog_cat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myblogs.blog_category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog_post',
            name='like_count',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='blog_post',
            name='views_count',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='blog_category',
            name='blog_cat',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='blog_category',
            name='blogcat_description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='contact_info',
            name='u_message',
            field=models.CharField(max_length=300),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='myblogs.blog_post')),
            ],
        ),
    ]
