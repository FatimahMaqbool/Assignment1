def checkValidDFA(s):
    initial_state = 0
 
    final_state = 0
 
    previous_state = 0
 
    for i in range(len(s)):
         
        if ((s[i] == '0' and previous_state == 0) or
            (s[i] == '1' and previous_state == 3)):
            final_state = 1
        elif ((s[i] == '0' and previous_state == 3) or
              (s[i] == '1' and previous_state == 0)):
            final_state = 2
        elif ((s[i] == '0' and previous_state == 1) or
              (s[i] == '1' and previous_state == 2)):
            final_state = 0
        elif ((s[i] == '0' and previous_state == 2) or
              (s[i] == '1' and previous_state == 1)):
            final_state = 3
 
        previous_state = final_state
 
    if (final_state == 3):
        print("Accepted")
         
    else:
        print("Not Accepted")
 
if __name__ == '__main__':
     
    s = "010011"
 
    checkValidDFA(s)