#/usr/bin/env python

import csv
import numpy
import Gnuplot

class Gnuplot(object):
    def plot_multiple_xy(files, skipColumns, delim):
        g = Gnuplot.Gnuplot(persist = 0)
        for file in files:
            reader = csv.reader(open(file, "rb"), delimiter=delim)
            values = list(reader)
            array = numpy.array(values).astype("string")
            array = array[:, skipColumns:]
            array = array.astype("float")

