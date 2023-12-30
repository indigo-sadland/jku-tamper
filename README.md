## Description
**jku-tamper.py** - script for automating attack on JWT based on tampering of JKU header.

♦️ *I've made this tool mainly for the **Unicode** machine on Hack The Box* ♦️

### Workflow
1) Checks if JWT contains JKU header and downloads JWKS file from it to get structure;
3) Creates malicious JWKS;
4) Creates malicious JWT;
5) Runs http server to serve the malicious JWKS file.

## Installation

`git clone https://github.com/indigo-sadland/jku-tamper && cd jku-tamper` \
`pip3 install -r requirements.txt`

## Usage Example

```     
python3 jku-tamper.py -rurl "http://example.com/redirect/?url=" -lh 10.10.10.10 -lp 8080 -token "eyJhbGz ... x47_zWyA"
```

<img width="733" alt="Screenshot" src="https://user-images.githubusercontent.com/37074372/163670251-7d05a0c4-a361-43af-9067-5f96c9958fb8.png">
