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
usage = 'usage: savetest <command> [<arg>] [-v]\n'
run = '\n    run\ttests your app with saved testsuite'
add = '\n    add\tadds new tests to your testsuite'
usage_ext = '<command>'+run+add
usage_ext2 = '[<args>]'+'\n    in this case <arg> is the name of your app with extension'
usage_ext3 = '[-v]'+'\n    option -v is for verbose output'
# \n\n\t  where (your_app) is your script with extension e.g. main.c\n'
options = notification+'For verbose: use -v option'
use = 'Enter test cases separated by an empty line.\n\tSave and exit by writing command "save()" (without quotes)'
multiline = 'If you want to insert multiline input, use option "--m" (without quotes)'
need_tests = prompt+'you have to provide some test cases first, use command "add" (without quotes) to save some tests'
