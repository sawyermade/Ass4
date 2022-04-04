import random

def makeTen(data_list):
	# if len(data_list) < 10:
	# 	[data_list.append(random.randint(-5, 5)) for i in range(10 - len(data_list))]
	while len(data_list) < 10:
		data_list.append(random.randint(-5, 5))

def findUnique(data_list):
	return [i for i in set(data_list) if data_list.count(i) == 1]

def main():
	data_list = [1, 2, 2]
	# data_list = [1, 2, 3, 3, 4, 4, 5, 5, 6, 7]
	# data_list = [1, 2, 3, 3, 4, 4, 5, 5, 6, 7, 1]
	print(f'You entered {len(data_list)} integers: {data_list}')

	len_diff = 10 - len(data_list)
	if len_diff > 0: 
		makeTen(data_list)
		print(f'After {len_diff} random integers are appeneded: {data_list}')
	else:
		print(data_list)

	unique_list = findUnique(data_list)
	print(f'These have no duplicates: {unique_list}')


if __name__ == '__main__':
	main()