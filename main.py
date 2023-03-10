import argparse
from commands.ByteChecker import ByteChecker
from commands.ByteWriter import ByteWriter

parser = argparse.ArgumentParser(description='Console for reading bytes and replacing bytes from another file.')
subparsers = parser.add_subparsers(dest='command', title='Commands')
# Subparser for 'c' command
parser_c = subparsers.add_parser('c', help='Process file for verify bytes')
parser_c.add_argument('filename', help='File to process')
# Subparser for 'w' command
parser_w = subparsers.add_parser('w', help='Copy bytes from first file into second')
parser_w.add_argument('filename1', help='First file with source bytes')
parser_w.add_argument('filename2', help='Second file with destination bytes')

args = parser.parse_args()

if args.command == 'c':
    c_command = ByteChecker(args.filename)
    c_command.run()
elif args.command == 'w':
    w_command = ByteWriter(args.filename1, args.filename2)
    w_command.run()
else:
    parser.print_help()
