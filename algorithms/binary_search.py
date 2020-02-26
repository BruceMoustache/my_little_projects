counter = 0

def binary_search(element, array):
	global counter

	min_limit = 0
	max_limit = len(array)

	while True:
		index = (min_limit + max_limit) // 2
		hit = array[index]

		counter += 1

		if hit == element:
			break
		elif element < hit:
			max_limit = index - 1
		elif hit < element:
			min_limit = index + 1
	return index


a = list(range(10, int(input('List len: '))))
n = int(input('Number to find: '))

print(binary_search(n, a))
print(f'counter: {counter}')

