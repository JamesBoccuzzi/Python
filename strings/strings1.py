colors = ['red','blue','yellow','green']
print(colors)

joined_colors = ', '.join(colors)
print(joined_colors)

time = '12:30:PM'
print(time)

parts = time.split(':')
print(parts)

message = 'I love my cat'
print(message)

message_replace = message.replace('cat','dog')
print(message_replace)

name = 'James'
print(name)

upper_name = name.upper()
print(upper_name)

lower_name = name.lower()
print(lower_name)

letters = 'ABCDEFG'
print(letters.startswith('ABC'))

letters = 'ABCDEFG'
print(letters.endswith('DGF'))

text = 'Hello : How are you'
print(text.split(':'))

numbers = '1,2,3,4,5,6,7,8,9,10'
print(numbers)

numbers_removed = numbers.removeprefix('1,2,3,4,5,')
print(numbers_removed)
