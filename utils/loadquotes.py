
#    Copyright 2025 Cameron Brock

#    This file is part of MotivateMe.

#    MotivateMe is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

#    MotivateMe is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License along with MotivateMe. If not, see <https://www.gnu.org/licenses/>. 


import os

# Loads the entire contents of the quotes.jsonl file into the
# program's memory, and returns the list of quotes as an array
# of strings.

# Get the path of the current directory.
dirname = os.path.dirname(os.path.abspath(__file__))

# Add the location of the quotes file to dirname/
# i.e. make the filepath <current directory>/quotes.jsonl
filepath = os.path.join(dirname, "quotes.jsonl")

# Now open the file and load all of its data into the array.
def loadquotes():
	quotesfile = open(filepath, "r")
	quoteslist = []

	for quote in quotesfile:
		quoteslist.append(quote)
	
	return quoteslist


