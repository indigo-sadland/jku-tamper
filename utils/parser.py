from termcolor import colored
from jwcrypto import jwk
import requests
import jwt

jku_detected = False


def parse_token(token_string):

    """
        Decodes jwt string, extracts JKU url
        and downloads jwks from the url
    """

    print(colored('\n----{   DECODED  TOKEN   }----\n', attrs=["bold"]))

    # Decode token's headers.
    token_headers = jwt.get_unverified_header(token_string)
    print(colored("Headers:", attrs=["underline"]))
    for key, val in token_headers.items():
        h = colored(f"[+] {key}: {val}", "green")
        if key == "jku":
            jku_detected = True
            jku_url = val
        print(h)

    # Decode token's payload without verifying signature.
    token_payload = jwt.decode(token_string, options={"verify_signature": False})
    print(colored("\nPayload:", attrs=["underline"]))
    for key, val in token_payload.items():
        p = colored(f"[+] {key}: {val}\n", "green")
        print(p)

    if jku_detected:
        print(colored('----{    JKU DETECTED    }----\n', attrs=["bold"]))
        print(colored("[+] Starting Download... ", "green"))
        print(colored("i'll store it in memory\n", "yellow"))

        try:
            r = requests.get(jku_url, timeout=10)
        except:
            print(colored("ERR: UNABLE TO DOWNLOAD FILE. TIMEOUT.", "red", attrs=["reverse"]))
            exit()
        jwks = r.json()

        return jwks


def parse_pem(pem):
    pem_parsed = jwk.JWK.from_pem(pem.getvalue())
    return pem_parsed
