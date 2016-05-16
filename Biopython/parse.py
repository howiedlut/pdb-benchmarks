# Benchmark the parsing of a PDB file given as an argument

import sys
import time
from Bio.PDB import PDBParser

pdb_filepath = sys.argv[1]
runs = 100

parser = PDBParser()
times = []

for i in range(runs):
    start = time.time()
    struc = parser.get_structure("", pdb_filepath)
    elapsed = time.time() - start
    times.append(elapsed)

print "Average time per run:", sum(times) / runs
