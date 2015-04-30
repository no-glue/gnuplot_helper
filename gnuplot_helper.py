#/usr/bin/env python

import csv
import numpy
import Gnuplot

class GnuplotHelper(object):
    def plot_multiple_xy(self, files, out, skipColumns, terminal, xlabel, ylabel):
        g = Gnuplot.Gnuplot(persist = 0)
        g("set xlabel '{0}'".format(xlabel))
        g("set ylabel '{0}'".format(ylabel))
        for i, f in enumerate(files):
            reader = csv.reader(open(f, "rb"), delimiter='\t')
            values = list(reader)
            print values
            array = numpy.array(values).astype("string")
            skipped = array[:, int(skipColumns):]
            print skipped
            floats = skipped.astype("float")
            data = Gnuplot.Data(floats[:,1], floats[:,0], with_="lp", title=f)
            data_points = Gnuplot.Data(floats[:,1], floats[:,0], using='1:2:(sprintf("(%d, %d)", $1, $2))', with_="labels offset 1")
            if i == 0:
                g.plot(data)
                g.replot(data_points)
                continue
            g.replot(data)
            g.replot(data_points)
        g.hardcopy(filename=out, terminal=terminal)
