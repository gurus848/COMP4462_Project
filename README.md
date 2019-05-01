# COMP4462_Project Spring 2019

Team “To be named”:
SENTHIL Guru Sarjith, SUN David, GUPTA Ayush, GUPTA Abhishek

Github Link: https://github.com/gurus848/COMP4462_Project.git

Tasks Research Document: https://docs.google.com/document/d/15AqlrcBQ0bR-ddqEdHO9ZM9beTVNrfiwokF32XI-XGs/edit

First Presentation: https://docs.google.com/presentation/d/1ALDNCVMtG0HbxWYJ_NJI8oeof2YkVC0IL685L6oCJGI/edit?usp=sharing

Possible Tasks Document: https://docs.google.com/document/d/1bAz7c6TN-Iy2XvFkMa9ZkjPYqcR8q04DqQmXA7cViUg/edit?usp=sharing

Drive link for data: https://drive.google.com/open?id=1oya6IbQI2ros8PA0arl0D92fUNEYjKvz

Remember to add the data files from the Google Drive link to the data folder before trying to run the code.

Please install dependencies before running the code. All of the paths used are relative paths.

# Progress

Please update the progress here if you start/continue working on a task

## Task 1

 <ins>Visualization 1: Circle Animation<ins>

Guru started working on it. Currently works OK, the placement of the circles in the animation could be improved. Could also play around with the animation duration, and maybe encode the ranking in some way other than area.

Abhishek is working on the positioning of the circles and changes in area.

<ins>Visualization 2: Theme River<ins>


Guru started working on it. Needs to be improved, if you use a large number of regions it does not look that great. Also need to figure out where to place labels for the rivers properly.

David will rewrite it in D3. 
UPDATE:

Done making the themeriver in D3. Some issues:
1. For D3 to make theme rivers, i need to normalize the streams. Is that okay, or should I change the y axis to reflect number of streams?
2. We should find good color schemes, for his course

## Task 2

<ins>Visualization 1: Parallel Coordinates <ins>

Ayush completed it.

<ins>Visualization 2: Edge bundling <ins>

David is working on it. Threshold is ok, but hovering is going to be hard since we use html canvas. Can I just make selector buttons?

## Task 3

<ins>Visualization 1: Line Graph Animation <ins>

Guru worked on it. Mostly done, only problem is that the colors of the song lines change sometimes, but this should be fixable. Another problem is that sometimes songs enter the charts from the bottom, and this looks a bit trippy. 

<ins>Visualization 2: Heatmap <ins>

Guru worked on it. HK is pretty small in the current heatmap, don't know any way currently to just make HK look larger. Could play around with how the ranking change speed is calculated to make it more interesting.

More or less finished.

## Task 4

<ins>Visualization 1: Artist-Country Node Link <ins>

Guru worked on it. Could play around and try to make it look nicer, maybe use country flags instead of just squares, can be done in plotly but more complex. Could maybe do higher level clusterings based on genre/continent. Layout is pretty good right now IMO, but could always try to improve it. 

Pretty much finished.

<ins>Visualization 2: Heatmap <ins>

Ayush worked on it. Guru mostly finished it, could maybe play around with different metrics to determine artist popularity. 

<ins>Visualization 3: Growth Rings <ins>

Abhishek is working on it

## Extra Task

<ins> Correlation heatmap <ins>

Add the top position reached, and the no. of days in the rankings as features of each song for it to potentially be more interesting.
David is working on it.
