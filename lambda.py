my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

squares = [x**2 for x in range(1,11)]
print squares
print filter(lambda x: x in range(30,71), squares)


movies = {
	"Monty Python and the Holy Grail": "Great",
	"Monty Python's Life of Brian": "Good",
	"Monty Python's Meaning of Life": "Okay"
}

print   movies.items()