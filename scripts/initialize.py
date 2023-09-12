from argparse import ArgumentParser
from os import environ
from src.main import main

def initialize():
    parser = ArgumentParser(description='Initialize the database and start the API service.')
    parser.add_argument(
        '-env',
        dest='env',
        type=str, 
        choices=['test', 'dev', 'prod'],
        default='dev',
        help='Specify if running in test, dev or prod mode. Default is dev.')
    args = parser.parse_args()
    environ["ENV"] = args.env
    print(f"Running in {environ['ENV']} mode.")
    main()