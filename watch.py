import time


def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours), int(mins), sec))


# input("Press Enter to start")
# start_time = time.time()
# input("Press Enter to stop")

# end_time = time.time()
# time_lapsed = end_time - start_time
# print(time_lapsed / 60)  # Minutes passed
# print((time_lapsed / 60) / 60)  # Hours passed
# time_convert(time_lapsed)
