from bs4 import BeautifulSoup


def get_content_filename(files_names,i):
    return files_names[i]

def get_content_category(soup,i):
    return soup[i].find("span", {"class":"tytul_font"}) \
    .get_text().replace(':','')

def get_content_category_slug(soup,i):
    category_slug = soup[i].find("span", {"class":"tytul_font"}) \
    .get_text().replace(':','')
    category_slug = category_slug.replace(' ', '-')
    category_slug = category_slug.replace('A', 'a')
    category_slug = category_slug.replace('/', '-')
    category_slug = category_slug.replace('ż', 'z')
    category_slug = category_slug.replace('Z', 'z')
    category_slug = category_slug.replace('ó', 'o')
    category_slug = category_slug.replace('ń', 'n')
    category_slug = category_slug.replace('P', 'p')
    category_slug = category_slug.replace('E', 'e')
    category_slug = category_slug.replace('I', 'i')
    category_slug = category_slug.replace('O', 'o')
    category_slug = category_slug.replace('K', 'k')
    category_slug = category_slug.replace('Ą', 'a')
    category_slug = category_slug.replace('L', 'l')
    category_slug = category_slug.replace('S', 's')
    category_slug = category_slug.replace('A', 'a')
    category_slug = category_slug.replace('ę', 'e')
    return category_slug

def get_content_title(soup,i):
    return soup[i].find("span", {"class":"sub_tytul_font"}) \
    .get_text()

def get_content_publishedby(soup,i):
    return soup[i].find("tr", {"class":"podpis"}) \
    .get_text().split(':',1)[1]

def get_content_createdby(soup,i):
    if (soup[i].find("tr", {"class":"podpis"}) \
        .findNext('tr', {"class":"podpis"})) is None:
        return '-'
    else:
        return soup[i].find("tr", {"class":"podpis"}) \
        .findNext('tr', {"class":"podpis"}).get_text().split(':',1)[1]

def get_content_publishedon(soup,i):
    if (soup[i].find("tr", {"class":"podpis"}) \
        .findNext('tr', {"class":"podpis"})) is None:
        return soup[i].find("tr", {"class":"podpis"}) \
        .findNext('tr').get_text().split(':',1)[1].lstrip()
    else:
        return soup[i].find("tr", {"class":"podpis"}) \
        .findNext('tr').findNext('tr').get_text().split(':',1)[1].lstrip()

def get_content_lastmodified(soup,i):
    if (soup[i].find("tr", {"class":"podpis"}) \
        .findNext('tr', {"class":"podpis"})) is None:
        data = soup[i].find("tr", {"class":"podpis"}) \
        .findNext('tr').findNext('tr')
    else:
        data = soup[i].find("tr", {"class":"podpis"}) \
        .findNext('tr').findNext('tr').findNext('tr')
    by = data.get_text().split(':',1)[1].split(' ',2)[1]
    on = data.get_text().split(':',1)[1]
    if len(str(on).split(' ')) == 6:
        by = by + ' ' +str(on).split(' ',5)[2]
        on = str(on).split(' ',5)[3] + ' ' + str(on).split(' ',5)[4]
    else:
        on = str(on).split(' ',4)[2] + ' ' + str(on).split(' ',4)[3]
    url = data.find_all(href=True)[1]['href']
    return [by, on, url]

def get_content_article(soup, i):
    data = soup[i].find("div", id="tresc").table.tbody.tr.td
    whitelist = ['a','img', 'br']
    for tag in data.find_all(True):
        if tag.name not in whitelist:    
            tag.attrs = {}
        if tag.name == 'font' or tag.name == 'span' \
        or tag.name == 'o:p' or tag.name == 'v:textbox' \
        or tag.name == 'v:shape' or tag.name == 'st1:metricconverter' \
        or tag.name == 'st1:personname' or tag.name == 'pre':
            tag.insert_before(' ')
            tag.unwrap()
        if tag.name == 'b':
            tag.name = 'strong'
        if tag.name == 'i':
            tag.name = 'em'
        if tag.name == 'u':
            tag.name = 'span'
            tag['class'] = 'underline'
    urls = data.find_all('a', href=True)
    if urls:
        for url in urls:
            if(url.get('href').find('mailto:') > -1):
                url.unwrap()
        for link in urls:
            if '../www.assets.server.com' in link.get('href'):
                link['href'] = link.get('href') \
                .replace("../www.assets.server.com/sport/", "/uploads/")
            elif '../assets.server.com' in link.get('href'):
                link['href'] = link.get('href') \
                .replace("../assets.server.com/sport/", "/uploads/")
            elif '../sport.assets.com/' in link.get('href'):
                link['href'] = link.get('href') \
                .replace("../sport.assets.com/bip/", "/uploads/")
            elif '../www.assets.com/' in link.get('href'):
                link['href'] = link.get('href') \
                .replace("../www.assets.com/", "/uploads/")
            elif '.html?cms_id=' in link.get('href'):
                linkUrl = link.get('href').split(".html", 0)[0]
                link['href'] = link.get('href').replace(linkUrl, "")
            elif '../www.bip.*.*.pl/' in link.get('href'):
                link['href'] = link.get('href') \
                .replace("../www.bip.*.*.pl/", "/uploads/")
            elif '../bip.*.*.pl/' in link.get('href'):
                link['href'] = link.get('href') \
                .replace("../bip.*.*.pl/", "/uploads/")
            else:
                link['href'] = link.get('href')
    imgsrc = data.find_all('img', src=True)
    if imgsrc:
        for img in imgsrc:
            if '../www.bip.*.*.pl/' in img.get('src'):
                img['src'] = img.get('src') \
                .replace("../www.bip.*.*.pl/", "/uploads/")
            elif '../bip.*.*.pl/' in img.get('src'):
                img['src'] = img.get('src') \
                .replace("../bip.*.*.pl/", "/uploads/")
    imgwidth = data.find_all('img', width=True)
    if imgwidth:
        for img in imgwidth:
            del img['width']

    data = str(data).replace('<?xml:namespace prefix = "o" />',' ')
    data = str(data).replace('<?xml:namespace prefix = o />',' ')
    data = str(data).replace('<!--?xml:namespace prefix = "o" /-->', ' ')
    data = str(data).replace('<!--?xml:namespace prefix = o /-->',' ')
    data = str(data).replace('<?xml:namespace prefix = "o" ns = "urn:schemas-microsoft-com:office:office" />', ' ')
    data = str(data).replace('<?xml:namespace prefix = o ns = "urn:schemas-microsoft-com:office:office" />', ' ')
    data = str(data).replace('<!--?xml:namespace prefix = "o" ns = "urn:schemas-microsoft-com:office:office" /-->', ' ')
    data = str(data).replace('<!--?xml:namespace prefix = o ns = "urn:schemas-microsoft-com:office:office" /-->',' ')
    data = str(data).replace('<?xml:namespace prefix = "v" />',' ')
    data = str(data).replace('<?xml:namespace prefix = v />',' ')
    data = str(data).replace('<!--?xml:namespace prefix = "v" /-->',' ')
    data = str(data).replace('<!--?xml:namespace prefix = v /-->',' ')
    data = str(data).replace('<?xml:namespace prefix = "v" ns = "urn:schemas-microsoft-com:vml" />',' ')
    data = str(data).replace('<?xml:namespace prefix = v ns = "urn:schemas-microsoft-com:vml" />', ' ')
    data = str(data).replace('<!--?xml:namespace prefix = "v" ns = "urn:schemas-microsoft-com:vml" /-->',' ')
    data = str(data).replace('<!--?xml:namespace prefix = v ns = "urn:schemas-microsoft-com:vml" /-->',' ')
    data = str(data).replace('<?xml:namespace prefix = "st1" />',' ')
    data = str(data).replace('<?xml:namespace prefix = st1 />',' ')
    data = str(data).replace('<!--?xml:namespace prefix = "st1" /-->',' ')
    data = str(data).replace('<!--?xml:namespace prefix = st1 /-->',' ')
    data = str(data).replace('<?xml:namespace prefix = "st1" ns = "urn:schemas-microsoft-com:office:smarttags" />',' ')
    data = str(data).replace('<?xml:namespace prefix = st1 ns = "urn:schemas-microsoft-com:office:smarttags" />',' ')
    data = str(data).replace('<!--?xml:namespace prefix = "st1" ns = "urn:schemas-microsoft-com:office:smarttags" /-->',' ')
    data = str(data).replace('<!--?xml:namespace prefix = st1 ns = "urn:schemas-microsoft-com:office:smarttags" /-->',' ')
    data = str(data).replace('<?xml:namespace prefix = "w" />',' ')
    data = str(data).replace('<?xml:namespace prefix = w />',' ')
    data = str(data).replace('<!--?xml:namespace prefix = "w" /-->',' ')
    data = str(data).replace('<!--?xml:namespace prefix = w /-->',' ')
    data = str(data).replace('<?xml:namespace prefix = "w" ns = "urn:schemas-microsoft-com:office:word" />',' ')
    data = str(data).replace('<?xml:namespace prefix = w ns = "urn:schemas-microsoft-com:office:word" />',' ')
    data = str(data).replace('<!--?xml:namespace prefix = "w" ns = "urn:schemas-microsoft-com:office:word" /-->',' ')
    data = str(data).replace('<!--?xml:namespace prefix = w ns = "urn:schemas-microsoft-com:office:word" /-->',' ')
    data = str(data).replace('ñ','&#8226;')
    
    data = BeautifulSoup(data, 'html5lib')
    data.html.unwrap()
    data.head.unwrap()
    data.body.unwrap()
    return str(data)