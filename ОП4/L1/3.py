def main():
	with open('lines.txt', 'r+', encoding='utf-8') as f:
	    words = [i.strip() for i in f.readlines()]
	
	    print('чётные:')
	    for i in range(len(words)):
	        if i % 2 != 0:
	            print(words[i], end=' ')
	
	    print('\n\nнечётные:')
	    for i in range(len(words)):
	        if i % 2 == 0:
	            print(words[i], end=' ')
				
if __name__ == "__main__":
	main()
