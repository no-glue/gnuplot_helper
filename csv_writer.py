import csv

class CsvWriter(object):
  def write_row(self, fileName, values):
    f = open(fileName, "wb")
    writer = csv.writer(f, delimiter = "\t")
    for value in values:
      writer.writerow(value)
