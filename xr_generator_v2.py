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

	if (locase_theme in locase_envs or locase_theme in locase_fea1 or locase_theme in locase_fea2 or locase_theme in locase_adjs):
		return True
	return False
 

# MAIN LOGIC: Reprompt until valid theme, then generate 9 scenes

valid = False
while not valid: 

	theme = input('Type a keyword to get XR themes: ' )
	if user_theme(theme):
		valid = True


# GENERATE 9 EXAMPLES ONCE VALID

		for _ in range (9):
			print(generate_xr_scene())
	else: 
		print('You can try typing: Cyborgs, people with cyber parts, flying vehicles, floating roads, immersive, crowded, quiet, romantic, touristy, desertic, colorful')
	







