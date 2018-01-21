from options import Options
import re

def parseCommandArgs(args):
    line = ''
    is_verbose = 0
    interpreter = 'python' # 'interpreter to run app, default is pypy'
    for j in args: line += str(j) + ' '

    if str(Options.VERBOSE) in args: is_verbose = 1
    if str(Options.INTERPRETER) in args:
        try:
            p = re.compile('--i\s+?(\w+)')
            m = p.search(line)
            print(m.group(1))
            interpreter = str(m.group(1).strip())
        except Exception as e:
            print('\t\tPosibly, no interpreter provided')
            raise Exception(e)
    if str(Options.WITH_CASES) in args:
        try:
            p = re.compile('--with-cases\s+?(\d.*)+')
            m = p.search(line)
            cases = list(map(int, m.group(1).strip().split(' ')))
        except:
            cases = []
    else: cases = []

    return is_verbose, interpreter, cases
