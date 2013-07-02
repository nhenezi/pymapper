#! /usr/bin/python

from urlparse import urlparse

def fullPath(baseUrl, link):
  # converts baseUrl string to ParseResult (urlparse object)
  # for constructing simple links we can ignore everything after 
  # last slash, i.e. on http://test.com/super.ext?mag=ic
  # relative links are constructed with http://test.com/ prefix
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
