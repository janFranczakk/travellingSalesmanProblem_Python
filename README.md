
# Travelling Salesman Problem in Python

Simple program that finds shortest route between point on a map/graph using brute force method. Writed in Python language.



## Used imports

- itertools
- math
- random
- time
- matplotlib.pyplot
- from threading Thread

## How it works

- Program gives a random location to the 9 points on the graph
- Program using multiThreading to help with brute forcing every possibility of connection between points
- Console prints Shortes distance, Optimal route and the number of seconds the program took to calculate the shortest path
- Console shows a graph that shows user connected points in shortest way



## Screenshots

### Console
![console](https://github.com/janFranczakk/travellingSalesmanProblem_Python/blob/main/Screenshots/ecf340de7c04279ffcb526c3c15742c4.png?raw=true)

### Graphs
![firstGraph](https://github.com/janFranczakk/travellingSalesmanProblem_Python/blob/main/Screenshots/0378de38b6fb563fa5f9113d6e48a415.png?raw=true)

![secondGraph](https://github.com/janFranczakk/travellingSalesmanProblem_Python/blob/main/Screenshots/4508801cdbeed09d4238c1531669856e.png?raw=true)

![thirdGraph](https://github.com/janFranczakk/travellingSalesmanProblem_Python/blob/main/Screenshots/b10ef715242056a128b8e4f1527cfa76.png?raw=true)

![fourthGraph](https://github.com/janFranczakk/travellingSalesmanProblem_Python/blob/main/Screenshots/d81255279b2f7c03a3d25c7e0b6bf651.png?raw=true)

## Multithreading
### One thread
[<Thread(Thread-1, started 7648)>, <Thread(Thread-2, initial)>, <Thread(Thread-3, initial)>, <Thread(Thread-4, initial)>, <Thread(Thread-5, initial)>, <Thread(Thread-6, initial)>, <Thread(Thread-7, initial)>, <Thread(Thread-8, initial)>]
### Two threads
[<Thread(Thread-1, started 7648)>, <Thread(Thread-2, started 12628)>, <Thread(Thread-3, initial)>, <Thread(Thread-4, initial)>, <Thread(Thread-5, initial)>, <Thread(Thread-6, initial)>, <Thread(Thread-7, initial)>, <Thread(Thread-8, initial)>]
### Three threads
[<Thread(Thread-1, started 7648)>, <Thread(Thread-2, started 12628)>, <Thread(Thread-3, started 5152)>, <Thread(Thread-4, initial)>, <Thread(Thread-5, initial)>, <Thread(Thread-6, initial)>, <Thread(Thread-7, initial)>, <Thread(Thread-8, initial)>]
### Four threads
[<Thread(Thread-1, started 7648)>, <Thread(Thread-2, started 12628)>, <Thread(Thread-3, started 5152)>, <Thread(Thread-4, started 10264)>, <Thread(Thread-5, initial)>, <Thread(Thread-6, initial)>, <Thread(Thread-7, initial)>, <Thread(Thread-8, initial)>]
### Five threads
[<Thread(Thread-1, started 7648)>, <Thread(Thread-2, started 12628)>, <Thread(Thread-3, started 5152)>, <Thread(Thread-4, started 10264)>, <Thread(Thread-5, started 14688)>, <Thread(Thread-6, initial)>, <Thread(Thread-7, initial)>, <Thread(Thread-8, initial)>]
### Six threads
[<Thread(Thread-1, started 7648)>, <Thread(Thread-2, started 12628)>, <Thread(Thread-3, started 5152)>, <Thread(Thread-4, started 10264)>, <Thread(Thread-5, started 14688)>, <Thread(Thread-6, started 10332)>, <Thread(Thread-7, initial)>, <Thread(Thread-8, initial)>]
### Seven threads
[<Thread(Thread-1, started 7648)>, <Thread(Thread-2, started 12628)>, <Thread(Thread-3, started 5152)>, <Thread(Thread-4, started 10264)>, <Thread(Thread-5, started 14688)>, <Thread(Thread-6, started 10332)>, <Thread(Thread-7, started 7900)>, <Thread(Thread-8, initial)>]
### Eight threads
[<Thread(Thread-1, started 7648)>, <Thread(Thread-2, started 12628)>, <Thread(Thread-3, started 5152)>, <Thread(Thread-4, started 10264)>, <Thread(Thread-5, started 14688)>, <Thread(Thread-6, started 10332)>, <Thread(Thread-7, started 7900)>, <Thread(Thread-8, started 7012)>]

