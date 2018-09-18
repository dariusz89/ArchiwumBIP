import os


def get_files_names(path):
    for _, _, files in os.walk(path):
        return files

def get_list(files_names):
    list_files_names = []
    for item in files_names:
        if 'list' in item:
            list_files_names.append(item)
    return list_files_names

def get_register(files_names):
    register_files_names = []
    for item in files_names:
        if 'rejestr_zmian' in item:
            register_files_names.append(item)
    return register_files_names

def get_content(files_names):
    content_files_names = []
    for item in files_names:
        if 'content' in item and not 'print_content' in item:
            content_files_names.append(item)
    return content_files_names