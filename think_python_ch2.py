# Homework assignment Chapter 2, Exercise 4

print "Ex. 4.1, ANSWER:"
r = 5
pi = 3.14
x = 4.0/3.0
y = x * pi
print y * r**3, "volume of sphere with radius 5"

print "Ex. 4.2, ANSWER:"
bookstore_price = 24.95 * (1-.4)
first_copy = 3 + bookstore_price
add_copy = .75 + bookstore_price
wholesale = first_copy + (59 * add_copy)
print wholesale, "cost of books"

print "Ex. 4.3, ANSWER:"
import datetime
a = datetime.datetime(100,1,1,6,52)
easy_pace = (8 * 60) + 15 # time in seconds
tempo_pace = (7 * 60) + 12 # time in seconds
total_run_seconds = (2 * easy_pace) + (3 * tempo_pace) # total run time in seconds
b = a + datetime.timedelta(0, total_run_seconds) # days, seconds, then other fields.
print "Gets home by", b.time()


