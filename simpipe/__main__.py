from argparse import ArgumentParser, Namespace
from colorama import Fore, Back, Style
import subprocess
import shlex
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
    parser.add_argument('--output', help='Set output destination [Default: ./output]', default='.')
    # Set collapse option (Paired-ended reads to single-ended reads)
    parser.add_argument('--collapse', action='store_true', help='Set collapse option (Paired-ended reads to single-ended reads)')
    # Get arguments from command line
    args: Namespace = parser.parse_args()

    # Check file extension
    if not (args.refDNA.endswith('.fa') or args.refDNA.endswith('.fasta')):
        print('[ERROR] Provide a FASTA format file as reference DNA')

    # Clear previous endo data
    # subprocess.run(['rm', '-rf', os.path.join(os.path.dirname(__file__), './.data/endo/*')])

    # Move data to default endo location
    subprocess.run(['cp', args.refDNA, os.path.join(os.path.dirname(__file__), './.data/endo/')])

    # Create loading script
    # file = open(os.path.join(os.path.dirname(__file__),'./temp'), 'a')
    # subprocess.run(['sudo', 'echo', '-e', '#!/bin/bash\n\n"\$@" &\n\nwhile kill -0 \$!; do\n\tprintf \'.\' > /dev/tty\n\tsleep 1\ndone\nprintf \'\\\\n\' > /dev/tty'], stdout=file)
    # file.close()

    print()
    printRunningMessage('Gargammel')

    print()

    printEndOfToolMessage('Gargammel')

    output_dir = os.path.join(args.output, 'gargammel')

    # Remove output dir if it exists
    subprocess.run(['rm', '-rf', output_dir])
    # Create output dir
    subprocess.run(['mkdir', output_dir])
    # Move files to output dir
    subprocess.run(['cp', os.path.join(os.path.dirname(__file__), './.data/simadna_s1.fq.gz'), os.path.join(output_dir, 'simadna_s1.fq.gz')])
    subprocess.run(['cp', os.path.join(os.path.dirname(__file__), './.data/simadna_s2.fq.gz'), os.path.join(output_dir, 'simadna_s2.fq.gz')])
    # Decompress files and delete previous compressed files
    subprocess.run(['gzip', '-d', '-q', '-f', '-v', os.path.join(output_dir, 'simadna_s1.fq.gz')])
    subprocess.run(['gzip', '-d', '-q', '-f', '-v', os.path.join(output_dir, 'simadna_s2.fq.gz')])
    # Rename paired ended reads
    subprocess.run(['mv', os.path.join(output_dir, 'simadna_s1.fq'), os.path.join(output_dir, 'paired_ended_read_1.fq')])
    subprocess.run(['mv', os.path.join(output_dir, 'simadna_s2.fq'), os.path.join(output_dir, 'paired_ended_read_2.fq')])

    # Collapse paired-ended into single-ended reads using adapterRemoval
    if args.collapse:
        subprocess.run(['AdapterRemoval', '--threads', '40', '--file1', os.path.join(output_dir, 'paired_ended_read_1.fq'), '--file2', os.path.join(output_dir, 'paired_ended_read_2.fq'), '--outputcollapsed', os.path.join(output_dir, 'single_ended_read.fq'), '--trimns', '--trimqualities', '--minlength', '30', '--collapse'])

    # Remove not necessary output files from AdapterRemoval
    # extract file names
    file_list = os.listdir() 
    file_list = list(filter(lambda file_name: file_name.startswith('your_output'), file_list))

    # command sentence
    cmd = 'rm -rf %s'

    for file in file_list:
        subprocess.Popen(shlex.split(cmd % file)) 

    # Remove temporary loading file
    # subprocess.run(['rm', 'temp'])
    
    printEndOfPipelineMessage()

if __name__ == '__main__':
    main()