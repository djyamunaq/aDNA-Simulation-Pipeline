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

def processConfigFileFlags(flagStr, flags):
    flagStr = flagStr.replace('\t', ' ')
    flagStr = flagStr.replace('\n', '')
    flagStr = flagStr.replace(',', ' ')
    flagList = flagStr.split()
    
    flagName = flagList[0]
    flagValues = flagList[1:]

    # print(flagName, end='\n\t')
    # print(flagValues)

    flags[flagName] = flagValues 

def main():
    parser = ArgumentParser()

    # Set config file from command line 
    parser.add_argument('--configFile', help='Configuration file with gargammel parameters and flags', default=None)
    # Set reference mtDNA from command line 
    parser.add_argument('--refDNA', help='Reference DNA that will be used to generate FASTQ of simulated aDNA')
    # Set output destionation from command line
    parser.add_argument('--output', help='Set output destination [Default: ./output]', default='.')
    
    # Get arguments from command line
    args: Namespace = parser.parse_args()

    configFile = None
    flags = {}
    if args.configFile:
        configFile = open(args.configFile, 'r') 
        for line in configFile:
            line = line.lstrip()
            if not line.startswith('#') and line != "":
                processConfigFileFlags(line, flags)

    # Check file extension
    if not (args.refDNA.endswith('.fa') or args.refDNA.endswith('.fasta')):
        print('[ERROR] Provide a FASTA format file as reference DNA')

    # Move data to default endo location
    subprocess.run(['rm', '-rf', os.path.join(os.path.dirname(__file__), './.data/endo/')])
    subprocess.run(['mkdir', '-p', os.path.join(os.path.dirname(__file__), './.data/endo/')])
    subprocess.run(['cp', args.refDNA, os.path.join(os.path.dirname(__file__), './.data/endo/')])

    output_dir = os.path.join(args.output, 'simpipe_output')
    subprocess.run(['mkdir', '-p', output_dir])

    print()
    printRunningMessage('Gargammel')

    # Build gargammel command
    command = [os.path.join(os.path.dirname(__file__),'./gargammel/gargammel.pl')]
    for key in flags:
        command.append(key)
        if len(flags[key]) > 0: 
            command.append(','.join(flags[key]))
    
    command.append('-o')
    command.append(output_dir + '/simadna')

    command.append(os.path.join(os.path.dirname(__file__), '.data/'))

    # print(command)

    # Run gargammel simulation
    subprocess.run(command)

    print()
    printEndOfToolMessage('Gargammel')

    printEndOfPipelineMessage()

if __name__ == '__main__':
    main()