from tweet_app.models import *


def my_scheduled_job():
    Comment.objects.all().delete()
