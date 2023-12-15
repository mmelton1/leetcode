#Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.
#
#He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, 
#he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
#Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

#4 / 10, 10 / 37, 20 / 96

n = 4
x = 0
y = 1
answer = 0
weeksAndDays = divmod(n, 7)
weeks = weeksAndDays[0]
days = weeksAndDays[1]

while weeks > 0:
    for x in range(7):
        print(f'{x}')
        x = x+y
        answer = answer+x
    weeks = weeks-1
    x = 0
    y = y+1
while days > 0:
    for x in range(days):
        x = x+y
        answer = answer+x
        days = days-1
