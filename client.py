from socket import *
from threading import Thread
from customtkinter import *

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(("localhost", 8080))

my_data = sock.recv(64).decode().strip().split(",")

my_data_int_list = List(map(int, my_data_int_list)) 

my_id = my_data_int_list[0]
my_player_data = my_data_int_list[1:] 
