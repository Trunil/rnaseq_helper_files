"""
Script to generate bash script for estimating transcript abundances and table counts for ballgown.

"""

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


with open('rnaseq_est_trans_abundances.sh', 'w') as f:
    for name in sample_names:
        write_str = f"stringtie -e -B -p 4 -G output/stringtie_merged/stringtie_merged.gtf -o output/for_ballgown/{name}/{name}_chrX.gtf output/o_samtools/{name}_chrX.bam"
        
        print(write_str, file=f)
        
