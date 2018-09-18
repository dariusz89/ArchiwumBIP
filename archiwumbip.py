import sys
import dataprocessing
from dataprocessing.read import get_files_names
from dataprocessing.read import get_list
from dataprocessing.read import get_register
from dataprocessing.read import get_content
from dataprocessing.soup import create_soups
from dataprocessing.processing import process_list_data
from dataprocessing.processing import process_register_data
from dataprocessing.processing import process_content_data
import database
from database.queries import insert_all_data


path = 'files/'
files_names = get_files_names(path)

register_files = get_register(files_names)
register_soup = create_soups(register_files, path)
print("Przetwarzanie informacji z plików 'register_xxxx.html'. Proszę czekać.")
register_results = process_register_data(register_soup)

with open ('data/register_results.txt', 'w', encoding='utf-8') as result:
    for dataset in register_results:
        result.write(str(dataset) + '\n')

no_repeat_register_files = []
for item in register_results:
    no_repeat_register_files.append(item[5])

list_files = get_list(files_names)
list_soup = create_soups(list_files, path)
print("Przetwarzanie informacji z plików 'list_xxxx.html'. Proszę czekać.")
list_results = process_list_data(list_soup, list_files, no_repeat_register_files)
with open ('data/list_results.txt', 'w', encoding='utf-8') as result:
    for dataset in list_results:
        result.write(str(dataset) + '\n')

content_files = get_content(files_names)
content_soup = create_soups(content_files, path)
print("Przetwarzanie informacji z plików 'content_xxxx.html'. Proszę czekać.")
content_results = process_content_data(content_soup, content_files, no_repeat_register_files)
with open ('data/content_results.txt', 'w', encoding='utf-8') as result:
    for dataset in content_results:
        result.write(str(dataset) + '\n')

print("Wgrywanie informacji do bazy danych. Proszę czekać.")
insert_all_data(list_results, content_results, register_results)
print("Skończyłem.")