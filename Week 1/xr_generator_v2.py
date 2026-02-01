import random


# LIST OF XR ELEMENTS 

with open ('environments.txt', 'r') as e_file:
	envs = e_file.read().splitlines()

with open ('features1.txt', 'r') as f1_file:
	fea1 = f1_file.read().splitlines()

with open ('features2.txt', 'r') as f2_file:
	fea2 = f2_file.read().splitlines()

with open ('adjs.txt', 'r') as ad_file:
	adjs = ad_file.read().splitlines()


# GENERATE A XR SCENE 

def generate_xr_scene():
	env = random.choice(envs)
	feature = random.choice(fea1)
	feature2 = random.choice(fea2)
	adj = random.choice(adjs)
	description = f"A {adj} {env} with {feature} and {feature2}."
	return description


# VALIDATE USER INPUT (THEME) WITH THE LISTS OF LOWERED TERMS

def user_theme(theme):
	locase_theme = theme.lower()
	locase_envs = [e.lower() for e in envs]
	locase_fea1 = [f1.lower() for f1 in fea1]
	locase_fea2 = [f2.lower() for f2 in fea2]
	locase_adjs = [a.lower() for a in adjs]

	if (any(locase_theme in e for e in locase_envs) or any(locase_theme in f1 for f1 in locase_fea1) or any(locase_theme in f2 for f2 in locase_fea2) or any(locase_theme in adjs for adjs in locase_adjs)):
		return True
	return False

###English: "For each item 'e' in the list 'locase_envs', check if 'locase_theme' is a substring inside 'e', and yield True or False for that check."###



# MAIN LOGIC: Reprompt until valid theme, then generate 9 scenes

valid = False
while not valid: 

	theme = input('Type a keyword to get XR themes: ' )
	if user_theme(theme):
		valid = True

#THE FILE PRINTER WAS PUT RIGHT BEFORE THE FOR LOOP SO IT RUNS ONLY IF THEME IS VALID.
# WITH OPEN LINE opens a file named that way or create if does not exist. 'w' allows the file to be written.

		with open('scenes.txt', 'w') as outfile:


#The loop is indented under the with block, so everything inside it has access to the open file (outfile)		
# GENERATE 9 EXAMPLES ONCE VALID
			for _ in range (9):
				scene = generate_xr_scene()
				outfile.write(scene + '\n')
				print(scene)


#.write is a built-in method (function) of file objects in Python. It's called on outfile (the file we opened) and tells it to add the provided text to the file. 
#(scene + '\n'): This concatenates (joins) the scene string with a newline character ('\n'). The newline ensures each scene goes on its own line in the file, making it readable (like separating paragraphs). Without '\n', all 9 scenes would smoosh together into one long line. (Spot on—it's for separating lines!)




	else: 
		print('You can try typing: Cyborgs, people with cyber parts, flying vehicles, floating roads, immersive, crowded, quiet, romantic, touristy, desertic, colorful')
	
	





