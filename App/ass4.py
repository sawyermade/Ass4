import sys
try:
	sys.path.append('../Data')
	sys.path.append('../Analysis')
	sys.path.append('../Summary')
	import dataInput
	import check
	import dataOutput
except:
	sys.path.append('Data')
	sys.path.append('Analysis')
	sys.path.append('Summary')
	import dataInput
	import check
	import dataOutput

def main():
	data_list = []
	dataInput.getData(data_list)
	print(f'You entered {len(data_list)} integers: {data_list}\n')

	len_diff = 10 - len(data_list)
	if len_diff > 0: 
		check.makeTen(data_list)
		print(f'After {len_diff} random integers are appeneded: {data_list}\n')
	else:
		print(f'{data_list}\n')

	unique_list = check.findUnique(data_list)
	print(f'These have no duplicates: {unique_list}\n')

	dataOutput.printSummary(data_list)

if __name__ == '__main__':
	main()