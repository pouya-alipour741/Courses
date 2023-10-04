import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped): #for these charactors you need to use \ as escape function because they are builtin in pythons
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
cat
mat
pat
bat
'''


sentence = 'Start a sentence and then bring it to an end'
#
# pattern = re.compile(r'end$')
# matches = pattern.finditer(sentence)
# for match in matches:
#     print(match)

# pattern_2 = re.compile(r'[^a-zA-Z]')
# matches_2 = pattern_2.finditer(text_to_search)
# for match in matches_2:
#     print(match)

# pattern_3 = re.compile(r'[89]\d\d[-.]\d\d\d.\d\d\d\d')
# matches_3 = pattern_3.finditer(text_to_search)
# for match in matches_3:
#     print(match)

# pattern_4 = re.compile(r'[^b]at')
# matches_4 = pattern_4.finditer(text_to_search)
# for match in matches_4:
#     print(match)

# pattern_5 = re.compile(r'\d{3}.\d{3}.\d{4}')    ##3digits then 3digits then 4digits
# matches_5 = pattern_5.finditer(text_to_search)
# for match in matches_5:
#     print(match)

# patter_6 = re.compile(r'Mr\.?\s[A-Z]\w*')
# matches_6 = patter_6.finditer(text_to_search)
# for match in matches_6:
#     print(match)

# pattern_7 = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')   ###(rs) means find 'rs'  ,[rs] means find 'r' 's'
# matches_7 = pattern_7.finditer(text_to_search)
# for match in matches_7:
#     print(match)

# pattern_7 = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
# matches_7 = pattern_7.findall(text_to_search)  # findall method find all the ones in the groups ,if there are no groups () then it bring matches as strings
# for match in matches_7:
#     print(match)

# pattern = re.compile(r'[89][0][0][-]555[-]\d\d\d\d')
# with open('data.txt','r') as f:
#     contents = f.read()
#     matches = pattern.finditer(contents)
#     for match in matches:
#         print(match)

# pattern = re.compile(r'Start')
# matches = pattern.match(sentence) #match method brings the first match at the begining of a string so no need for a for loop
# print(matches)

# pattern = re.compile(r'sentence')
# matches = pattern.search(sentence) #search method brings the first match
# print(matches)

# pattern = re.compile(r'start', re.I)  #re.I = re.IGNORECASE same as [Ss][Tt][Aa][Rr][Tt]
#
# matches = pattern.search(sentence)
#
# print(matches)


