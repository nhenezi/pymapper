#! /usr/bin/python

import urllib2
from validator import fullPath
from bs4 import BeautifulSoup
from collections import deque

url = "test url"
maxDepth = 1

queue = deque([(url, 0)])
info = {}
visited = []

def qtl(queue):
  '''Converts depth queue to list of urls'''
  return map(lambda x: x[0], queue)

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
  info[url]['img'] = html.find_all('img')
  info[url]['a'] = html.find_all('a')
  for link in info[url]['a']:
    if not link.get('href'):
      continue
    href = fullPath(url, link.get('href'));
    if href == None:
      continue
    if href not in visited and href not in qtl(queue):
      queue.append((href, depth));
