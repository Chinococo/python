name = str(input())
data = str(input())
y = data.split('/')[0]
m = data.split('/')[1]
d = data.split('/')[2]
print('{0} is born at year {1} month {2} day {3} in {4} family.'.format(name.split(' ')[0],y,m,d,name.split(' ')[1]),end='')
