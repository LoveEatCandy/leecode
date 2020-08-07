from datetime import datetime


def check_time():
    if datetime.now().hour == 16:
        raise AssertionError("超过23点，自动关闭！")


check_time()
