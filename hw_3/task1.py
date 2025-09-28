#task1
name = 'Olya'
day = 'Friday'

print('Good day' + ' ' + name + '!' + ' ' + day + ' ' + 'is a perfect day to learn some python')

print(f'Good day {name}! {day} is a perfect day to learn some python')

message = 'Good day {}! {} is a perfect day to learn some python'
print(message.format(name, day))

print('Good day {0}! {1} is a perfect day to learn some python' .format(name, day))

print('Good day %s! %s is a perfect day to learn some python' % (name, day))