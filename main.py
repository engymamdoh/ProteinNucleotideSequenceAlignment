#This file is a main file for project of Protein/Nucleotide Sequence Alignment. 
#It contains interface to the four parts which make a whole, those are the following:
#1. Global and local alignment of nucleotide sequences using given matrix as a score matrix 
#2. Global and local alignments of protein sequences using PAM and BLOSUM score matrices 
#3. Alignment of protein and nucleotide sequences, depending on the type
#4. Alignment of multiple sequences using CLUSTALW algorithm 
import third, fourth 
from first import global_alignment_nucleotide, local_alignment_nucleotide
from second import global_alignment_protein, local_alignment_protein

def sequence_chooser():
	print("Enter 1 for a file name or 2 for DNA/protein sequence:")
	a = input()
	if a not in {"1","2"}:
		print("Not a valid option.Try again.")
		return sequence_chooser()
	elif a == "1":
		print("Enter file name:")
		#try:
		#	data = input()
		#except FileNotFoundError:
		#	print("File does not exist. Try again.")
		#	return sequence_chooser()
		data = input()
		if(data.find('.txt') == -1):
			print("Not a valid option. Try again.")
			return sequence_chooser()
		else:
			return data
	else:
		print("Insert sequence:")
		#info = sequence_input_check()
		sequence = input()
		return sequence 

def sequence_input_check():
	sequence = input()
	for i in range(len(sequence)):
		if sequence[i] not in {"A","C","G","T","a","c","g","t"}:
			print("Not a valid sequence.Try again")
			return sequence_input_check()
	return sequence	

def alignment_chooser(opt):
	print("For global alignment type G, for local L:")
	a = input()
	if a not in ["L","G", "l", "g"]:
		print("Not a valid option. Try again.")
		return alignment_chooser(opt)
	elif a in ["G", "g"]:
		if opt == '1':
			print("Unesite niske za racunanje poravnanja")
			first = sequence_input_check()
			second = sequence_input_check()
			print(global_alignment_nucleotide(first, second))
		else:
			global_alignment_protein()
	elif a in ["L","l"]:
		if opt == '1':
			print("Unesite niske za racunanje poravnanja")
			first = sequence_input_check()
			second = sequence_input_check()
			print(local_alignment_nucleotide(first, second))
		else:
			print(local_alignment_protein())

def option_chooser(opt):
	valid = set(['1','2','3','4','5'])
	if opt not in valid:
		print("Not a valid option. Try again.")
		return screen()
	elif opt in ["1","2"]:
		return alignment_chooser(opt)
	elif opt == '3':
		print("Option 3")
		first = sequence_chooser()
		second = sequence_chooser()
		return third.protein_nucleotide_alignment(first, second)
	elif opt == '4':
		print("Option 4")
	else:
		exit()
		
def screen():
	print("Choose one option of the following:\n \
		1. Global and local alignment of nucleotide sequences using given matrix as a score matrix\n \
		2. Global and local alignments of protein sequences using PAM and BLOOSUM score matrices\n \
		3. Alignment of protein or nucleotide sequences, depending on the type\n\
		4. Alignment of multiple sequences using CLUSTALW algorithm \n \
		5. Exit program")
	option = input()
	return option_chooser(option)

def main():
	screen()
	
if __name__ == "__main__":
	main()