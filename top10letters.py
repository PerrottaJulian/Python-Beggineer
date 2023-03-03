import time;
max = 0
mcw = str();

flag = True;
while flag is True:
    try:
        file = input("File: ");
        fhand = open(file)
        flag = False
    except:
        print("File doesnt exist.")
        time.sleep(1);

counts = dict();
for line in fhand:
    words = line.split();
    for word in words: 
        for letter in word:
            letter = letter.lower()
            counts[letter] = counts.get(letter, 0) + 1

lst = sorted([(v,k) for k,v in counts.items()], reverse=True);

c = 0;
for v,k in lst[:10]: 
    c += 1;
    print(f"Common Letter {c}: {k} ({v})");

