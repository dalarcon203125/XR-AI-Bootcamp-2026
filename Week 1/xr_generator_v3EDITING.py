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

