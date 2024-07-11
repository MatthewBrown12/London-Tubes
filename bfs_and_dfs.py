# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 16:05:54 2024

@author: matth
"""

def bfs(graph, start_vertex, end_vertex): #Performs a breadth first search on the graph
    path = [start_vertex]
    vertex_and_path = [start_vertex, path]
    queue = [vertex_and_path]
    visited = set()
    while queue:
        current_vertex, path = queue.pop(0)
        visited.add(current_vertex)
        neighbours = []
        lines = []
        for station in graph[current_vertex]:
            stations = station.split(' - ')
            neighbours.append(stations[0])
            lines.append(stations[1])
        for i in range(len(neighbours)):
            if neighbours[i] not in visited:
                if neighbours[i] == end_vertex:
                    return path + [neighbours[i] + " - " + lines[i]]
                else:
                    queue.append([neighbours[i], path + [neighbours[i] + " - " + lines[i]]])

def dfs(graph, start_vertex, end_vertex, visited = None): #Performs a depth first search on the graph
    if visited == None:
        visited = []
    
    visited.append(start_vertex)
    
    if start_vertex == end_vertex:
        return visited
    
    else:
        for neighbor in graph[start_vertex]:
            if neighbor not in visited:
              path = dfs(graph, start_vertex, end_vertex, visited)
            
              if path:
                  return path