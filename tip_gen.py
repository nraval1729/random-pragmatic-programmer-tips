import pickle
import random

def main():
	with open("pragmatic_tips.p", "rb") as p:
		tip_to_description = pickle.load(p)

	random_tip = random.choice(tip_to_description.keys())

	print "*******************************************"
	print "Tip: ", random_tip
	print "Summary: ", tip_to_description[random_tip], "*******************************************"

if __name__ == "__main__":
	main()

