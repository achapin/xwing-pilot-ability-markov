import os
import json
import random

abilities = []
markov = {}
replacements = [
	[",",""],
	[".",""],
	["[Bullseye Arc]","[Bullseye-Arc]"],
	["[Critical Hit]","[Critical-Hit]"],
	["[Left Arc]","[Left-Arc]"],
	["[Right Arc]","[Right-Arc]"],
	["[Single Turret Arc]","[Single-Turret-Arc]"],
	["[Front Arc]","[Front-Arc]"],
	["[Rear Arc]","[Rear-Arc]"],
	["[Full Front Arc]","[Full-Front-Arc]"],
	["[Full Rear Arc]","[Full-Rear-Arc]"],
	["([Segnor's Loop Left] or [Segnor's Loop Right])",""],
	["([Turn Left] or [Turn Right])",""],
	["[[Tallon Roll Left] or [Tallon Roll Right]]",""],
	["[Bank Left]","[Bank-Left]"],
	["[Bank Left]","[Bank-Right]"],
	["[Turn Left]","[Turn-Left]"],
	["[Turn Right]","[Turn-Right]"],
]
first_word_totals = {}
first_words = []
firstWordKey = "FIIIIRSTWOOOROD"
lastWordKey = "LAAAASTWOOOORD"

def create_random_ability():
	line = []
	word = random.choice(first_words)
	while word != lastWordKey:
		line.append(word)
		if word in markov:
			word_choices = []
			word_weights = []
			for next_word in markov[word]:
				if(next_word != firstWordKey):
					word_choices.append(next_word)
					word_weights.append(markov[word][next_word])
			word = random.choices(word_choices, word_weights)[0]
		else:
			word = lastWordKey
	print(" ".join(line))

def convert_markov_to_probabilities():
	for word in markov:
		total = 0
		for next_word in markov[word]:
			if(next_word == firstWordKey):
				first_word_totals[word] = markov[word][next_word]
				first_words.append(word)
			else:
				total += markov[word][next_word]
		for next_word in markov[word]:
			if(next_word != firstWordKey):
				markov[word][next_word] = markov[word][next_word] / total

def process_abilities():
	for line in abilities:
		for replacement in replacements:
			line = line.replace(replacement[0], replacement[1])
		splitLine = line.split(" ")
		index = 0
		while index < len(splitLine):
			process_ability_line(index, splitLine)
			index += 1

def process_ability_line(index, wordArray):
	word = wordArray[index]
	firstWord = index == 0
	lastWord = index == len(wordArray) - 1
	if lastWord:
		if word not in markov:
			markov[word]={lastWordKey:1}
		else:
			if lastWordKey in markov[word]:
				markov[word][lastWordKey] += 1
			else:
				markov[word][lastWordKey] = 1
		return
	nextWord = wordArray[index + 1]
	if word not in markov:
		markov[word] = {nextWord:1}
		if firstWord:
			markov[word][firstWordKey] = 1
	else:
		if nextWord in markov[word]:
			markov[word][nextWord] += 1
		else:
			markov[word][nextWord] = 1
		if firstWord:
			if firstWordKey in markov[word]:
				markov[word][firstWordKey] += 1
			else:
				markov[word][firstWordKey] = 1

def process_file(file):
	openfile = open(file)
	loadedjson = json.load(openfile)
	if "pilots" not in loadedjson:
		return
	for pilot in loadedjson["pilots"]:
		if "ability" in pilot:
			abilities.append(pilot["ability"])

def process_directory(directory):
	for r, d, f in os.walk(directory):
		for subdirectory in d:
			process_directory(subdirectory)
		for file in f:
			if file.endswith(".json"):
				process_file(os.path.join(r, file))

def main():
	thisdir = os.getcwd()
	process_directory(thisdir)
	process_abilities()
	with open('abilities.txt', mode='wt', encoding='utf-8') as myfile:
		myfile.write('\n'.join(abilities))
	with open('markov.json', 'w') as fp:
		json.dump(markov, fp)
	convert_markov_to_probabilities()
	val = 100
	while val > 0:
		create_random_ability()
		val -= 1

if __name__ == "__main__":
	main()