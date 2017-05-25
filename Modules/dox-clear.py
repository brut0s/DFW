import os

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def next():
	raw_input('Press enter to continue...')
