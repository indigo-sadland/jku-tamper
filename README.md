## Description
**jku-tamper.py** - script for automating attack on JWT based on tampering of JKU header.

♦️ *I've made this tool mainly for the **Unicode** machine on Hack The Box* ♦️

## Installation

`git clone https://github.com/indigo-sadland/jku-tamper && cd jku-tamper` \
`pip3 install -r requirements.txt`

## Usage Example

```     
python3 jku-tamper.py -rurl "http://example.com/redirect/?url=" -lh 10.10.10.10 -lp 8080 -token "eyJhbGz ... x47_zWyA"
```
