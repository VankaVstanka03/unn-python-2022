import argparse
import sys
import pytz as pz
from datetime import datetime, timedelta
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PythonLexer

#code = 'print "Hello World"'
#print(highlight(code, PythonLexer(), TerminalFormatter()))

def Highlight(text):
    print(highlight(text, PythonLexer(), TerminalFormatter()))

def Cowsay(text):
    print(f"""___________
< {text} >
 -----------
     \   ^__^
      \  (oo)\_______
         (__)\       )\/\
           ||----w |
           ||     ||""")

def Time(text):
    
    fmt = '%Y-%m-%d %H:%M:%S %Z%z'
    source_date = datetime.now()
    current_time_zone = pz.timezone(text)
    currentDateWithTimeZone = current_time_zone.localize(source_date)
    print(currentDateWithTimeZone)



def build_argparser():
    comm = ['time', "highlight", "cowsay"]
    parser = argparse.ArgumentParser()
    parser.add_argument('command', type=str, help=f'write commands: {comm[0]}, {comm[1]}, {comm[2]}')
    parser.add_argument('parametrs', type=str, help='enter parametrs for command')
    return parser

def main():
    args = build_argparser().parse_args()
    if args.command == "highlight":
        Highlight(args.parametrs)
    elif args.command == "cowsay":
        Cowsay(args.parametrs)
    elif args.command == "time":
        Time(args.parametrs)

if __name__ == '__main__':
    sys.exit(main())

