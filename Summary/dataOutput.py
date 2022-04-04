import sys
try:
	sys.path.append('../Analysis')
	import check
except:
	sys.path.append('Analysis')
	import check

def printSummary(data_list):
	unique_list = check.findUnique(data_list)
	non_unique_list = set(data_list) - set(unique_list)
	print('Summary:\n')
	for i in unique_list: print(f'{i} (1)\n')
	for i in non_unique_list: print(f'{i} ({data_list.count(i)})\n')
	# [print(f'{i} (1)\n') for i in unique_list]
	# [print(f'{i} ({data_list.count(i)})\n') for i in set(data_list) if i not in unique_list]


def main():
	data_list = [1, 2, 3, 3, 4, 4, 5, 5, 5, 4]
	print(data_list)
	printSummary(data_list)

if __name__ == '__main__':
	main()