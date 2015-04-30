# pymapper

pymapper is a simple website mapper/crawler.

## What can it do?

pymapper can:
* recursively crawl website
* extract `a` and `img` elements
* write output to stdout or file

## Details and usage example!

DFS using links as nodes. Example usage: `./pymapper -t http://test.local/ -d 1 -e img -w images.out` will visit http://test.local, all links on that page and output all images to images.out file

### Arguments:

* `-d DEPTH, --depth DEPTH` how deep do you want to dig?
* `-e EL, --extract EL` element to extract. Currently, only `a` and
  `img` are supported
* `-t TARGET, --target TARGET` Starting adderss
* `-v, --verbose` displays detailed information, i.e. things like
  depth, current url...
* `-w FILE, --write FILE` writes ouput to FILE


## Dependencies

* python 2.7
* pip
* virtualenv

## Setup instructions

* Initialize virtualenv `virtualenv venv`
* Activate virtualenv `source ./venv/bin/activate`
* Install pip dependencies `pip install -r reqs.txt`
* run pymapper `pyhon pymapper -h`

Released under MIT license, see [license.txt](https://github.com/nhenezi/pymapper/blob/master/license.txt) for more details
