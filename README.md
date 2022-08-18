# Maze Path Visualizer 
This is a portfolio/study project that finds pathways in given MxN (max 20x20) maze from start to end.

| Project Started | Last Update | Version |
| :-------------- | :---------- | :-----: |
| 31 May 2022     | 18 Aug 2022 | 1.02    |

# Table of Contents
1. [Description](#description)
2. [Installation and Usage](#installation-and-usage)
3. [Controls](#controls)
4. [Feature List](#feature-list)
5. [Display](#display)
6. [References](#references)


# Description
Maze Path Visualizer is an intermediate level project that I created by using various sources to study and display various computer science concepts.

Some of the practiced concepts are listed below: 

- **Abstract Data Structures**: Dictionary, Set, Queue, Stack
- **Search Algorithms**: Breath-first- Depth-first search 
- **Model**: Data driven, Event driven
- **Architecture**: Model-view-controller
- **Debugging**


# Installation and Usage
- **Installation**
    - Install Dependencies
        - Install [Python 3.xx](https://www.python.org/downloads/)
        - Install [Windows Curses](https://pypi.org/project/windows-curses/) 
            - Alternatively after installing python use `pip install windows-curses` on command line
    - Download [Maze Path Visualizer](https://github.com/kutaycoskuner/Project-MazePathVisualizer-Python/archive/refs/heads/main.zip)
- **Usage**
    - Open project folder in your console and use cli commands `py main.py` or `py main.py -gui`
    - It is possible to create your own input data and pass it to the program. Input needs to be defined as below:
        - Entry point of maze `0` exit is `1`
        - Obstacles defined by `#` path defined by `.`
        - You could use space between character for better human readability
        - Maze perimeters should be covered by obstacles and only one enter and exit point is allowed
        - Sample maze:
            ```
            # # # # # # # # # #
            0 . . . . # . . . #
            # # # # . # . . . #
            # . . . . # . . . #
            # . . . . # . # . #
            # . . . . . . # . #
            # . . . . . . # . #
            # # # # # # # # 1 #
            ```


# Controls
## | Command Line Interface (CLI) Controls
| Command | Description | Example Usage |
| :------ | :---------- | :------------ |
| `-t <seconds>`  | adding time deplay between maze progression steps | `py main.py -t 0.3` |
| `-d <path>`  | specify input data for the program            | `py main.py "/Data/maze2.txt"` |
| `-df`  | uses depth first method for search (default is breadth search)  | `py main.py -df` |
| `-cp [red\|green\|blue]`  | changing color of the drawn path between discrete options | `py main.py -cp "green"` |
| `-co [red\|green\|blue]`  | changing color of the obstacles between discrete options  | `py main.py -co "blue"` |
| `-gui`  | activates gui instead of command line interface            | `py main.py -gui` |

Example combined usage:  
```py main.py -d "/Data/maze2.txt"  -t 0.3 -df```


## | Graphical User Interface (GUI) Controls
| Button | Function |
| :----- | :------ |
| `Start` | goes to the first step of the path progression |
| `End` | goes to the last step of the path progression |
| `prev` | goes to the previous step of the currently visualized path |
| `next` | goes to the next step of the currently visualized path |
| `Play` | plays animation of path finding with the static delay of `0.2` sec |
| `Stop` | stops/pauses animation |
| `Browse` | allows user to select `.txt` formatted maze input |


# Feature List
- [x] `31-May-2022` Core algorithm MxN maze solving
- [x] `31-May-2022` CLI input option Data driven input
- [x] `31-May-2022` CLI input option animation time delay
- [x] `31-May-2022` CLI input option discrete search algorithm selection breadth first/depth first
- [x] `09-Jun-2022` CLI input option path and obstacle color alteration
- [x] `09-Jul-2022` CLI input option GUI activation
- [x] `10-Aug-2022` GUI animation; play/stop buttons
- [x] `13-Aug-2022` GUI animation slider
- [ ] Data input inside GUI


# Display
```
Version 1.00 cli
```  
![0.21 cli](display/version%201.00%20cli.gif)
```
Version 1.00 gui animation
```  
![0.16 animation](display/version%201.00%20animation.gif)
```
Version 1.00 gui display
```  
![0.16 gui](display/version%201.00%20gui.png)


# References
- Learning
    - Videos
        - [Youtube-Tech With Tim. 2022. 3 Mini Python Projects - For Intermediates](https://www.youtube.com/watch?v=txKBWtvV99Y)
        - [Youtube-Life in Code. 2019. Phython Tutorial: GUI Calculator with Model View Controller #2](https://www.youtube.com/watch?v=MwMRUr1a3YM)
        - [Youtube-freeCodeCamp.org. 2019. Tkinter Course - Create Graphic User Interfaces in Python Tutorial](https://www.youtube.com/watch?v=YXPyB4XeYLA&t=2740s)
    - Websites
        - Main Documentation Reference: [https://github.com/ocornut/imgui](https://github.com/ocornut/imgui)
    - Supervision/ Support
        - [Volkan İlbeyli](https://github.com/vilbeyli)
        - [Bugra Üvez](https://github.com/Liffrey)
- Libraries
    - [windows-curses 2.3.0](https://pypi.org/project/windows-curses/)

[Return to top](#maze-path-visualizer)
