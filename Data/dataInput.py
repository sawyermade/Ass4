import sys

def getData(data_list):
	data_list.clear()
	# [data_list.append(int(i)) for i in sys.argv[1:]]
	# data_list[:] = [int(i) for i in sys.argv[1:]]
	for i in sys.argv[1:]: data_list.append(int(i))

def main():
	data_list = [1, 2, 3]
	getData(data_list)
	print(f'You entered {len(data_list)} integers: {data_list}')

if __name__ == '__main__':
	main()