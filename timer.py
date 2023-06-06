"""Time reading"""
import time

minute = 0
sec = 0
value = input("Enter Duration :")
while True:
    print(minute, ":", sec)
    time.sleep(1)
    sec = sec + 1
    if sec > 60:
        minute = minute + 1
        sec = 0
    if minute == value and sec == 1:
      break
