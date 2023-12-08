from argparse import ArgumentParser, Namespace

def main():
    parser = ArgumentParser()

    parser.add_argument('--refDNA', help='Reference DNA that will be used to generate FASTQ of simulated aDNA')

    args: Namespace = parser.parse_args()


if __name__ == '__main__':
    main()