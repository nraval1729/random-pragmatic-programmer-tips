import pickle
import random
import sys

def main():
	with open(sys.argv[1], "rb") as p:
		tip_to_description = pickle.load(p)

	random_tip = random.choice(tip_to_description.keys())

	print "*******************************************"
	print "Tip: ", random_tip
	print "Summary: ", tip_to_description[random_tip], "*******************************************"

if __name__ == "__main__":
	main()

