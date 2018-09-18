# ArchiwumBIP
Webscraping project using python and beautifulsoup library.

## Project description
The archiwumbip project was invented to create a database with information contained in html files from a static copy of a web page and to allow it to be browsed using any web browser.

To create a database from html files, the python language was used along with additional libraries: [bs4](https://www.crummy.com/software/BeautifulSoup/), [mysql.connector](https://dev.mysql.com/doc/connector-python/en/), [configparser](https://docs.python.org/3/library/configparser.html), [os](https://docs.python.org/3/library/os.html), [sys](https://docs.python.org/3/library/sys.html), [time](https://docs.python.org/3/library/time.html), [datetime](https://docs.python.org/3/library/datetime.html), [re](https://docs.python.org/3/library/re.html).
During the work of the script, the files in the data directory will be created with information that has been obtained from the html files.

* dummy_database.sql - An empty database, which does not contain any data yet, can be found in the root directory of this repository under the name.

## First start
Before you run the script that processes html files for the first time, you must configure the connection to the database correctly.
Location of configuration files:
* database / config.ini

## Acknowledgments
* Stackoverflow - For the existence of solutions that existed before the problem appeared