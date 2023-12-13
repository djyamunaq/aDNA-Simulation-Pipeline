from argparse import ArgumentParser, Namespace
from colorama import Fore, Back, Style
import subprocess
import os

def printRunningMessage(toolName):
    print(Fore.BLUE + Style.BRIGHT + '> Running on', toolName)
    print(Style.RESET_ALL)

def printEndOfPipelineMessage():
    print(Fore.GREEN + Style.BRIGHT + '> Pipeline finished')
    print(Style.RESET_ALL)

def printEndOfToolMessage(toolName):
    print(Fore.GREEN + Style.BRIGHT + '> Ended running on', toolName)
    print(Style.RESET_ALL)

def main():
    parser = ArgumentParser()

    # Set reference mtDNA from command line 
    parser.add_argument('--refDNA', help='Reference DNA that will be used to generate FASTQ of simulated aDNA')
    # Set output destionation from command line
    parser.add_argument('--output', help='Set output destination [Default: ./output]', default='output')
    # Get arguments from command line
    args: Namespace = parser.parse_args()

    # Clear previous endo data
    subprocess.run(['rm', '-rf', os.path.join(os.path.dirname(__file__), './.data/endo/*')])
    # Move data to default endo location
    subprocess.run(['cp', args.refDNA, os.path.join(os.path.dirname(__file__), './.data/endo/')])

    # Create loading script
    file = open(os.path.join(os.path.dirname(__file__),'./temp'), 'a')
    subprocess.run(['sudo', 'echo', '-e', '#!/bin/bash\n\n"\$@" &\n\nwhile kill -0 \$!; do\n\tprintf \'.\' > /dev/tty\n\tsleep 1\ndone\nprintf \'\\\\n\' > /dev/tty'], stdout=file)
    file.close()

    printRunningMessage('Gargammel')

    # Run gargammel simulation
    subprocess.run(['sudo', os.path.join(os.path.dirname(__file__),'./temp'), os.path.join(os.path.dirname(__file__),'./gargammel/gargammel.pl'), os.path.join(os.path.dirname(__file__), './.data/'),  '>>', '/dev/null', '2', '>', '&1'])

    printEndOfToolMessage('Gargammel')

    # Remove output dir if it exists
    subprocess.run(['rm', '-rf', args.output])
    # Create output
    subprocess.run(['mkdir', args.output])
    # Move files to output dir
    subprocess.run(['cp', os.path.join(os.path.dirname(__file__), './.data/simadna_s1.fq.gz'), os.path.join(args.output, 'simadna_s1.fq.gz')])
    subprocess.run(['cp', os.path.join(os.path.dirname(__file__), './.data/simadna_s2.fq.gz'), os.path.join(args.output, 'simadna_s2.fq.gz')])
    # Decompress files and delete previous compressed files
    subprocess.run(['gzip', '-d', '-q', '-f', os.path.join(args.output, 'simadna_s1.fq.gz')])
    subprocess.run(['gzip', '-d', '-q', '-f', os.path.join(args.output, 'simadna_s2.fq.gz')])

    # Remove temporary loading file
    subprocess.run(['rm', 'temp'])
    
    printEndOfPipelineMessage()

if __name__ == '__main__':
    main()