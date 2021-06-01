import random
print("Press enter to get new line. Press space then enter to quit.")
while True:
    with open("Adj.txt") as adj:
        selectadj = adj.readlines()
    with open("curwords.txt") as curs:
        selectcurs = curs.readlines()
    with open("nouns.txt") as noun:
        selectnoun = noun.readlines()
    finalsentence = (random.choice(selectadj), random.choice(selectcurs), random.choice(selectnoun))
    def fix(sentence):
        fin = ' '.join(sentence)
        return fin
    fin = fix(finalsentence)
    fin.split('\n')
    fin = [i for i in fin if i not in ('\n')]
    final = ''.join(map(str, fin))
    print(f"You {final}!")
    q = input("").lower()
    if q == (' '):
        break
    continue