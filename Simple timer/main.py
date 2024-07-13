import time

def get_time():
    while True:
        try:
            total_seconds = int(input("Enter the time in seconds: "))
            if total_seconds > 0:
                return total_seconds
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter an integer value.")

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        time_format = f"{mins:02d}:{secs:02d}"
        print(time_format, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

def main():
    total_seconds = get_time()
    countdown_timer(total_seconds)

if __name__ == "__main__":
    main()
