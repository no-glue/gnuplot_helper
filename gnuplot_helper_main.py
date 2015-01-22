#!/usr/bin/env python

import argparse
import sys
import gnuplot_helper

if __name__ == "__main__":
  argv = sys.argv[1:]
  parser = argparse.ArgumentParser()
  parser.add_argument("-files", nargs='+')
  parser.add_argument("-out")
  parser.add_argument("-skipColumns")
  parser.add_argument("-terminal")
  args = parser.parse_args(argv)

  plot = gnuplot_helper.GnuplotHelper()
  plot.plot_multiple_xy(args.files, args.out, args.skipColumns, args.terminal)
