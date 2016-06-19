import pickle

def main():
	f = open("pragmatic_tips.txt")
	line_num = 0
	tip_to_description = {}

	lines = f.readlines()

	while line_num < len(lines):
		tip_to_description[lines[line_num]] = lines[line_num + 1]
		line_num += 2

	f.close()

	with open("pragmatic_tips.p", "wb") as p:
		pickle.dump(tip_to_description, p)

if __name__ == "__main__":
	main()