# Towers of Hanoi
'''
n = # of disks

if n == 1:
    move disk from post 1 to post 3
if n == 2:
    move top disk to post 2
    bottom disk to post 3
    disc from post 2 to post 3
if n == 3:
    post 1 to post 3
    post 1 to post 2
    post 3 to post 2
    post 1 to post 3
    post 2 to post 1
    post 2 to post 3
    post 1 to post 3

hanoi(3, 1, 3) # Take 3 discs from peg 1 to peg 3
    hanoi(2, 1, 2) # Take 2 discs from peg 1 to peg 2
    move(3, 1, 3) # Move disc 3 from  post 1 to post 3
    hanoi(2, 2, 3) # Take 2 discs from peg 2 to peg 3
    ...
'''
def move(disk_number, from_peg, to_peg):
    print("Move disk " + str(disk_number) + " from peg " + str(from_peg) + " to peg " + str(to_peg) + ".")

def hanoi(n, start_peg, end_peg): # 3 params
    # What is the base case?
    if n == 1:
        move(n, start_peg, end_peg)
    else:
        spare_peg = 6 - (start_peg + end_peg) # Find spare peg so we know what's free to move to
        hanoi(n - 1, start_peg, spare_peg)
        move(n, start_peg, end_peg)
        hanoi(n - 1, spare_peg, end_peg)

hanoi(4, 1, 3) # n = 3
# spare = 2
    #(hanoi, 2, 1, 2) 
        # spare = 3
        # hanoi(1, 1, 3)
            # move disk 1 from peg 1 to peg 3
        # move disk 2 from peg 1 to peg 2
        # hanoi(1, 3, 2)
        # spare = 1
            # move disk 1 from peg 3 to peg 2
#move(disk 3, from peg 1, to peg 3)
    # hanoi(2, 2, 3)
        # spare = 1
        # hanoi(1, 2, 1)
            # move disk 1 from peg 2 to peg 1
        # move disk 2 from peg 2 to peg 3
        # hanoi(1, 1, 3)
            # move disk 1 from peg 1 to peg 3