
#    Copyright 2025 Cameron Brock

#    This file is part of MotivateMe.

#    MotivateMe is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

#    MotivateMe is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License along with MotivateMe. If not, see <https://www.gnu.org/licenses/>. 


import math
from utils.output_formatting.prevchar import prevchar

# Splits a string into <width>-long substrings, but doesn't cut any
# word in that string in half. Instead, it finds the most recent
# whitespace character and splits it by that index.
def widthsplit(string, width):

	# numlines is the number of lines the string will be split
	# into.
	numlines = math.ceil(len(string) / width)

	# Initialize the list of substrings.
	substring_list = []

	# While the string is longer than the given width, look for
	# the width-th character in the string and then look for the
	# index of the previous whitespace character. Then add the entire
	# string up to that point to the substring_list, and remove it
	# from the string. Keep doing this until the string is too short
	# to be cut up any longer, and then just append whatever the
	# remainder is to the list.
	while (len(string) != 0):
		if (len(string) <= width):
			substring_list.append(string)
			break
		prev_whitespace_idx = prevchar(string, width, ' ')
		substring_list.append(string[:prev_whitespace_idx])
		string = string[prev_whitespace_idx+1:]

	# Finally, return the resulting list.
	return substring_list


