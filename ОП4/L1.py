from random import choice

def main():
	with open('lines.txt', 'r+') as f:
	    words = [i.strip() for i in f.readlines()]
	
	    try:
	        print(choice(words))
	
	    except IndexError:
	        print('', end='')
			
if __name__ == "__main__":
	main()
