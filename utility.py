# All utility function definintions


# Function to count the number of words in the input
def countWords(data):
	words = data.split()
	return len(words)


# Function to count the number of paragraphs in the input
def countParas(data):
	lines = data.split('\n')
	paragraphs = [line for line in lines if line.strip()]
	return len(paragraphs)

# Function to count the number of characters in the input
def countCharactersOnly(data):
	characters = list(filter(lambda x: x != '\n' and x != ' ', data))
	return len(characters)

if __name__ == '__main__':
	response = (input('Enter your response: ')).lower()
	data = input('Enter the text: ')
	switcher = {
		"count words" : countWords,
		"count paras" : countParas,
		"count characters" : countCharactersOnly
	}

	action = switcher.get(response)
	result = action(data)
	print(result)
