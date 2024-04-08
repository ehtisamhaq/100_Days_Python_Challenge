# import os, time

# for i in range(1, 1000):
#     print(i)
#     os.system("clear")

# print("Welcome")
# time.sleep(1)
# os.system("cls")
# username = input("username: ")


""" audio play """
# from playsound import playsound
# import time

# def play():
#     playsound('audio.wav')
#     while True:
#         stop_playback = input("Press 's' to stop playback: ")
#         if stop_playback.lower() == 's':
#             return

# while True:
#     print(" MyPOD Music Player ")
#     time.sleep(1)
#     print("Press 1 to Play")
#     time.sleep(1)
#     print("Press 2 to Exit")
#     time.sleep(1)
#     userInput = int(input("Enter your choice (1/2): "))
#     if userInput == 1:
#         print("Playing some proper tunes!")
#         play()
#     elif userInput == 2:
#         exit()
#     else:
#         continue
