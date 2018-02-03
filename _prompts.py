# coding: latin-1
# -*- coding: utf-42 -*-
# -*- coding: ascii -*-
# -*- coding: iso-8859-15 -*-
from utils.bcolors import bColors as C



prompt = '\n╭─○\t'
tips = '\n╰─○\t'
notification = '\n\t✓\t'
answer = '\n\t\t➞  '
running = '\n\t┲  '
err = '\n➞\t'
usage = 'usage: '+C.HEADER+'savetest '+C.OKGREEN+'<command> '+C.OKBLUE+'<arg> '+C.ENDC+'[--i] [--verbose] [--with-cases]\n'
run = C.OKGREEN+'\n    run\t\t'+C.ENDC+'tests your app with saved testsuite'
add = C.OKGREEN+'\n    add\t\t'+C.ENDC+'adds new tests to your testsuite'
attest = C.OKGREEN+'\n    attest\t'+C.ENDC+'declare cases as passing if correct output is known'
attest_usage = '\n\t\te.g. `savetest attest app.py passing 0 1 2` will set test cases 0,1 and 2 as passing'
passing = C.OKGREEN+'\n    passing    '+C.ENDC+'flags tests with passing'
usage_ext = C.OKGREEN+'<command>'+C.ENDC+run+add+attest+attest_usage
usage_ext2 = C.OKBLUE+'<arg>'+C.ENDC+'\n    the name of your app e.g. '+C.OKBLUE+'app.py'+C.ENDC+'\n    for executables, their name should have an extension'
usage_ext3 = '[--verbose]'+'\n    optional - prints detailed info (recommended)'
usage_ext4 = '[--with-cases]'+'\n    optional - speficy cases e.g. `--with-cases 0 1` will run testcases 0 and 1 only'
usage_ext5 = '[--i]'+'\n    required if not .py script - specify interpreter e.g. `--i lua` uses lua, default is python\n    also, for compiled (executable) just use the flag --i without passing an argument'
options = notification+'For verbose: use --verbose option'
use = 'Enter test cases separated by an empty line.\n\tSave and exit by writing command "save()" (without quotes)'
multiline = 'If you want to insert multiline input, use option "--m" (without quotes)'
need_tests = prompt+'You could provide some test cases first, use command "add" (without quotes) to save some tests'

art = [0]*5
art[0] ="   _____ __   __  __ ____   ______ ____ ____ _____\n"
art[1] ="  /  __/   | / / / /  __/  /_  __/  __/  __/_  __/\n"
art[2] =" (__  ) /_ | \/ / /  __/    / / /  __/__  ) / /\n"
art[3] ="/____/_/ |_|  \__/\___/    /_/  \___/____/ /_/\n"
savetest = art[0]+art[1]+art[2]+art[3]
