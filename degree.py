from urllib.request import urlretrieve
import mechanicalsoup
import re
import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
url = "http://www.umji.sjtu.edu.cn/equivalence/university/index/2"
UM_INDEX = 1
JI_INDEX = 4
TYPE_INDEX = -4
browser = mechanicalsoup.StatefulBrowser()
d = {}
def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleanr2 = re.compile('\$\(document\)[\s\S\w\W]*')
  cleantext = re.sub(cleanr, '', raw_html)
  cleantext = re.sub(cleanr2, '', cleantext)
  return ' '.join(cleantext.split())

def get_dict(browser=browser, url=url):
    if not url:
        return
    browser.open(url)
    print(f"Open page: {url}")
    page = browser.get_current_page()
    course_list = page.find('div', class_='list')
    course_list = course_list.find_all('li')
    for course in course_list:
        tmps = course.find_all('span')
        um = cleanhtml(tmps[UM_INDEX].text)
        ji = cleanhtml(tmps[JI_INDEX].text)
        ji_type = cleanhtml(tmps[TYPE_INDEX].text)
        d[um] = (ji or 'none ', ji_type)

def get_courses(courses):
    for ji in courses:
        ji = ji.upper()
        um = d.get(ji, None)
        if (um):
            print(f'{ji:12}\t{um[0]:6}\t{um[1]}')
        else:
            print(f'{ji} not found, you may need to transfer yourself')

def main(file_name):
    with open(file_name) as f:
        course_list = [course.strip() for l in f.readlines() for course in l.split(' ') ]
        get_dict()
        print(course_list)
        get_courses(course_list)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('usage: python degree.py <file> one course id one line no space')
        exit(1)
    main(sys.argv[1])

