import time
import datetime 
import pygame

def set_alarm(alarm_time):
    print(f"You have set the alarm for {alarm_time}")
    sound_file = "alarm.mp3"
    
    is_running = True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time == alarm_time:
            print("Wake up")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            
            is_running = False
        
        time.sleep(1)


alarm_time = input("Enter the date and time you want to set the alarm: ")
set_alarm(alarm_time)