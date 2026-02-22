def CountNucFrequency(seq):
  #Takes a DNA sequence and returns a dictionary with the count of each nucleotide
  FreqDict = {"A":0, "C":0, "G":0, "T":0}
  for nuc in seq:
    FreqDict[nuc] += 1
  return FreqDict

DNAString = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC" #insert nucleotide sequence here
result = CountNucFrequency(DNAString)
print(result)