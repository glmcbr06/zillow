import logging


def main(args):
    print(args)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--city', help='search city')
    parser.add_argument('--state', help='search state')
    parser.add_argument("-v", action='store_true', help="Show DEBUG log")
    parsedArgs = parser.parse_args()

    if parsedArgs.v:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    main(parsedArgs)
