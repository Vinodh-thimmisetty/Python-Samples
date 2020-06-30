import sys
from urllib.request import urlopen

def fetch_words(url='http://sixty-north.com/c/t.txt', border='-'):
	"""
		Args:
			'http://sixty-north.com/c/t.txt'
		Return:
			List of Words
	"""
	line = border * len(url)
	print(line)
	story = urlopen(url)
	story_words = []
	for line in story:
		line_words = line.decode('utf8').split()
		for word in line_words:
			story_words.append(word)
	story.close()
	print(line)
	return story_words;

def print_items(items):
	for item in items:
		print(item)

def main(url='http://sixty-north.com/c/t.txt'):
	print_items(fetch_words(url))

def istrcmp(first, second, fn = lambda s: s.upper()):
	return fn(first) == fn(second)

def apply(func, first):
	return func(first)


def sumOfItems(items):
	sum=items[0]
	for val in range(1, len(items)):
		sum += items[val]
	return sum

def prodOfItems(items):
	prod=items[0]
	for val in range(1, len(items)):
		prod *= items[val]
	return prod

def factorial(n):
	if n <= 1 : return 1;
	return prodOfItems([n, factorial(n-1)])

def reverse(items):
	size=len(items)
	newList=[]
	for val in range(0, size):
		newList.append(items[size-val-1])
	return newList

def minAndMax(items):
	minVal,maxVal=items[0],items[0]
	for val in items:
		if val < minVal:
			minVal = val
		if val > maxVal:
			maxVal = val
	return (minVal, maxVal)

def cumSum(items):
	curSum=items[0]
	newList=[curSum]
	for val in range(1, len(items)):
		curSum += items[val]
		newList.append(curSum)
	return newList


def uniqueNumbers(items):
	newList = []
	for i in range(0, len(items)):
		exists=True
		for j in range(0, len(newList)):
			if items[i] == newList[j]:
				exists= False
				break
		if exists:
			newList.append(items[i])
	return newList

def uniqueTexts(items, fn=lambda x: x.lower()):
	newList = []
	for i in range(0, len(items)):
		exists=True
		for j in range(0, len(newList)):
			if fn(items[i]) == fn(newList[j]):
				exists= False
				break
		if exists:
			newList.append(items[i])
	return newList

def dups(items):
	newList=[]
	for i in range(0, len(items)):
		sameVal=False
		for j in range(0, i):
			if items[i] == items[j]:
				sameVal=True
				break
		exists=True
		for j in range(0, len(newList)):
			if items[i] == newList[j]:
				exists= False
				break
		if sameVal and exists:
			newList.append(items[i])
	return newList

def group(items, size):
	quotient = int(len(items)/size)
	remainder = len(items)%size
	totalLists = 0
	if remainder:
		totalLists = quotient + 1
	else:
		totalLists = quotient

	print(len(items), size, quotient, remainder, totalLists)
	lists = [[]] * totalLists
	for val in range(0, totalLists):
		lists[val] = items[val*size:val*size+size]
	return lists

def customSort(items, fn):
	items.sort(key = fn)
	return items

def fileRead(file):
	with open(file) as fs:
		s=fs.readline()
		while s:
			print(s, end='', file=sys.stdout)
			s=fs.readline()

def fileStats(file):
	print(f'Lines = {open(file).readlines()}')
	print(f'noOfLines = {len(open(file).readlines())}')
	print(f'Words = {open(file).read().split()}')
	print(f'noOfWords = {len(open(file).read().split())}')
	print(f'Chars = {open(file).read()}')
	print(f'noOfChars = {len(open(file).read())}')
	lines = open(file).readlines()
	print(lines)
	for line in range(0, len(lines)):
		print(lines[len(lines)-line-1])


def pythagoranTheorem(n):
	return [ (x,y,z) for x in range(1,n) for y in range(x,n) for z in range(y,n) if x**2 + y**2  == z **2]


def zip(first, second):
	return [ (x,y) for i,x in enumerate(first) for j,y in enumerate(second) if i ==j]


def square(items, map, filter):
	return [ map(val) for val in items if filter(val)]

def triplets(n):
	return [(x,y,z) for x in range(1, n) for y in range(x,n) for z in range(y,n) if x + y == z]

from math import log
def convert(s):
	try:
		print(f'Try Logic')
		# IndentationError, SyntaxError, NameError should be fixed and not caught
	except KeyError as ke:
		print('Key Error')
	except TypeError as te:
		print('Type Error')
	except (EOFError, OSError) as e:
		log(f'Other Errors {e!r}')
		raise
	finally:
		print('Cleanup')


from itertools import islice, count
from pprint import pprint as pp

if __name__ == '__main__':
	# main(sys.argv[1])
	print(sumOfItems([1,2,3,4,5]))
	print(sumOfItems(['Hello', 'Vinodh', 'How', 'are', 'you?']))
	print(prodOfItems([1,2,3,4,5]))
	print(factorial(5))
	print(reverse([1,2,3,4,5]))
	print(reverse(reverse([1,2,3,4,5])))
	print(minAndMax([1,12,3,-4,5]))
	print(minAndMax(['Hello', 'Vinodh', 'How', 'are', 'you?']))

	print(cumSum([1,2,3,4,5]))
	print(cumSum(['Hello', 'Vinodh', 'How', 'are', 'you?']))

	print(uniqueNumbers([1, 2, 1, 3, 3, 2, 5, 5]))
	print(dups([1, 2, 1, 3, 3, 2, 5, 5]))
	print(uniqueNumbers([1,1,1,1,1,12,2,2,2,2,24,2,5,5,5,6,2]))
	print(dups([1,1,1,1,1,12,2,2,2,2,24,2,5,5,5,6,2]))

	print(group([1, 2, 3, 4, 5, 6, 7, 8, 9,10], 3))
	print(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))
	print(group(['Hello', 'Vinodh', 'How', 'are', 'you?'], 3))

	print(uniqueTexts(["python", "java", "Python", "Java"]))
	print(customSort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'], lambda a: a.split(".")[1]))
	
	fileStats('foo.txt')
	print(pythagoranTheorem(25))
	print(zip([1, 2, 3], ["a", "b", "c"]))
	print(square([1,2,3,4,5], lambda x: x**2, lambda x: x%2==0))
	print(triplets(5))