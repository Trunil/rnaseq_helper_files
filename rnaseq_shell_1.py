'''
For writing shell commands for RNA-seq analysis

- Map reads
- convert sam to bam
- Assemble transcripts

The script was supposed to directly give instruction to shell but multiple commands were run simultaneously resulting in errors.
Therefore, this script now generates the shell script that can be run through the terminal.

'''

import os


def get_command(command, name):
    '''
    Modifies command template to include sample name.
    '''

    command_split = command.split('sample_name')
    ret_command = name.join(command_split)

    return ret_command




# list of sample names
sample_names = ["ERR188044",
                "ERR188104",
                "ERR188234",
                "ERR188245",
                "ERR188257",
                "ERR188273",
                "ERR188337",
                "ERR188383",
                "ERR188401",
                "ERR188428",
                "ERR188454",
                "ERR204916"]


# command templates, the sample id is replaced with "sample_name"

cmnd1 = "hisat2 -p 4 --dta -x chrX_data/indexes/chrX_tran -1 chrX_data/samples/sample_name_chrX_1.fastq.gz -2 chrX_data/samples/sample_name_chrX_2.fastq.gz -S output/o_hisat2/sample_name_chrX.sam"

cmnd2 = "samtools sort -@ 4 -o output/o_samtools/sample_name_chrX.bam output/o_hisat2/sample_name_chrX.sam"

cmnd3 = "stringtie -p 4 -G chrX_data/genes/chrX.gtf -o output/o_stringtie/sample_name_chrX.gtf output/o_samtools/sample_name_chrX.bam -l sample_name"


with open('rnaseq_shell_commands_1.sh', 'w') as f:
    for name in sample_names:
        
        # get proper shell commands
        cmd1 = get_command(cmnd1, name)
        
        cmd2 = get_command(cmnd2, name)
        cmd3 = get_command(cmnd3, name)

        # write them to file
        echo_line = "echo " + name
        
        print(echo_line, file=f)
        print(cmd1, file=f)
        print(cmd2, file=f)
        print(cmd3, file=f)
        
        print("echo Done", file=f)
    


    
