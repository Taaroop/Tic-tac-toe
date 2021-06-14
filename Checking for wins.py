
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
