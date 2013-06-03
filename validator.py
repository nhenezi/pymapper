#! /usr/bin/python

from urlparse import urlparse

def fullPath(baseUrl, link):
  baseUrl = urlparse(baseUrl[:baseUrl.rfind('/') + 1])
  if link.startswith('http'):
    '''Full link'''
    return link
  if link.startswith('javascript'):
    '''We are not interested in following these links'''
    return None
  
  if link.startswith('/'):
    return "http://" + baseUrl.netloc + link
  
  return baseUrl.geturl() + link
