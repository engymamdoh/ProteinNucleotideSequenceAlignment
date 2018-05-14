#This file contains alignment of protein and nucleotide sequences. 
#Firstly, we recognize if sequence is a nucleotide or a protein.
#Secondly, from nucleotide sequences we extract potential coding subsequence (from START to STOP codon). 
#Thirdly, codons are translated into aminoacids. 
#Finally, protein sequences are aligned. 

def file_opener(filename):
	try:	
		dna = open(filename, 'r')
		content = dna.read()
		content = content.replace('\n','')
		return content
	except FileNotFoundError:
		print("The file does not exist.")
		exit()

def rna_file_writer(content):
	print("Do you want to have RNA info written in a file?")
	answer = input()
	if answer not in ["Yes","y", "yes", "No", "n", "no"]:
		print("Not a valid answer. Try again.")
		return rna_file_writer(content)
	elif answer in ["Yes","y", "yes"]:
		print("Insert file name:")
		filename = input()
		filename.append(".txt")
		print(filename)
		rna = open(filename, 'w')
		rna.write(content)
		print("Writing in " + filename + "successfully finished.")
		return
	else:
		return

def protein_nucleotide_alignment(first, second):
	first = protein_or_nucleotide(first)
	second = protein_or_nucleotide(second)
	if first == -1 and second == -1:
		print("Both proteins.")
	else:
		print(first)
		print(second)

def protein_or_nucleotide(sequence):
	p = 0
	if sequence.find('.txt') != -1:
		data = file_opener(sequence)
		return protein_or_nucleotide(data)
	for i in range(len(sequence)):
		if sequence[i] in {"A","C","G","T","a","c","g","t"}:
			p += 1
	if p == len(sequence):
		print("Sequence1 : " + sequence)
		print("Nucleotide. It will be translated into aminoacid.")
		return dna_to_rna(sequence)
	else:
		print("Sequence2 : " + sequence)
		print("Protein.")
		return -1
				
#DNA to RNA
def dna_to_rna(dna):
	content = dna.replace('T','U')
	rna_file_writer(content)
	print("DNA to RNA transcription completed.")
	return rna_to_aa(content)

#RNK to AA
def rna_to_aa(rna):
	map = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
	    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
	    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
	    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
	    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
	    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
	    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
	    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
	    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
	    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
	    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
	    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
	    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
	    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
	    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
	    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}
		
	start = rna.find('AUG')
	protein_sequence = ""
	while start + 2 < len(rna):
		codon = rna[start:start+3]
		if map[codon] == "STOP":
			break;
		protein_sequence += map[codon]
		start += 3
	print(protein_sequence)	
	return protein_sequence