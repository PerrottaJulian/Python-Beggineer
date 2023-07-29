import time;
max = 0
mcw = str();

flag = True;
while flag:
    try:
        file = input("File: ");
        fhand = open(file.strip())
        flag = False
    except:
        print("File doesnt exist.")
        time.sleep(1);

counts = dict();
for line in fhand:
    words = line.split();
    for word in words:
        counts[word] = counts.get(word, 0)+1;

lst = sorted([(v,k) for k,v in counts.items()], reverse=True);

c = 0;
for v,k in lst[:10]: c += 1; print(f"Common Word {c}: {k}({v})");

