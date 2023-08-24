import time
from datetime import datetime, timedelta

def calculate_time_until_birthday(birthday):
    now = datetime.now()
    time_until_birthday = birthday - now
    return time_until_birthday

def format_time(delta):
    hours, seconds = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return hours, minutes, seconds

def print_stylized_number(number):
    big_numbers = [
        ["  ###  ", " #   # ", "#     #", "#     #", "#     #", " #   # ", "  ###  "],
        ["   #   ", "   #   ", "   #   ", "   #   ", "   #   ", "   #   ", "   #   "],
        [" ##### ", "#     #", "      #", " ##### ", "#      ", "#     #", "#######"],
        [" ##### ", "#     #", "      #", "  #### ", "      #", "#     #", " ##### "],
        ["#      ", "#    # ", "#    # ", "#    # ", "#######", "     # ", "     # "],
        ["#######", "#      ", "#      ", "###### ", "      #", "#     #", " ##### "],
        ["  ###  ", " #     ", "#      ", "###### ", "#     #", "#     #", " ##### "],
        ["#######", "     # ", "    #  ", "   #   ", "  #    ", " #     ", "#      "],
        [" ##### ", "#     #", "#     #", " ##### ", "#     #", "#     #", " ##### "],
        [" ##### ", "#     #", "#     #", " ######", "      #", "#     #", " ##### "]
    ]
    
    big_happy_birthday = [
        "H   H  AAA  PPPPP  PPPPP  Y   Y        BBBBB IIIII RRRRR  TTTTT  H   H DDDD   AAA  Y   Y",
        "H   H A   A P   P  P   P   Y Y         B   B   I   R   R    T    H   H D   D A   A  Y Y ",
        "HHHHH AAAAA PPPPP  PPPPP    Y          BBBB    I   RRRRR    T    HHHHH D   D AAAAA   Y  ",
        "H   H A   A P      P        Y          B   B   I   R  R     T    H   H D   D A   A   Y  ",
        "H   H A   A P      P        Y          BBBBB IIIII R   R    T    H   H DDDD  A   A   Y  "
    ]
    
    hours, minutes, seconds = number
    
    digits = [seconds // 10, seconds % 10]
    if hours > 0:
        digits = [hours // 10, hours % 10, -1, minutes // 10, minutes % 10, -1, -1, seconds // 10, seconds % 10]
    elif minutes > 0:
        digits = [minutes // 10, minutes % 10, -1, -1, seconds // 10, seconds % 10]
    
    if hours == 0 and minutes == 0 and seconds == 0:
        for line in big_happy_birthday:
            print(line)
        return
    
    for row in range(7):
        line = " ".join([big_numbers[d][row] if d != -1 else " " for d in digits])
        print(line)

def main():
    birthday = datetime(datetime.now().year, 12, 31, 23, 59)  # Set the birthday date and time (Month, Day, Hour, Minute)

    while True:
        time_until_birthday = calculate_time_until_birthday(birthday)
        if time_until_birthday.total_seconds() <= 0:
            print_stylized_number((0, 0, 0))
            break

        hours, minutes, seconds = format_time(time_until_birthday)
        
        print_stylized_number((hours, minutes, seconds))
        time.sleep(1)
        print("\033[H\033[J", end="")

if __name__ == "__main__":
    main()
