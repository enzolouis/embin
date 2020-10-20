from django.db import models

# Create your models here.

from datetime import datetime


def get_there_is_format(created_at):
            stats = {
                "years":datetime.now().year - created_at.year,
                "months":datetime.now().month - created_at.month,
                "days":datetime.now().day - created_at.day,
                "hours":datetime.now().hour - created_at.hour,
                "minutes":datetime.now().minute - created_at.minute,
                "seconds":datetime.now().second - created_at.second,
            }

            print(stats)

            there_is_ago = "/"

            for x, y in stats.items():
                if y > 0:
                    if x == 1:
                        there_is_ago = f"il y a {y} {x.rstrip('s')}"
                    else:
                        there_is_ago = f"il y a {y} {x}"
                    break

            return there_is_ago


print(get_there_is_format(datetime(year=2020, month=10, day=18, hour=10, minute=20, second=1)))