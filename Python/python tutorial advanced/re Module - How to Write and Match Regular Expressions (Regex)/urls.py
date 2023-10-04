import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

# pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')     ##we have made 3 groups here
# #
# matches = pattern.finditer(urls)
# for match in matches:
#     print(match)
#     print(match.group(3))     ##.group relate to each () we used in line 10


# pattern = re.compile(r'https?://(www.)?(\w+)(\.\w+)')
#
# subbed_urls = pattern.sub(r'\2\3', urls)      ## \2 here means group 2 and so on
# print(subbed_urls)
# #
#
# matches = pattern.finditer(urls)
#
# for match in matches:
#     print(match)
#     print(match.group(3))