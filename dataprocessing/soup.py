import sys
import time
import datetime
from bs4 import BeautifulSoup


def create_soups(files_names, files_path):
    created_soups = []
    j = 1
    print('Trwa parsowanie pliku: ')
    errors_while_creating_soups = []
    files_with_errors_while_creating_soups = []
    errors_while_creating_soups_counter = 0
    for i in range(len(files_names)):
        print(str(j).zfill(3) + '. ' + files_names[i] + '.', end='  \r')
        sys.stdout.flush()
        time.sleep(0.01)
        with open(files_path + files_names[i], encoding="utf-8") as fp:
            try:
                created_soups.append(BeautifulSoup(fp, 'html5lib'))
            except UnicodeDecodeError as e:
                error_custom_description = '\nWystąpił problem ze stroną kodowania ' \
                'niektórych z parsowanych plików. \nZawierają one w sobie niepoprawne znaki ' \
                'dla strony kodowej UTF-8, tzw Mojibake.'
                error_original_description = '\nKomunikat błędu:\n' + str(e)
                errors_while_creating_soups_counter = errors_while_creating_soups_counter + 1
                log_time = time.time()
                log_time_signature = datetime.datetime.fromtimestamp(log_time).strftime('%Y-%m-%d %H:%M:%S')
                errors_while_creating_soups.append('Sygnatura czasowa: ' \
                 + log_time_signature + '\n' + 'Plik:\n' + files_names[i] + error_original_description)
                files_with_errors_while_creating_soups.append(files_names[i])
        j = j + 1
    if errors_while_creating_soups_counter > 0:
        print('\n' + error_custom_description)
        print('\nWięcej szczegółów odnajdziesz w pliku errors.txt,'
        + '\nktóry został utworzony w poniższej lokalizacji:\n' + sys.path[0] + 'data/errors.txt')
        with open (sys.path[0] + 'data/errors.txt', 'w', encoding='utf-8') as r:
            for error in errors_while_creating_soups:
                r.write(error + '\n\n')
        print('\nWykaz plików źródłowych do poprawienia:')
        for file_name in files_with_errors_while_creating_soups:
            print(file_name)
        sys.exit('Uruchom skrypt ponownie, gdy tylko poprawisz wskazane powyżej pliki.')
    else:
        print('\nZakończono odczytywanie plików.')
        return created_soups