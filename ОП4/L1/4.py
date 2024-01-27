def main():
	with open('words.txt', 'r+', encoding='utf-8') as f:
	    words = [i.strip() for i in f.readlines()]
	
	    mx = len(max(words, key=len))
	    print(*[i for i in words if len(i) == mx])

if __name__ == "__main__":
	main()
