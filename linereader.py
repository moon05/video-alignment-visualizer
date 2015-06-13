import csv


def configReader(filepath):
  """Method to read the config file in CSV format."""
  
  vidFileNames = []
  vidPaths = []
  protocolNames = []
  protocolPaths = []
  alignmentPaths = []
  # open the CSV file, and read data
  with open(filepath, "rb") as csvfile:
    reader = csv.DictReader(csvfile, dialect=csv.excel,
                          delimiter=",", quotechar="\"")
    for row in reader:
      print row
      vidFileNames.append(row["VideoFileName"])
      vidPaths.append(row["VideoFilePath"])
      protocolNames.append(row["ProtocolName"])
      protocolPaths.append(row["ProtocolPath"])
      alignmentPaths.append(row["AlignmentPath"])
  return vidFileNames, vidPaths, protocolNames, protocolPaths, alignmentPaths


def subReader(filePath):
  """Method for reading the protocol sentences from the protocol file"""

  text_file = open(filePath, "rt")
  lines = text_file.readlines()
  text_file.close()
  #readText = text_file.read().replace('\n','').replace('  ',' ')
  Titles = []
  for line in lines:
    line = line.lstrip().rstrip()
    if len(line) == 0:
      continue
    Titles.append(line)
  return Titles


##This method takes a PATH(of the alignment file) and returns all the data in three lists
def timingReader(filePath):
  """Method for reading the index, start and end times for each sentence from a Alignment file"""

	AL_file = open(filePath, "r")
	AL_file.readline()
	readCols = []
	sentence_index = []
	start_time = []
	end_time = []
	for lines in AL_file:
		readCols.append(lines)
	for cols in readCols:
		rows = cols.split(',')
		sentence_index.append(rows[0])
		start_time.append(rows[1])
		end_time.append(rows[2].replace('\n',''))

	print type(sentence_index[0])

	finalStartTime = []
	finalEndTime = []
	finalIndex = []
	for i in range(len(start_time)):
		finalIndex.append(int(sentence_index[i]))
	for i in range(len(start_time)):
		finalStartTime.append(float(start_time[i]))
	for i in range(len(end_time)):
		finalEndTime.append(float(end_time[i]))


	return finalIndex, finalStartTime, finalEndTime

