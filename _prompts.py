# coding: latin-1
# -*- coding: utf-42 -*-
# -*- coding: ascii -*-
# -*- coding: iso-8859-15 -*-



prompt = '\n╭─○\t'
tips = '\n╰─○\t'
notification = '\n\t✓\t'
answer = '\n\t\t➞  '
running = '\n\t┲  '
err = '\n➞\t'
usage = 'usage: savetest <command> [<arg>] [--verbose]\n'
run = '\n    run    tests your app with saved testsuite'
add = '\n    add    adds new tests to your testsuite'
usage_ext = '<command>'+run+add
usage_ext2 = '[<arg>]'+'\n    in this case, <arg> is the name of your app with extension'
usage_ext3 = '[--verbose]'+'\n    option for printing additional output'
# \n\n\t  where (your_app) is your script with extension e.g. main.c\n'
options = notification+'For verbose: use --verbose option'
use = 'Enter test cases separated by an empty line.\n\tSave and exit by writing command "save()" (without quotes)'
multiline = 'If you want to insert multiline input, use option "--m" (without quotes)'
need_tests = prompt+'you have to provide some test cases first, use command "add" (without quotes) to save some tests'

art = [0]*5
art[0] ="   _____ ___   __  __ ____   _____ ____ _____ ____\n"
art[1] ="  /  __/ __ | / / / /  __/  /_  __/ __/  __/_  __/\n"
art[2] =" (__  ) /_/ | \/ / /  __/    / / / __/__  ) / /\n"
art[3] ="/____/_/ /__|  \__/____/    /_/ /___/____/ /_/\n"
savetest = art[0]+art[1]+art[2]+art[3]
