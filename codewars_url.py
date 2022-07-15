"""
from urllib.parse import urlparse

def domain_name(url):
    # Return a clean domain name.
    domain = urlparse(url).netloc
    if domain == '':
        domain = urlparse(url).path
        return "".join(domain.split(".", 3) [1:2])
    else:
        return "".join(domain.split(".") [:1])
"""
import re

def domain_name(url):
    # Return a clean domain name.
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')

url = ["http://github.com/carbonfive/raygun", "www.xakep.ru",
       "https://youtube.com"]

for i in url:
    print(domain_name(i))