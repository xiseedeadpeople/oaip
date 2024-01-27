def main():
	with open('prices.txt', 'r+', encoding='utf-8') as f:
	    words = [i.strip().split() for i in f.readlines()]
	
	    try:
	        res = 0
	        for i in words:
	            res += int(i[1]) * float(i[2])
	
	        print(res)
	
	    except IndexError:
	        print('', end='')
		
if __name__ == "__main__":
	main()
