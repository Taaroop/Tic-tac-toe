
import turtle

def draw_grid():
    turtle.home()
    for i in range(4):
        turtle.forward(240)
        turtle.right(90)
    for j in range(1, 3):
        turtle.pendown()
        turtle.forward(j*80)
        turtle.right(90)
        turtle.forward(240)
        turtle.penup()
        turtle.home()
    for k in range(1, 3):
        turtle.pendown()
        turtle.right(90)
        turtle.forward(k*80)
        turtle.left(90)
        turtle.forward(240)
        turtle.penup()
        turtle.home()

def goto_center(string):
    num = string[1]
    num = int(num)
    letter = string[0]
    forward = (80*num) - 40
    if letter == "A":
        i = 1
    elif letter == "B":
        i = 2
    else:
        i = 3
    forward_2 = (80*i) - 40
    turtle.home()
    turtle.setheading(0)
    turtle.penup()
    turtle.forward(forward)
    turtle.right(90)
    turtle.forward(forward_2)
        

def draw_cross():
    c_pos = turtle.pos()
    for m in range(1, 5):
        turtle.penup()
        turtle.goto(c_pos)
        turtle.setheading(0)
        turtle.pendown()
        turtle.left((90*m)-45)
        turtle.forward(30)
    turtle.penup()
    turtle.home()

def draw_circle():
    turtle.setheading(270)
    turtle.penup()
    turtle.forward(30)
    turtle.setheading(0)
    turtle.pendown()
    turtle.circle(30)
    turtle.penup()
    turtle.home()
    

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
    m_type = ""
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
        m_type = "A"
    if B_count == 3:
        match_count += 1
        m_type = "B"
    if C_count == 3:
        match_count += 1
        m_type = "C"
    if count_1 == 3:
        match_count += 1
        m_type = "1"
    if count_2 == 3:
        match_count += 1
        m_type = "2"
    if count_3 == 3:
        match_count += 1
        m_type = "3"
        
    a = 0
    b = 0
    if find("A1", li) == True and find("B2", li) == True and find("C3", li) == True:
        a = 1
    if find("A3", li) == True and find("B2", li) == True and find("C1", li) == True:
    	b = 1
    if a == 1:
        match_count += 1
        m_type = "c"
    if b == 1:
        match_count += 1
        m_type = "d"
    	
    output = str(match_count) + m_type
    return output


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

draw_grid()

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
    match_ini = matching_check(player1)
    match = int(match_ini[0])
    goto_center(s_pos_1)
    draw_cross()
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
    match_2_ini = matching_check(player2)
    match_2 = int(match_2_ini[0])
    goto_center(s_pos_2)
    draw_circle()
    if match_2 > 0:
        deter2 += 1
        print("Player 2 WINS!")
        break

if deter1 == 0 and deter2 == 0:
    print("Draw!")
else:
    if deter1 == 1:
        v_type_ini = matching_check(player1)
        v_type = v_type_ini[1]
        turtle.pensize(3)
        if v_type == "A" or v_type == "B" or v_type == "C":
            goto_center(v_type + "1")
            turtle.setheading(0)
            turtle.pendown()
            turtle.forward(160)
        elif v_type == "1" or v_type == "2" or v_type == "3":
            goto_center("A" + v_type)
            turtle.setheading(270)
            turtle.pendown()
            turtle.forward(160)
        elif v_type == "c":
            goto_center("A1")
            turtle.setheading(0)
            turtle.right(45)
            turtle.pendown()
            turtle.forward(226)
        elif v_type == "d":
            goto_center("A3")
            turtle.setheading(180)
            turtle.left(45)
            turtle.pendown()
            turtle.forward(226) 

        
    elif deter2 == 1:
        v_type_ini = matching_check(player2)
        v_type = v_type_ini[1]
        turtle.pensize(3)
        if v_type == "A" or v_type == "B" or v_type == "C":
            goto_center(v_type + "1")
            turtle.setheading(0)
            turtle.pendown()
            turtle.forward(160)
        elif v_type == "1" or v_type == "2" or v_type == "3":
            goto_center("A" + v_type)
            turtle.setheading(270)
            turtle.pendown()
            turtle.forward(160)
        elif v_type == "c":
            goto_center("A1")
            turtle.setheading(0)
            turtle.right(45)
            turtle.pendown()
            turtle.forward(226)
        elif v_type == "d":
            goto_center("A3")
            turtle.setheading(180)
            turtle.left(45)
            turtle.pendown()
            turtle.forward(226)

turtle.penup()
turtle.home()
        
        


    
