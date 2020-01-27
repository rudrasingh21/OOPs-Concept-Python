#0.025.1 Read Only and Computed Properties Program

import urllib
from urllib import request
from time import perf_counter


class WebPage:
    def __init__(self, url):
        self.url = url
        self._page = None
        self._load_time_secs = None
        self._page_size = None

    #looks like we are using url above as a bare attribute ,
    #So lets make it as a property.

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value
        self._page = None
        # we'll lazy load the page - i.e. we wait until some property is requested

    @property
    def page(self):
        if self._page is None:
            self.download_page()
        return self._page

    @property
    def page_size(self):
        if self.page is None:
            self.download_page()
        return self._page_size

    @property
    def time_elapsed(self):
        if self._page is None:
            self.download_page()
        return self._load_time_secs

    def download_page(self):
        self._page_size = None
        self._load_time_secs = None
        start_time = perf_counter()
        with urllib.request.urlopen(self.url) as f:
            self._page = f.read()
        end_time = perf_counter()
        self._page_size = len(self._page)
        self._load_time_secs = end_time - start_time


urls = {
    'https://www.google.com',
    'https://www.yahoo.com'
    }

for url in urls:
    page = WebPage(url)

'''
Above will just load tha page , 
this is called lazy property.

it will just create instances.
        self.url = url
        self._page = None
        self._load_time_secs = None
        self._page_size = None
        
and as per our need , it will get loaded.

It will not use any resources .
Find below code -
'''

for url in urls:
    page = WebPage(url)
    print(f'{url} \tsize={format(page.page_size, "_")} \telapsed={page.time_elapsed:.2f} secs')

'''
Output:-

https://www.yahoo.com 	size=462_866 	elapsed=2.07 secs
https://www.google.com 	size=15_130 	elapsed=0.20 secs

'''

# READ:- https://www.journaldev.com/14893/python-property-decorator