import os
import sys
import string
import argparse
import itertools
from datetime import datetime


def wordlist(chrs, min_len, max_len, list):

    if min_len > max_len:
        print('[->] minimal value should be smaller or the same as maximal value')
        sys.exit()

    if os.path.exists(os.path.dirname(list)) == False:
        os.makedirs(os.path.dirname(list))

    print('\n')

    print('[->] creating a wordlist = %s' % list)
    start = datetime.now()
    print('[->] start time : %s' % start)
    list = open(list, 'w')

    for n in range(min_len, max_len+1):
        for bear in itertools.product(chrs, repeat=n):
            chars = ''.join(bear)
            list.write('%s\n' % chars)
            sys.stdout.write('\r[->] saving %s' % chars)
            sys.stdout.flush()

    list.close()

    end = datetime.now()
    print('\n[->] ended : %s ' % end)
    print('\n[->] total : {}\n'.format(end - start))



def main() :

    parser = argparse.ArgumentParser(description = 'Wordlist')
    parser.add_argument('-chr', '--chars', default = None , help = 'charset')
    parser.add_argument('-min', '--min_len', type = int, default = 1 , help = 'minimum length')
    parser.add_argument('-max', '--max_len' , type = int, default = 2 , help = 'maximum length')
    parser.add_argument('-out', '--list', default = 'list/wordlist.txt', help = 'with this argument you can specify an exact path where your output will be located')
    args = parser.parse_args()
    if args.chars is None :
       os.system('python3 wordlist.py -h')
    else :
       wordlist(args.chars, args.min_len, args.max_len, args.list)





if __name__ == '__main__' :

   main()
