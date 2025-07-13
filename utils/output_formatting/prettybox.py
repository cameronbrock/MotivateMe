
#    Copyright 2025 Cameron Brock

#    This file is part of MotivateMe.

#    MotivateMe is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

#    MotivateMe is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License along with MotivateMe. If not, see <https://www.gnu.org/licenses/>. 


from utils.output_formatting.widthsplit import widthsplit
import emoji
import random
import math


num_vert_buffer_chars = 1
num_side_buffer_chars = 5

sparkle = emoji.emojize(':sparkles:')
sparkle_size = 2

# Prints a line of the box output without text. Just whitespace and
# some sparkles.
def print_width_whitespace(width):
	sparkle_location = math.floor(random.randint(0, width))
	width_whitespace = ' '*sparkle_location + sparkle + ' '*(width - sparkle_location - sparkle_size)
	print('\u2551', width_whitespace, '\u2551', sep='')

# Prints a given string inside a pretty-looking unicode box.
def print_msg(msg, author, width):
	msg_lines = widthsplit(msg, width)
	width = 2*num_side_buffer_chars + width

	# Print the top of the box
	print('\u2554', '\u2550'*width, '\u2557', sep='')

	# Print the extra buffer space above the string.
	for i in range(num_vert_buffer_chars):
		print_width_whitespace(width)

	# For each line in the message, print it surrounded by box lines.
	for msg_line in msg_lines:
		print('\u2551', end='')
		print(' '*num_side_buffer_chars, end='')
		print(msg_line, end='')
		print(' '*(width-len(msg_line)-2*num_side_buffer_chars), end='')
		print(' '*num_side_buffer_chars, end='')
		print('\u2551')

	# Now it's time to print the author. Add an extra space.
	print_width_whitespace(width)

	# Now add the author, making sure to right-justify it.
	author_str = '- ' + author + '  '
	print('\u2551', ' '*(width - len(author_str)), author_str, '\u2551', sep='')

	# Now print an extra buffer space at the bottom
	for i in range(num_vert_buffer_chars):
		#print('\u2551', ' '*width, '\u2551', sep='')
		print_width_whitespace(width)

	# Print the bottom of the box.
	print('\u255A', '\u2550'*width, '\u255D', sep='')


