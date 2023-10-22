# .group can only be used with .search and .match methods.

import re
str1 = 'The Dr. Zkulla album is released on 2023-09-10.'
info = re.search(r'(\d{4})-(\d{2})-(\d{2})', str1)
# info
# <re.Match object; span=(36, 46), match='2023-09-10'>
info.group(0)
# '2023-09-10'
info.group(1)
# '2023'
info.group(2)
# '09'
info.group(3)
# '10'

# Use named groups
# Assign a name to a group: (?P<name>(regex))
str2 = 'New York, 10021'
city_info = re.search(r'(?P<city>[A-Za-z]+\s*[A-Za-z]*).*?(?P<zipcode>\d{5})', str2)
city_info.group('city')
# 'New York'
city_info.group('zipcode')
# '10021'
