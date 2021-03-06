from org.transcrypt.stubs.browser import *
import random

def gen_random_int(number, seed):
	random.seed(seed)
	array = list(range(number))
	random.shuffle(array)
	return array

def generate():
	number = 10
	seed = 200

	# call gen_random_int() with the given number and seed
	# store it to the variable array

	array = gen_random_int(number, seed)

	# convert the items into one single string 
	# the number should be separated by a comma
	# and a full stop should end the string.

	array_str = array.join(",") + "."

	# This line is to placed the string into the HTML
	# under div section with the id called "generate"	
	document.getElementById("generate").innerHTML = array_str


def bubble_sort(array):
	n = len(array)
	swapped = True
	count = 0
	while swapped:
		swapped = False
		new_n = 0
		for i in range(1, n):
			second = array[i]
			first = array[i-1]
			count += 1
			if second < first:
				array[i], array[i-1] = first, second
				swapped = True
				new_n = i

		n = new_n
	print(f"Array in bubble_sort: {array} Count: {count}")

def insertion_sort(array):
	n = len(array)
	count = 0

	# Loop through (n-1) times in outer loop
	for outer in range(1, n):
		temp = array[outer]
		idx = outer 
		
		# Remember: You are NOT shfiting the number yet. Hence, compare with temp
		while idx > 0 and temp < array[idx-1]:
			count += 1
			# Shift right
			array[idx] = array[idx-1]
			# Move left
			idx -= 1
		
		# Save temp element to its final position
		array[idx] = temp

	print(f"Array in insertion_sort: {array} Count: {count}")

def sortnumber1():
	'''	This function is used in Exercise 1.
		The function is called when the sort button is clicked.

		You need to do the following:
		- get the list of numbers from the "generate" HTML id, use document.getElementById(id).innerHTML
		- create a list of integers from the string of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	pass

	array = document.getElementById("generate").innerHTML

	array_int = [int(i) for i in array[:-1].split(",")]

	insertion_sort(array_int)

	array_str = [str(i) for i in array_int]
	
	document.getElementById("sorted").innerHTML = array_str

def sortnumber2():
	'''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.

		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to 
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
	value = document.getElementsByName("numbers")[0].value
	

	# Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty")
		return

	# Your code should start from here
	# store the final string to the variable array_str
	array_int = [int(i) for i in value.split(",")]
	bubble_sort(array_int)

	array_str = [str(i) for i in array_int]

	document.getElementById("sorted").innerHTML = array_str


