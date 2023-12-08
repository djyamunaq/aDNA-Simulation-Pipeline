from argparse import ArgumentParser, Namespace
import subprocess
import os

def main():
    parser = ArgumentParser()

    # Set reference mtDNA from command line 
    parser.add_argument('--refDNA', help='Reference DNA that will be used to generate FASTQ of simulated aDNA')
    # Set output destionation from command line
    parser.add_argument('--output', help='Set output destination [Default: ./output]', default='output')
    # Get arguments from command line
    args: Namespace = parser.parse_args()

    # Clear previous endo data
    subprocess.run(['rm', '-rf', ])
    # Move data to default location
    subprocess.run(['cp', args.refDNA, os.path.join(os.path.dirname(__file__), './.data/endo/')])
    # Run gargammel simulation
    subprocess.run([os.path.join(os.path.dirname(__file__),'./gargammel/gargammel.pl'), os.path.join(os.path.dirname(__file__), './.data/')])
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


if __name__ == '__main__':
    main()