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
run = C.OKGREEN+'\n    run    '+C.ENDC+'tests your app with saved testsuite'
add = C.OKGREEN+'\n    add    '+C.ENDC+'adds new tests to your testsuite'
usage_ext = C.OKGREEN+'<command>'+C.ENDC+run+add
usage_ext2 = C.OKBLUE+'<arg>'+C.ENDC+'\n    <arg> is the name of your app e.g. '+C.OKBLUE+'app.py'+C.ENDC
usage_ext3 = '[--verbose]'+'\n    optional - prints information (recommended)'
usage_ext4 = '[--with-cases]'+'\n    optional - speficy cases e.g. `--with-cases 0 1` will run testcases 0 and 1 only'
usage_ext5 = '[--i]'+'\n    required if not .py script - specify interpreter e.g. `--i lua` uses lua, default is python'
options = notification+'For verbose: use --verbose option'
use = 'Enter test cases separated by an empty line.\n\tSave and exit by writing command "save()" (without quotes)'
multiline = 'If you want to insert multiline input, use option "--m" (without quotes)'
need_tests = prompt+'you have to provide some test cases first, use command "add" (without quotes) to save some tests'

art = [0]*5
art[0] ="   _____ __   __  __ ____   ______ ____ ____ _____\n"
art[1] ="  /  __/   | / / / /  __/  /_  __/  __/  __/_  __/\n"
art[2] =" (__  ) /_ | \/ / /  __/    / / /  __/__  ) / /\n"
art[3] ="/____/_/ |_|  \__/\___/    /_/  \___/____/ /_/\n"
savetest = art[0]+art[1]+art[2]+art[3]
