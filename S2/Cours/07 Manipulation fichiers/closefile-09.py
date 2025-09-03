import os

file = open("crash.txt", mode="w")
file.write("Hello, world!")
os._exit(1)