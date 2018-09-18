def get_list_url(soup, i):
    results = []
    for item in soup[i].find_all('td', {'width':'70%'}):
        results.append(item.find("a").get('href'))
    return results

def get_list_url_text(soup, i):
    results = []
    for item in soup[i].find_all('td', {'width':'70%'}):
        results.append(item.find("a").get_text())
    return results

def get_list_date(soup, i):
    results = []
    for item in soup[i].find_all('td', {'width':'30%'}):
        day = item.get_text().split(' ', 3)[0]
        year = item.get_text().split(' ', 3)[2]
        month = item.get_text().split(' ', 3)[1]
        months = [
            'Stycznia', 
            'Lutego', 
            'Marca', 
            'Kwietnia', 
            'Maja', 
            'Czerwca', 
            'Lipca', 
            'Sierpnia', 
            'Września', 
            'Października', 
            'Listopada', 
            'Grudnia'
            ]
        for key, month_name in enumerate(months):
            if month == month_name:
                if key > 9:
                    month = str(key + 1)
                else:
                    month = '0' + str(key + 1)
        results.append(year + '-' + month + '-' + day)
    return results