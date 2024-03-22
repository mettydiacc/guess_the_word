from random_word import RandomWords
import os
randWord = RandomWords()

lives: int = 5
start: int = 0
guessed_chars = []
other_chars   = []
clear = lambda: os.system('cls')

def get_random() -> str:
	return str(randWord.get_random_word())

def check_draw_word(word: str, charr: str) -> int:
	if len(charr) >= 2:
		print("You must insert only one char at once!")
		return 0
	global lives, guessed_chars
	total_guess: int = 0

	clear()

	if charr not in word and charr not in guessed_chars and charr not in other_chars:
		lives -= 1
		other_chars.append(charr)
	elif charr in other_chars:
		print(f"You've already guessed '{charr}', try again.")
	elif charr in guessed_chars:
		print(f"You've already guessed '{charr}', try again.")
	else:
		guessed_chars.append(charr)

	print(f"{guessed_chars} ; {lives = }\nchars given: {other_chars}")

	for char in word:
		if char in guessed_chars:
			print(f"{char}", end=" ")
			total_guess += 1	
		else:
			print("_", end=" ")
	print()
	return total_guess

rword: str = ""
while (lives > 0):
	if start == 0:
		rword = get_random()
		start += 1

	input_char: str = input("Insert a char: ")
	res = check_draw_word(rword, input_char)

	if res >= len(rword):
		clear()
		print(	f"""\n\n
			╔═════════════════════╗\n
			║	You Won !     ║\n
			╚═════════════════════╝\n\n
			The word was: {rword}!
			""")
		break

if lives <= 0: print(f"You loose, the word was: {rword}")