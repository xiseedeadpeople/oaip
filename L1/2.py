def main():
  a = int(input('Зарплата за месяц:\n'))
  b = int(input('Количество отработанных в выходные часов:\n'))
  print(f'Размер премии: {a*0.01*b}')

 if __name__ == "__main__":
  main()
