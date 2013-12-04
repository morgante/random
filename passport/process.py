newfile = 'new-list.txt';
oldfile = 'old.txt';
finalfile = 'new.txt';

new = [line.strip() for line in open(newfile)];
old = [line.strip() for line in open(oldfile)];

print len(new);

for net in old:
	if net in new:
		new.remove(net);

print len(new);

for net in new:
	print net;