import time

def timer(sec):
    while sec:
        mins, secs = divmod(sec, 60)
        time_display = f"{mins:02d}:{secs:02d}"
        print(time_display, end="\r")
        time.sleep(1)
        sec -= 1
    print("Time's up!            ")

def main():
    try:
        min = int(input("Enter minutes: "))
        sec = int(input("Enter seconds: "))
        total_sec = min * 60 + sec
        print("⏳ Timer started....")
        timer(total_sec)
    except ValueError:
        print("❌ Please enter valid numbers.")

if __name__ == "__main__":
    main()
