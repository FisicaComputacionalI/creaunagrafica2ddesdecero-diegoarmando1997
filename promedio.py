# lineplot.py
import numpy as np
import pylab as pl
# Make an array of x values
x = [1,2,3,4]
pl.xlabel ('Semestre')
# Make an array for y values for each x value
y = [8.66,8.33,8.50,8.50]
pl.ylabel ('Calificacion')
# Use pylab to plot x and y
pl.plot(x,y, 'bs')
# Show the plot on the screen
pl.savefig('prom.png')