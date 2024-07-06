# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 15:31:56 2024

@author: matth
"""
import hello
from bfs_and_dfs import bfs, dfs

def greet():
    print("Hi, welcome to my london tube route planner!!!")
    print("This program is able to plan the shortest route, in terms of number of stations, between two tube stations of your choice.")
    

def stations_string(tubes): #Returns a list of possible tube stations on separate lines
    tube_stations_string = ""
    for tube in tubes.keys():
        tube_stations_string += "{0}\n".format(tube)
    return tube_stations_string


def get_station_from(): #Returns the station that we want to leave from
    print("Here is a list of zone 1 tube stations that you can choose from.")
    tube_stations = hello.tubemap.keys()
    print(stations_string(hello.tubemap))
    response = input("Which station would you like to leave from today?")
    if response not in tube_stations:
        print("Unfortunately, this is not a station that we have in our program, please choose one from the list provided.")
        get_station_from()
    
    else:
        print(response)
    return response

def get_station_to(): #Returns the station that we want to go to
    print("Here is a list of zone 1 tube stations that you can choose from.")
    tube_stations = hello.tubemap.keys()
    print(stations_string(hello.tubemap))
    response = input("Which station would you like to reach today?")
    if response not in tube_stations:
        print("Unfortunately, this is not a station that we have in our program, please choose from the list provided.")
        get_station_to()
    
    else:
        print(response)
    return response

def program():
    greet()
    start = get_station_from()
    end = get_station_to()
    route = bfs(hello.tubemap, start, end)
    if route:
        print("A route exists!")
        print(route)
        return route
    else:
        print("Sorry, it does not look like a route exists between these two stations")
        return None

program()
