from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='labexam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_date', models.DateTimeField()),
                ('exam_name', models.CharField(max_length=300)),
                ('exam_description', models.TextField(max_length=500)),
                ('total_marks', models.FloatField()),
                ('pass_marks', models.FloatField()),
                ('exam_status', models.BooleanField()),
                ('is_active', models.BooleanField()),
            ],
        ),
    ]