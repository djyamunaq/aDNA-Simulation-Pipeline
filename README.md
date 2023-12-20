# aDNA-Simulation-Pipeline
Pipeline for simulation of aDNA (.fq) based on reference DNA (.fa). Program works as a wrapper for Gargammel, easing the usage for generation of simulated aDNA. 

## Description
The aDNA Simulation Pipeline (Simpipe) is a tool based on Gargammel thought to make easier to generate samples of ancient DNA based on a reference DNA. 
Simpipe installs all the necessary dependencies and deals with the files and folders structures needed to run Gargammel*. After the .fq files are generated, the pipeline collapses them from paired-ended reads into single-ended reads using the program AdapterRemoval*.
The user only has to provide the input fasta reference file and, optionally, the output directory:

```
$ sim --refDNA <reference mtDNA> --output <output directory [Default: ./]>
```

Inside the output directory, if the pipeline runs successfully, will be found a .fq file with the reads.

The tool is hosted in github (https://github.com/djyamunaq/aDNA-Simulation-Pipeline.git), where is possible to find the installation guide and basic usage instructions.

*Include references when passing it to latex

```
```


## Downloading:
```
$ git clone https://github.com/djyamunaq/aDNA-Simulation-Pipeline.git
```

## Installation:
The file install.sh is responsible for installing necessary dependencies and setup to run the pipeline. It's necessary to have *sudo* access in order to install the package and all the dependencies.

```
$ cd aDNA-Simulation-Pipeline
$ ./install.sh
```

## Usage:
The pipeline expects a fasta format file (.fa) with the mtDNA reference as input and will output a fastq format file (.fq) with the simulated aDNA as output.
After installation, it is possible to run the program with the *sim* command in any directory.
```
$ sim --refDNA <reference mtDNA> --output <output directory [Default: ./]>
```
Use flag -h or --help to check on how to use the program.
```
$ sim -h
```