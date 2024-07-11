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
    
    tube_stations = hello.tubemap.keys()
    
    response = input("Which station would you like to leave from today?")
    while response not in tube_stations:
        print("Unfortunately, this is not a station that we have in our program, please choose one from the list provided.")
        response = input("Which station would you like to leave from today?")
    

    return response

def get_station_to(): #Returns the station that we want to go to
    
    tube_stations = hello.tubemap.keys()
    response = input("Which station would you like to reach today?")
    while response not in tube_stations:
        print("Unfortunately, this is not a station that we have in our program, please choose from the list provided.")
        response = input("Which station would you like to leave from today?")
    
    return response

def program():
    greet()
    print("Here is a list of zone 1 tube stations that you can choose from.")
    print(stations_string(hello.tubemap))
    start = get_station_from()
    end = get_station_to()
    route = bfs(hello.tubemap, start, end)
    if route:
        print("A route exists!")
        split_route(route)
        print("You have reached your destination!!!")
    else:
        print("Sorry, it does not look like a route exists between these two stations")
    
    play_again = input("Would you like to see another route? y/n")
    if play_again == "y":
        program()
    else:
        print("Thank you for using my program. Hope to see you again!!!")



def split_route(route):
    length = len(route) - 1
    print("There are {0} stops on this route.".format(length))
    i = 1
    stations = []
    lines = []
    while i < len(route):
        station = route[i].split(' - ')
        stations.append(station[0])
        lines.append(station[1])
        i += 1
    count = 1
    queue = lines[0]
    lines.pop(0)
    while len(lines) > 0:
        if lines[0] == queue:
            count += 1
            lines.pop(0)
        else:
            print("Stay on the {} line for {} stops.".format(queue, count))
            for i in range(count):
                print(stations[i])
            print("Get off the {} line at {}.".format(queue, stations[count-1]))
            queue = lines[0]
            print("Switch to the {} line.".format(queue))
            lines.pop(0)
            stations = stations[count:]
            count = 1
    print("Stay on the {} line for {} stops.".format(queue, count))
    for i in range(count):
        print(stations[i])
    print("Get off the {} line.".format(queue))
program()
