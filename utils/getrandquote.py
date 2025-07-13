
#    Copyright 2025 Cameron Brock

#    This file is part of MotivateMe.

#    MotivateMe is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

#    MotivateMe is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License along with MotivateMe. If not, see <https://www.gnu.org/licenses/>. 


from utils.loadquotes import loadquotes
import json
import random

# Get an array of quote JSON strings from loadquotes(). At random,
# select one element of that array, and then convert that JSON string
# into a Python dictionary object. Finally, return that object.
def getrandquote():
	quoteslist = loadquotes()
	quote_string = random.choice(quoteslist)
	quote_obj = json.loads(quote_string)	
	return quote_obj
	
