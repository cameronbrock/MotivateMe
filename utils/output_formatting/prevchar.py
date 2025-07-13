
#    Copyright 2025 Cameron Brock

#    This file is part of MotivateMe.

#    MotivateMe is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

#    MotivateMe is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License along with MotivateMe. If not, see <https://www.gnu.org/licenses/>. 


# Returns the index of the previous character in the string given
# by "ch. For example, prevchar("helloworld", 5, 'l') would return
# 3.
def prevchar(string, index,  ch):
	# For each index i from string[index] to string[0], if
	# string[i] == ch, return i.
	for i in range(index, 0, -1):
		if (string[i] == ch):
			return i

	# If no ch is found, raise an exception.
	raise Exception('Could not find '+ch+' before string['+str(index)+']')

