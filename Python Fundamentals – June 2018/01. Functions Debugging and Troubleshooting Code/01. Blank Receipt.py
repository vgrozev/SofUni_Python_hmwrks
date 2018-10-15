def print_header():
    return "CASH RECEIPT\n------------------------------"


def print_body():
    return "Charged to____________________\nReceived by___________________"


def print_footer():
    return "------------------------------\n\u00A9 SoftUni"


def receipt():
    print(print_header())
    print(print_body())
    print(print_footer())


receipt()
