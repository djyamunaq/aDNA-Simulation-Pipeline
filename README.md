# aDNA-Simulation-Pipeline
Pipeline for simulation of aDNA (.fq) based on reference DNA (.fa). Program works as a wrapper for Gargammel, easing the usage for generation of simulated aDNA. 

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