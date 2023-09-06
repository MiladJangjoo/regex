import re
# milad = re.compile('[A-Z][a-z]+\s[A-Z][a-z]+,.([0-9][0-9]),\s([A-Z][a-z]+\s?[A-Z]?[a-z]+)')
# for line in data:
#     result = (milad.match(line))
#     print(f'Age: {result.group(1)}, Country: {result.group(2)}')
# for line in data:
#     if milad.match(line) == None:
#         print('Invalid record')
#     else:
#         result = (milad.match(line))
#         print(f'Age: {result.group(1)}, Country: {result.group(2)}')
# def one_st(my_li):
#     for item in my_li:
#         if milad.findall(item):
#             print(item)
#         else:
#             print('Invalid record')
# print(one_st(data))


with open('./user_records.txt') as f:
    data = f.readlines()
    print(data)


def one_st(my_li):
    milad = re.compile('[A-Z][a-z]+\s[A-Z][a-z]+,.([0-9][0-9]),\s([A-Z][a-z]+\s?[A-Z]?[a-z]+)')
    for line in my_li:
        if milad.match(line) == None:
            print('Invalid record')
        else:
            result = (milad.match(line))
            print(f'Age: {result.group(1)}, Country: {result.group(2)}')


print(one_st(data))