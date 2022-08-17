import itertools

open('out1.txt','w').write(
    ''.join(
        l for l in open(
            'front.txt') if l.strip())) 
open('out2.txt','w').write(
    ''.join(
        l for l in open(
            'back.txt') if l.strip())) 

f_1 = open("out1.txt", "r")
with open("deck1.txt", "w") as w:
    for x in f_1:
        times = int(x[0:2])
        card = x[2:]
        clean_card = card.replace(",", " ")
        while times > 0:
            w.write(f'"{clean_card.strip()}"\n')
            times -=1
            
f_2 = open("out2.txt", "r")
with open("deck2.txt", "w") as w:
    for x in f_2:
        times = int(x[0:2])
        card = x[2:]
        clean_card = card.replace(",", " ")
        while times > 0:
            w.write(f'"{clean_card.strip()}"\n')
            times -=1
            
filenames = ['deck1.txt', 'deck2.txt']

with open('deck1.txt') as src1, open('deck2.txt', 'r') as src2, open('merged.csv', 'w') as dst:
    dst.write(f"Quantity, Front, Back\n")
    for line_from_first, line_from_second in itertools.zip_longest(src1, src2):
        if line_from_first is not None:
            dst.write(f"1, {line_from_first.strip()}, {line_from_second.strip()}\n")
        # if line_from_second is not None:
        #     dst.write(line_from_second)

  
# # Open file3 in write mode
# with open('final_deck.txt', 'w') as outfile:

  
#     # Iterate through list
#     for names in filenames:
  
#         # Open each file in read mode
#         with open(names) as infile:
  
#             # read the data from deck1 and
#             # file2 and write it in file3
#             outfile.write(infile.read())
  
#         # Add '\n' to enter data of file2
#         # from next line
#         outfile.write("\n")
