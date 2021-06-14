
def find(string, li):
    string_2 = ""
    for n in li:
        string_2 += n
        result = string_2.find(string)
    if result != -1:
        return True
    else:
        return False

def matching_check(li):
    A_count = 0
    B_count = 0
    C_count = 0
    count_1 = 0
    count_2 = 0
    count_3 = 0
    match_count = 0
    for item in li:
        if item.find("A") != -1:
           A_count += 1
        if item.find("B") != -1:
           B_count += 1
        if item.find("C") != -1:
           C_count += 1
        if item.find("1") != -1:
           count_1 += 1
        if item.find("2") != -1:
           count_2 += 1
        if item.find("3") != -1:
           count_3 += 1

    if A_count == 3:
        match_count += 1
    if B_count == 3:
        match_count += 1
    if C_count == 3:
        match_count += 1
    if count_1 == 3:
        match_count += 1
    if count_2 == 3:
        match_count += 1
    if count_3 == 3:
        match_count += 1
        
    a = 0
    b = 0
    if find("A1", li) == True and find("B2", li) == True and find("C3", li) == True:
        a = 1
    if find("A3", li) == True and find("B2", li) == True and find("C1", li) == True:
    	b = 1
    if a == 1 or b == 1:
    	match_count += 1
    	
    return match_count



p1 = ["A", "B", "C"]
p2 = ["1", "2", "3"]
p = []
for x in p1:
    for y in p2:
        p.append(x+y)

player1 = []
player2 = []

deter1 = 0
deter2 = 0

game_over = False

count = 0
while game_over == False:
    
    s_pos_1 = str(input("Enter the coordinate, player 1: "))
    if s_pos_1 in p:
        p.remove(s_pos_1)
    else:
        while s_pos_1 not in p:
            print("Invaid coordinate!")
            s_pos_1 = str(input("Enter the coordinate again, player 1: "))
    
        p.remove(s_pos_1)
    player1.append(s_pos_1)
    match = matching_check(player1)
    if match > 0:
        deter1 += 1
        print("Player 1 WINS!")
        break
    
    count += 1
    if count == 5:
        game_over = True
        continue
        
    s_pos_2 = str(input("Enter the coordinate, player 2: "))
    if s_pos_2 in p:
        p.remove(s_pos_2)
    else:
        while s_pos_2 not in p:
            print("Invaid coordinate")
            s_pos_2 = str(input("Enter the coordinate again, player 2: "))
        p.remove(s_pos_2)
    player2.append(s_pos_2)
    match_2 = matching_check(player2)
    if match_2 > 0:
        deter2 += 1
        print("Player 2 WINS!")
        break

if deter1 == 0 and deter2 == 0:
    print("Draw!")
