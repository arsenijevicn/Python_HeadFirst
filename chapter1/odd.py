from datetime import datetime

import time
import random

nepar = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
         21, 23, 25, 27, 29, 31, 33, 35, 37,
         39, 41, 43, 45, 47, 49, 51, 53, 55,
            57, 59]

for i in range(5):
    trenutno = datetime.today().minute
    if trenutno in nepar:
        print("Ovaj minut je neparan!")
    else:
        print("Ovaj minut je paran!")
    wait_time = random.randint(1, 60)
    time.sleep(wait_time)


# import os
# import sys
# import datetime
# import time
# import html
#
# print(sys.platform)
# print(sys.version)
# print(os.getcwd())
# print(os.environ)
# print(os.getenv("HOME"))
# print(datetime.date.today())
# print(datetime.date.today().day)
# print(datetime.date.today().month)
# print(datetime.date.today().year)
# print(datetime.date.isoformat(datetime.date.today()))
# print(time.strftime("%H:%M"))
# print(time.strftime("%A %p"))

