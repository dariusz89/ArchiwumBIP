import re


def get_register_action(soup,i):
    action = []
    for item in soup[i].find_all('td', {'width':'80%'}):
        action.append(item.find(text=re.compile("akcja: ")) \
        .replace('\n', '').split(':',1)[1].lstrip())
    return action

def get_register_title(soup,i):
    title = []
    for item in soup[i].find_all('td', {'width':'80%'}):
        title.append(item.find(text=re.compile("tytuł pozycji: ")) \
        .replace('\n', '').split(':',1)[1].lstrip())
    return title

def get_register_section(soup,i):
    section = []
    for item in soup[i].find_all('td', {'width':'80%'}):
        section.append(item.find(text=re.compile("dział: ")) \
        .replace('\n', '').split(':', 1)[1].lstrip())
    return section

def get_register_by(soup,i):
    by = []
    for item in soup[i].find_all('td', {'width':'80%'}):
        if item.find(text=re.compile("osoba ")) is not None:
            by.append(item.find(text=re.compile("osoba ")) \
            .replace('\n', '').split(':',2)[1].lstrip())
        elif item.find(text=re.compile("autor: ")) is not None:
            by.append(item.find(text=re.compile("autor: ")) \
            .replace('\n', '').split(':',2)[1].lstrip())
    return by

def get_register_on(soup,i):
    on = []
    for item in soup[i].find_all('td', {'width':'80%'}):
        on.append(item.find(text=re.compile("czas akcji: ")) \
        .replace('\n', '').split(':',1)[1].lstrip().replace(' / ', ' '))
    return on

def get_register_url(soup,i):
    url = []
    for item in soup[i].find_all('td', {'width':'80%'}):
        if item.find('a'):
            url.append(item.find('a')['href'])
        elif item.find('font'):
            url.append(item.find('font').get_text())
    return url