# coding=utf-8
from celery.schedules import crontab

# from datetime import timedelta

BROKER_URL = 'redis://127.0.0.1:6379'  # 指定 Broker

CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'  # 指定 Backend

CELERY_TIMEZONE = 'Asia/Shanghai'  # 指定时区，默认是 UTC

CELERY_ENABLE_UTC = True

CELERY_TASK_SERIALIZER = 'json'  # 任务序列化和反序列化 ls: json yaml msgpack pickle(不推荐)

CELERY_RESULT_SERIALIZER = 'json'  # 读取任务结果一般性能要求不高，所以使用了可读性更好的JSON

CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 4  # 任务过期时间，不建议直接写86400，应该让这样的magic数字表述更明显

CELERY_IMPORTS = (  # 指定导入的任务模块
    'app.tasks.job',
    'app.tasks.company'
)

CELERY_TASK_PUBLISH_RETRY = False  # 重试

# schedules
CELERYBEAT_SCHEDULE = {
    'crawl-jobs-count-task': {
        'task': 'app.tasks.crontab.crawl_lagou_job_count',
        'schedule': crontab(hour=0, minute=10),
        # "schedule": timedelta(seconds=5),
        # 'args': (5, 8)  # 任务函数参数
    },
}
