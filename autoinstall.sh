
#    Copyright 2025 Cameron Brock

#    This file is part of MotivateMe.

#    MotivateMe is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

#    MotivateMe is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License along with MotivateMe. If not, see <https://www.gnu.org/licenses/>. 


# Clone the repository into /usr/local/src/motivateme
cd /usr/local/src/
git clone github.com/cameronbrock/MotivateMe

# Add execute permissions for all users.
cd /usr/local/src/motivateme
chmod 755 motivateme

# Create a symbolic link in /usr/local/bin
ln -s /usr/local/src/motivateme/motivateme /usr/local/bin/motivateme
cd /usr/local/bin/motivateme
chmod 755 motivateme

