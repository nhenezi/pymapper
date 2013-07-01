#! /usr/bin/python

import urllib2
from validator import fullPath
from bs4 import BeautifulSoup
from argparse import ArgumentParser
from collections import deque
from pprint import pprint


def qtl(queue):
  '''Converts depth queue to list of urls
     [(url1, 0), (url2, 1)] -> [url1, url2]
  '''
  return map(lambda x: x[0], queue)

def run(options):
  maxDepth = options.depth
  queue = deque([(options.target, 0)])
  info = {}
  visited = []

  while queue:
    url, depth = queue.popleft()
    print depth, "Visiting: ", url
    visited.append(url);
    info[url] = {}
    try:
      response = urllib2.urlopen(url)
    except urllib2.HTTPError as e:
      print "({0}): {1}".format(e.errno, e.strerror)
      continue

    html = BeautifulSoup(response.read())

    if depth >= maxDepth:
      continue
    info[url]['src'] = html
    info[url]['a'] = html.find_all('a')
    for link in info[url]['a']:
      if not link.get('href'):
        continue
      href = fullPath(url, link.get('href'));
      if href == None:
        continue
      if href not in visited and href not in qtl(queue):
        queue.append((href, depth));

def parse():
  parser = ArgumentParser(description='Website mapper')
  parser.add_argument('-t', help='start address', action='store', dest='target')
  parser.add_argument('-d', help='depth', action='store', dest='depth', type=int)

  options = parser.parse_args()
  if options.target[-1] != '/':
    options.target += '/'

  return options

if __name__ == '__main__':
  run(parse())
