import time
from pathlib import Path
# from tqdm import tqdm


def bforcer(password, show_progress=True, show_errors=False):
    g = False
    p = Path("PasswordsList/")
    errs = 0
    not_opened = []

    start = time.time()
    for file in p.rglob("*"):  # x -  filenames

        with open(file, encoding='utf-8') as f:
            try:
                if show_progress is True:
                    print(f'Открываю {file}...')

                current_string = f.readlines()
                lines = [line.rstrip() for line in current_string]

                # pbar = tqdm(lines, ncols=100)
                # for char in pbar:
                #     pbar.set_description(f'Processing')

                for i in lines:

                    if i == password:
                        g = True
                        finish = time.time()
                        break

            except UnicodeDecodeError:
                not_opened.append(file)
                errs += 1

        if g is True:
            if show_progress is True:
                print()

            print(f'success!', end=' ')
            time.sleep(1)
            print(f'research time: {format((finish - start), ".2f")} seconds.')
            time.sleep(1)
            print(f'password: "{password}"')
            break

    if g is False:
        print(f'your password is strong', end='  ')
        time.sleep(1)
        print('.', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.', end=' ')
        time.sleep(0.5)
        print(f'or just absent in my database.')
        time.sleep(1)
        print('i cant guess :)')

    if errs > 0 and show_errors is True:
        time.sleep(0.75)
        print(f'\nerrors: {errs} (UnicodeDecodeError)\ncan\'t open: {not_opened}')


pasw = input('Введите пароль чтобы я попытался его угадать: ')
bforcer(pasw)  # show_progress=True, show_errors=True
