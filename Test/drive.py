import sys
try:
	sys.path.append('../App')
	import ass4
except:
	sys.path.append('App')
	import ass4

def main():
	print('Assignment 4 begins...\n')
	ass4.main()
	print('Assignment 4 ends...')

if __name__ == '__main__':
	main()