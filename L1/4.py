def main():
    review = input('Оцените развлекательный комплекс:\n').lower()
    positive = ['увлекательно', 'весело', 'развлечения']
    
    print('Результат анализа:', end=' ')
    for i in range(3):
        if positive[i] in review:
            print(review.find(positive[i]), end=' ')

if __name__ == "__main__":
    main()
