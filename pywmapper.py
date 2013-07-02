#! /usr/bin/python

import urllib2
import sys
from argparse import ArgumentParser
from bs4 import BeautifulSoup
from collections import deque
from validator import fullPath
from writer import writer

def qtl(queue):
  '''Converts depth queue to list of urls
     [(url1, 0), (url2, 1)] -> [url1, url2]
  '''
  return map(lambda x: x[0], queue)

def run(options):
  output = writer(options)
  maxDepth = options.depth
  queue = deque([(options.target, 0)])
  info = {} # contains all scraped info
  visited = [] # array of visited urls
  scraped = {  # list of scraped elements; to avoid duplication
    'a': [],
    'img': [],
  }

  while queue:
    url, depth = queue.popleft()
    if depth > maxDepth:
      break

    if options.verbose == True:
      print str(depth) + " Visiting: " + url
    visited.append(url);
    info[url] = {}
    try:
      response = urllib2.urlopen(url)
    except urllib2.HTTPError as e:
      if options.verbose == True:
        print "({0}): {1}".format(e.errno, e.strerror)
      continue

    html = BeautifulSoup(response.read())
    info[url]['src'] = html
    info[url]['a'] = html.find_all('a')
    info[url]['img'] = html.find_all('img')

    if options.extract == 'img':
      for image in info[url]['img']:
        href = fullPath(url, image['src'])
        if href != None and href not in scraped['img']:
          scraped['img'].append(href)
          output(href + '\n')

    for link in info[url]['a']:
      if not link.get('href'):
        continue
      href = fullPath(url, link.get('href'));
      if href == None:
        continue
      if options.extract == 'a':
        output(href + '\n')
      if href not in visited and href not in qtl(queue):
        queue.append((href, depth + 1));

def parse():
  parser = ArgumentParser(description='Website mapper')
  parser.add_argument('-t', '--target', help='Starting address', action='store', dest='target')
  parser.add_argument('-d', '--depth', help='How deep do you want to dig?', action='store', dest='depth', type=int, default=0)
  parser.add_argument('-v', '--verbose', help='Displays detailed ouput, i.e. things like depth, current base link...', action='store_true', default=False)
  parser.add_argument('-e', '--extract', choices=['a', 'img'], help="what to extract")
  parser.add_argument('-w', '--write', help='Write to file', default=False)


  options = parser.parse_args()
  if options.target == None:
    print "Invalid usage, try -h for help"
    sys.exit()
  if options.target[-1] != '/':
    options.target += '/'

  return options

if __name__ == '__main__':
  run(parse())
