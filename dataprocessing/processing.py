import dataprocessing
from dataprocessing.data.list import get_list_url
from dataprocessing.data.list import get_list_url_text
from dataprocessing.data.list import get_list_date
from dataprocessing.data.register import get_register_action
from dataprocessing.data.register import get_register_title
from dataprocessing.data.register import get_register_section
from dataprocessing.data.register import get_register_by
from dataprocessing.data.register import get_register_on
from dataprocessing.data.register import get_register_url
from dataprocessing.data.content import get_content_filename
from dataprocessing.data.content import get_content_category
from dataprocessing.data.content import get_content_category_slug
from dataprocessing.data.content import get_content_title
from dataprocessing.data.content import get_content_publishedby
from dataprocessing.data.content import get_content_createdby
from dataprocessing.data.content import get_content_publishedon
from dataprocessing.data.content import get_content_lastmodified
from dataprocessing.data.content import get_content_article


def process_list_data(soup, files_names, no_repeat_files):
    results = []
    for i in range(len(soup)):
        if len(get_list_url_text(soup, i)) == len(get_list_date(soup, i)) \
        and len(get_list_url(soup, i)) == len(get_list_date(soup, i)) \
        and len(get_list_url(soup, i)) == len(get_list_url_text(soup, i)):
            for j in range(len(get_list_date(soup, i))):
                if get_list_url(soup, i)[j].split('.html', 1)[0] in no_repeat_files:
                    results.append((
                        files_names[i].split('.html', 1)[0],
                        get_list_url(soup, i)[j].split('.html', 1)[0],
                        get_list_url_text(soup, i)[j],
                        get_list_date(soup, i)[j]
                    ))
    return results

def process_register_data(soup):
    results = []
    for i in range(len(soup)):
        if len(get_register_url(soup, i)) == len(get_register_on(soup, i)):
            for j in range(len(get_register_on(soup, i))):
                results.append((
                    get_register_action(soup, i)[j],
                    get_register_title(soup, i)[j],
                    get_register_section(soup, i)[j],
                    get_register_by(soup, i)[j],
                    get_register_on(soup, i)[j],
                    get_register_url(soup, i)[j].split('.html', 1)[0]
                ))
    return list(set(results))

def process_content_data(soup, files_names, no_repeat_files):
    results = []
    content_filename = {}
    value_content_category = {}
    category_slug = {}
    content_title = {}
    value_content_publishedby = {}
    value_content_createdby = {}
    content_publishedon = {}
    value_content_modifiedby = {}
    content_modifiedon = {}
    content_modifiedurl = {}
    content_article = {}    
    for i in range(len(soup)):
        content_filename.update({i + 1 : get_content_filename(files_names, i)})
        value_content_category.update({i + 1 : get_content_category(soup, i)})
        category_slug.update({i + 1 : get_content_category_slug(soup, i)})
        content_title.update({i + 1 : get_content_title(soup, i)})
        value_content_publishedby.update({i + 1 : get_content_publishedby(soup, i)})
        value_content_createdby.update({i + 1 : get_content_createdby(soup, i)})
        content_publishedon.update({i + 1 : get_content_publishedon(soup, i)})
        value_content_modifiedby.update({i + 1 : get_content_lastmodified(soup, i)[0]})
        content_modifiedon.update({i + 1 : get_content_lastmodified(soup, i)[1]})
        content_modifiedurl.update({i + 1 : get_content_lastmodified(soup, i)[2]})
        content_article.update({i + 1 : get_content_article(soup, i)})
    if len(content_filename) <= 459 \
    and len(content_title) == len(content_filename) \
    and len(content_filename) == len(value_content_category) \
    and len(value_content_category) == len(category_slug) \
    and len(category_slug) == len(value_content_publishedby) \
    and len(value_content_publishedby) == len(value_content_createdby) \
    and len(value_content_createdby) == len(content_publishedon) \
    and len(content_publishedon) == len(value_content_modifiedby) \
    and len(value_content_modifiedby) == len(content_modifiedon) \
    and len(content_modifiedon) == len(content_modifiedurl) \
    and len(content_modifiedurl) == len(content_article):
        for filename, category, category_slug, title, \
        publishedby, createdby, publishedon, \
        modifiedby, modifiedon, modifiedurl, \
        article in zip(content_filename.values(), value_content_category.values(), category_slug.values(), content_title.values(), \
        value_content_publishedby.values(), value_content_createdby.values(), content_publishedon.values(), \
        value_content_modifiedby.values(), content_modifiedon.values(), content_modifiedurl.values(),
        content_article.values()):
            if filename.split('.html', 1)[0] in no_repeat_files:
                results.append((filename.split('.html', 1)[0], category, category_slug, title, \
                publishedby, createdby, publishedon, \
                modifiedby, modifiedon, modifiedurl.split('.html', 1)[0], \
                article))
    return results