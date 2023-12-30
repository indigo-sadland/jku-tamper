import io
from Crypto.PublicKey import RSA
from termcolor import colored


def gen_key():

    """
        Creates new RSA private key.
            :returns
                buf_key_str: bytes buffer with PEM key.
    """

    print(colored('-------{ PEM KEY }-------\n', attrs=["bold"]))
    key = RSA.generate(2048)
    prv_key = key.exportKey("PEM")

    # Write key to buffer.
    output_buf = io.BytesIO()
    output_buf.write(prv_key)

    print(colored('[+] New RSA Private Key successfully generated!', "green"))
    print(colored("i'll store it in memory", "yellow"))

    return output_buf

