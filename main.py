import time
import pygame

def initialize_mixer():
    pygame.mixer.init()

def alert():
    print("ALERT! Time to take a break!")
    pygame.mixer.music.load('eff.mp3')
    pygame.mixer.music.play(loops=-1)

def stop_alert():
    print("Alert stopped.")
    pygame.mixer.music.stop()

def main():
    try:
        initialize_mixer()
        while True:
            alert_interval = 3 * 60
            alert_triggered = False
            
            input("Press any key to start the countdown...")
            print("\nCountdown started.")
            
            for time_remaining in range(alert_interval, 0, -1):
                print(f"Time remaining: {time_remaining // 60} minutes {time_remaining % 60} seconds", end='\r')
                time.sleep(1)
                
                if input_available():
                    print("\nUser input detected. Stopping the sound and restarting the timer.")
                    stop_alert()
                    alert_triggered = False
                    break
            
            stop_alert()

            if not alert_triggered:
                alert()
                
                while True:
                    if input_available():
                        print("\nUser input detected. Stopping the sound.")
                        stop_alert()
                        break
            
    except KeyboardInterrupt:
        print("\nScript terminated by user.")

def input_available():
    import msvcrt
    return msvcrt.kbhit() and msvcrt.getch()

if __name__ == "__main__":
    main()
