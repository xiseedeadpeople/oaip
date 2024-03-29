import json

def main():
    with open('data.json') as f:
        data = json.load(f)
        a, b = input('что меняем: '), input('на что меняем: ')
    
        data[a] = b
    
    with open('data.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False)

if __name__ == "__main__":
	main()
