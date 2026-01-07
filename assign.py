import random

# Lists of XR elements

environments = ["VR forest", "AR city", "mixed reality ocean", "futuristic space station"]
ai_features = ["floating holograms", "intelligent NPCs", "gesture-based controls", "voice-activated assistants"]
adjectives = ["mysterious", "vibrant", "high-tech", "immersive"]

def generate_xr_scene():
	env = random.choice(environments)
	feature = random.choice(ai_features)
	adj = random.choice(adjectives)
	description = f"A {adj} {env} with {feature}."
	return description

def user_input():
	input('Type a keyword to get 3 scenarios / variations: ')

print(user_input())


# Loop to generate 3 scenarios
for lol in range(3):
	print(generate_xr_scene())



