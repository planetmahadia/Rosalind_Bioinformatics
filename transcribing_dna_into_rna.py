def transcribe(dna_sequence):
    #Transcribes DNA string into RNA by replacing all occurrences of T with U
    return dna_sequence.replace('T', 'U')

sample_dna = 'GATGGAACTTGACTACGTAAATT'
new_rna = transcribe(sample_dna)
print(new_rna)
