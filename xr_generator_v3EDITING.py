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


class XRGenerator:
    def __init__(self, envs, fea1, fea2, adjs):  # (Step: Constructor—store lists as attributes on self)
        self.envs = envs
        self.fea1 = fea1
        self.fea2 = fea2
        self.adjs = adjs

    def random_env(self):
        return random.choice(self.envs)  # (Uses self.envs—object's own data)

    def random_feature1(self):
        return random.choice(self.fea1)

    def random_feature2(self):
        return random.choice(self.fea2)

    def random_adj(self):
        return random.choice(self.adjs)

    def generate_scene(self):
        env = self.random_env()  # (Calls object's own methods)
        feature = self.random_feature1()
        feature2 = self.random_feature2()
        adj = self.random_adj()
        description = f"A {adj} {env} with {feature} and {feature2}."
        return description

    # Converted from user_theme() (Step: Now a method—uses self's lists for validation)
    def validate_theme(self, theme):
        locase_theme = theme.lower()
        locase_envs = [e.lower() for e in self.envs]  # (Uses self.envs)
        locase_fea1 = [f1.lower() for f1 in self.fea1]
        locase_fea2 = [f2.lower() for f2 in self.fea2]
        locase_adjs = [a.lower() for a in self.adjs]

        if (any(locase_theme in e for e in locase_envs) or 
            any(locase_theme in f1 for f1 in locase_fea1) or 
            any(locase_theme in f2 for f2 in locase_fea2) or 
            any(locase_theme in a for a in locase_adjs)):  # (Fixed variable name in last any())
            return True
        return False
