#! /usr/bin/python

import urllib2
from validator import fullPath
from bs4 import BeautifulSoup
from collections import deque

url = "test url"
maxDepth = 2

queue = deque([(url, 0)])
visited = []

def qtl(queue):
  '''Converts depth queue to list of urls'''
  return map(lambda x: x[0], queue)

while queue:
  url, depth = queue.popleft()
  print depth, "Visiting: ", url
  visited.append(url);
  depth += 1
  try:
    response = urllib2.urlopen(url)
  except urllib2.HTTPError as e:
    print "({0}): {1}".format(e.errno, e.strerror)
    continue
  html = BeautifulSoup(response.read())

  if depth >= maxDepth:
    continue
  for link in html.find_all('a'):
    if not link.get('href'):
      continue
    href = fullPath(url, link.get('href'));
    if href == None:
      continue
    if href not in visited and href not in qtl(queue):
      queue.append((href, depth));
