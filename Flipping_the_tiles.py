from tkinter import *
import random
from tkinter import ttk
import time          
print("\n\n\n                                   \n\n\n")
print("\t*0* * 0 * 0 * 0 * 0 * 0 * 0 * 0 * 0 * 0 * 0\n")
print("\t*0* *      FLIPPING THE TILES           * 0\n")
print("\t*0* * 0 * 0 * 0 * 0 * 0 * 0 * 0 * 0 * 0 * 0\n")
print("\n\n                                       \n\n")


global moves1

def play():
    
    print("Enter your name:")
    global s
    s=input();
    print("\n\t\t\tEnter Level:\n\n");
    print("\t\t\t1.Easy\n");
    print("\t\t\t2.medium\n");
    print("\t\t\t3.Hard\n");
    print("\t\t\tEnter 4 to exit\n");
    print("\t\t\tEnter 5 to go bck to main menu:\n")
    print("\t\tEnter your choice:\n\n")
    option = int(input());
    
    if(option==1):
        PuzzleWindow=Tk()
        PuzzleWindow.title('Flipping the tiles')
        tabs = ttk.Notebook(PuzzleWindow) 
        easy= ttk.Frame(tabs)
        tabs.add(easy, text ='Easy') 
        tabs.pack(expand = 1, fill ="both") 
        global base1,ans1,board1,moves1,prev1
        

       

        def draw(a,l,m):
            
            global base1
            if a=='A':
                d=base1.create_rectangle(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='red')
            elif a=='B':
                d=base1.create_rectangle(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='yellow')
            elif a=='C':
                d=base1.create_rectangle(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='blue')
            elif a=='D':
                d=base1.create_oval(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='red')
            elif a=='E':
                d=base1.create_oval(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='yellow')
            elif a=='F':
                d=base1.create_oval(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='blue')
            elif a=='G':
                d=base1.create_polygon(100*l+50,m*100+20,100*l+20,100*m+100-20,100*l+100-20,100*m+100-20,fill='red')
            elif a=='H':
                d=base1.create_polygon(100*l+50,m*100+20,100*l+20,100*m+100-20,100*l+100-20,100*m+100-20,fill='green')
        def quizboard():
            global base1,ans1,board1,moves1
            count=1
            for i in range(4):
                for j in range(4):
                    rec=base1.create_rectangle(100*i,j*100,100*i+100,100*j+100,fill="white")
                    if(board1[i][j]!='.'):
                        draw(board1[i][j],i,j)
                        count+=1
            if count==16:
                base1.create_text(200,450,text="No. of moves: "+str(moves1),font=('arial',20))
                
                with open("high_score.txt","a") as f:
                    f.write(s)
                    f.write(",")
                    f.write(str(moves1))
                    f.write("\n")
                      
                
                           
                
                    
     
        def call(event):
           
            global base1,ans1,board1,moves1,prev1
            i=event.x//100
            j=event.y//100
            if board1[i][j]!='.':
                return
            moves1+=1
            #print(moves)
            if(prev1[0]>4):
                prev1[0]=i
                prev1[1]=j
                board1[i][j]=ans1[i][j]
                quizboard()
            else:
                board1[i][j]=ans1[i][j]
                quizboard()
                if(ans1[i][j]==board1[prev1[0]][prev1[1]]):
                    print("matched")
                    prev1=[100,100]
                    quizboard()
                    return
                else:
                    board1[prev1[0]][prev1[1]]='.'
                    quizboard()
                    prev1=[i,j]
                    return
     
        base1=Canvas(easy,width=500,height=500)
        base1.pack()
         
        ans1 = list('AABBCCDDEEFFGGHH')
        random.shuffle(ans1)
        ans1 = [ans1[:4],
               ans1[4:8],
               ans1[8:12],
               ans1[12:]]
         
        base1.bind("<Button-1>", call)
         
        moves1=IntVar()
        moves1=0
         
        prev1=[100,100]
         
        board1=[list('.'*4) for count in range(4)]
        
        quizboard()
        
          
        
    elif(option==2):
        PuzzleWindow=Tk()
        PuzzleWindow.title('Flipping the tiles')
        tabs = ttk.Notebook(PuzzleWindow) 
        easy= ttk.Frame(tabs)
        window2= ttk.Frame(tabs)
        tabs.add(window2, text ='medium')
        tabs.pack(expand = 1, fill ="both") 
        global base2,ans2,board2,moves2,prev2
     
        def draw1(a,l,m):
        
            global base2
            if a=='A':
                d=base2.create_rectangle(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='red')
            elif a=='B':
                d=base2.create_rectangle(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='yellow')
            elif a=='C':
                d=base2.create_rectangle(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='blue')
            elif a=='D':
                d=base2.create_oval(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='red')
            elif a=='E':
                d=base2.create_oval(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='yellow')
            elif a=='F':
                d=base2.create_oval(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='blue')
            elif a=='G':
                d=base2.create_polygon(100*l+50,m*100+20,100*l+20,100*m+100-20,100*l+100-20,100*m+100-20,fill='red')
            elif a=='H':
                d=base2.create_polygon(100*l+50,m*100+20,100*l+20,100*m+100-20,100*l+100-20,100*m+100-20,fill='green')
            elif a=='I':
                d=base2.create_polygon(100*l+50,m*100+20,100*l+20,100*m+100-20,100*l+100-20,100*m+100-20,fill='yellow')
            elif a=='J':
                d=base2.create_polygon(100*l+50,m*100+20,100*l+20,100*m+100-20,100*l+100-20,100*m+100-20,fill='blue')
            elif a=='K':
                d=base2.create_polygon(100*l+50,m*100+20,100*l+20,100*m+100-20,100*l+100-20,100*m+100-20,fill='black')
            elif a=='L':
                d=base2.create_polygon(100*l+50,m*100+20,100*l+20,100*m+100-20,100*l+100-20,100*m+100-20,fill='orange')
            elif a=='M':
                d=base2.create_rectangle(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='black')
            elif a=='N':
                d=base2.create_rectangle(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='orange')
            elif a=='O':
                d=base2.create_rectangle(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='green')
            elif a=='P':
                d=base2.create_oval(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='black')
            elif a=='Q':
                d=base2.create_oval(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='orange')
            elif a=='R':
                d=base2.create_oval(100*l+20,m*100+20,100*l+100-20,100*m+100-20,fill='green')
            
    
        def puzzleboard2():
                global base2,ans2,board2,moves2
                count=1
                for i in range(6):
                    for j in range(6):
                        rec=base2.create_rectangle(100*i,j*100,100*i+100,100*j+100,fill="white")
                        if(board2[i][j]!='.'):
                            draw1(board2[i][j],i,j)
                            count+=1
                if count>36:
                    base2.create_text(300,650,text="No. of moves: "+str(moves2),font=('arial',20))
                    with open("high_score1.txt","a") as file:
                        
                        file.write(s)
                        file.write(",")
                        file.write(str(moves2))
                        file.write("\n")
                          
                
        def call2(event):
         
                global base2,ans2,board2,moves2,prev2
                i=event.x//100
                j=event.y//100
                if board2[i][j]!='.':
                    return
                moves2+=1
                if(prev2[0]>6):
                    prev2[0]=i
                    prev2[1]=j
                    board2[i][j]=ans2[i][j]
                    puzzleboard2()
                else:
                    board2[i][j]=ans2[i][j]
                    puzzleboard2()
                    if(ans2[i][j]==board2[prev2[0]][prev2[1]]):
                        prev2=[100,100]
                        puzzleboard2()
                        return
                    else:
                        board2[prev2[0]][prev2[1]]='.'
                        puzzleboard2()
                        prev2=[i,j]
                        return
        base2=Canvas(window2,width=1000,height=1000)
        base2.pack()
        ans2 = list('AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRR')
        random.shuffle(ans2)
        ans2 = [ans2[:6],
               ans2[6:12],
               ans2[12:18],
               ans2[18:24],
               ans2[24:30],
               ans2[30:]
               ]
        base2.bind("<Button-1>", call2)
        moves2=IntVar()
        moves2=0
        prev2=[100,100]
        board2=[list('.'*6) for count in range(6)]
        puzzleboard2()

       
    elif(option==3):
        PuzzleWindow=Tk()
        PuzzleWindow.title('Flipping the tiles')
        tabs = ttk.Notebook(PuzzleWindow) 
        easy= ttk.Frame(tabs)
        window3= ttk.Frame(tabs)
        tabs.add(window3, text ='Hard')
        tabs.pack(expand = 1, fill ="both") 
        global base3,ans3,board3,moves3,prev3
        def draw2(a,l,m):
            
            global base3
            if a=='A':
                d=base3.create_rectangle(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='red')
            elif a=='B':
                d=base3.create_rectangle(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='yellow')
            elif a=='C':
                d=base3.create_rectangle(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='blue')
            elif a=='D':
                d=base3.create_oval(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='red')
            elif a=='E':
                d=base3.create_oval(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='yellow')
            elif a=='F':
                d=base3.create_oval(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='blue')
            elif a=='G':
                d=base3.create_polygon(80*l+50,m*80+20,80*l+20,80*m+80-20,80*l+80-20,80*m+80-20,fill='red')
            elif a=='H':
                d=base3.create_polygon(80*l+50,m*80+20,80*l+20,80*m+80-20,80*l+80-20,80*m+80-20,fill='green')
            elif a=='I':
                d=base3.create_polygon(80*l+50,m*80+20,80*l+20,80*m+80-20,80*l+80-20,80*m+80-20,fill='yellow')
            elif a=='J':
                d=base3.create_polygon(80*l+50,m*80+20,80*l+20,80*m+80-20,80*l+80-20,80*m+80-20,fill='blue')
            elif a=='K':
                d=base3.create_polygon(80*l+50,m*80+20,80*l+20,80*m+80-20,80*l+80-20,80*m+80-20,fill='black')
            elif a=='L':
                d=base3.create_polygon(80*l+50,m*80+20,80*l+20,80*m+80-20,80*l+80-20,80*m+80-20,fill='orange')
            elif a=='M':
                d=base3.create_rectangle(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='black')
            elif a=='N':
                d=base3.create_rectangle(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='orange')
            elif a=='O':
                d=base3.create_rectangle(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='green')
            elif a=='P':
                d=base3.create_oval(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='pink')
            elif a=='Q':
                d=base3.create_oval(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='green')
            elif a=='R':
                d=base3.create_rectangle(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='pink')
            elif a=='S':
                d=base3.create_rectangle(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='purple')
            elif a=='T':
                d=base3.create_oval(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='purple')
            elif a=='U':
                d=base3.create_polygon(80*l+50,m*80+20,80*l+20,80*m+80-20,80*l+80-20,80*m+80-20,fill='purple')
            elif a=='V':
                d=base3.create_polygon(80*l+50,m*80+20,80*l+20,80*m+80-20,80*l+80-20,80*m+80-20,fill='pink')
            elif a=='W':
                d=base3.create_polygon(80*l+50,m*80+20,80*l+20,80*m+80-20,80*l+80-20,80*m+80-20,fill='maroon')
            elif a=='X':
                d=base3.create_rectangle(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='maroon')
            elif a=='Y':
                d=base3.create_oval(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='maroon')
            elif a=='Z':
                d=base3.create_polygon(80*l+50,m*80+20,80*l+20,80*m+80-20,80*l+80-20,80*m+80-20,fill='brown')
            elif a=='a':
                d=base3.create_oval(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='brown')
            elif a=='b':
                d=base3.create_rectangle(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='brown')
            elif a=='c':
                d=base3.create_polygon(80*l+50,m*80+20,80*l+20,80*m+80-20,80*l+80-20,80*m+80-20,fill='aqua')
            elif a=='d':
                d=base3.create_rectangle(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='aqua')
            elif a=='e':
                d=base3.create_oval(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='aqua')
            elif a=='f':
                d=base3.create_polygon(80*l+50,m*80+20,80*l+20,80*m+80-20,80*l+80-20,80*m+80-20,fill='magenta')
            elif a=='g':
                d=base3.create_oval(80*l+20,m*80+20,80*l+80-20,80*m+80-20,fill='magenta')
  
        def quizboard3():
            
            global base3,ans3,board3,moves3
            count=1
            for i in range(8):
                for j in range(8):
                    e=base3.create_rectangle(80*i,j*80,80*i+80,80*j+80,fill="white")
                    if(board3[i][j]!='.'):
                        draw2(board3[i][j],i,j)
                        count+=1
            if count>64:
                base3.create_text(300,650,text="No. of moves: "+str(moves3),font=('arial',20))
                with open("high_score2.txt","a") as file1:
                    file1.write(s)
                    file1.write(",")
                    file1.write(str(moves1))
                    file1.write("\n")
                
            
 
        def call3(event):
            
            global base3,ans3,board3,moves3,prev3
            i=event.x//80
            j=event.y//80
            if board3[i][j]!='.':
                return
            moves3+=1
            if(prev3[0]>8):
                prev3[0]=i
                prev3[1]=j
                board3[i][j]=ans3[i][j]
                quizboard3()
            else:
                board3[i][j]=ans3[i][j]
                quizboard3()
                if(ans3[i][j]==board3[prev3[0]][prev3[1]]):
                    print("matched")
                    prev3=[100,100]
                    quizboard3()
                    return
                else:
                    board3[prev3[0]][prev3[1]]='.'
                    quizboard3()
                    prev3=[i,j]
                    return
         
        base3=Canvas(window3,width=1000,height=1000)
        base3.pack()
         
        ans3 = list('AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUWWXXYYZZaabbccddeeffgg')
        random.shuffle(ans3)
        ans3 = [ans3[:8],
               ans3[8:16],
               ans3[16:24],
               ans3[24:32],
               ans3[32:40],
               ans3[40:48],
               ans3[48:56],
               ans3[56:]
               ]
         
        base3.bind("<Button-1>", call3)
         
        moves3=IntVar()
        moves3=0
         
        prev3=[80,80]
         
        board3=[list('.'*8) for count in range(8)]
        quizboard3()
          
    elif(option==4):
          return;
    elif(option==5):
        main_menu()
    else:
          print("Enter a valid option\n");
        
    print("\n\t\t1.To play again:");
    print("\n\t\tPress 2 to return to Main Menu.  ");
    choice =int(input());
    if(choice==1):
        play();
    elif(choice==2):
        main_menu();
    else:
            print("\n\t\tThank You for playing!!!");

def instructions():
        file1= open("Rules.txt","r");
        print(file1.read());

def Easy_Leaderboard():
    global moves1
    print("\n\n***LEADERBOARD****\n\n")
    high_score=[]
    with open("high_score.txt") as p:
        for line in p:
            s,moves1=line.split(',')
            moves1=int(moves1)
            high_score.append((s,moves1))
    high_score.sort(key=lambda x:x[1])
    if not high_score:
        print("No Recorded Score\n")
        print("\n1.For Main_Menu\n")
        d=int(input())
        if(d==1):
            main_menu()
        else:
            exit()
    else:
            
        for s,moves1 in high_score:
            print(s,moves1)
            print("\n")
        print("\n1.For Main_Menu\n")
        c=int(input())
        if(c==1):
            main_menu()
        else:
            exit()
            
def Med_Leaderboard():
    global moves2,s
    print("\n\n***LEADERBOARD****\n\n")
    high_score1=[]
    with open("high_score1.txt") as q:
        for line in q:
            s,moves2=line.split(',')
            moves2=int(moves2)
            high_score1.append((s,moves2))
    high_score1.sort(key=lambda y:y[1])
    if not high_score1:
        print("No Recorded Score\n\n")
        print("\n1.For Main_Menu\n")
        e=int(input())
        if(e==1):
            main_menu()
        else:
            exit()
    else:
            
        for s,moves2 in enumerate(high_score1):
            print(s,moves2)
            print("\n")
        print("\n1.For Main_Menu\n")
        c1=int(input())
        if(c1==1):
            main_menu()
        else:
            exit()
    
def Hard_Leaderboard():
    global moves3
    print("\n\n***LEADERBOARD****\n\n")
    high_score2=[]
    with open("high_score2.txt") as r:
        for line in r:
            s,moves3=line.split(',')
            moves3=int(moves3)
            high_score2.append((s,moves3))
    high_score2.sort(key=lambda z:z[1])
    if not high_score2:
        print("No Recorded Score\n")
        print("\n1.For Main_Menu\n")
        g=int(input())
        if(g==1):
            main_menu()
        else:
            exit()
    else:
        
        for s,moves3 in high_score2:
            print(s,moves3)
            print("\n")
        print("\n1.For Main_Menu\n")
        c1=int(input())
        if(c2==1):
            main_menu()
        else:
            exit()
        
	
def main_menu():
    
    print("\t^0^ * ^0^ * --MENU--  * ^0^ * ^0^ *\n");
    print("\t\t1) Play\n");
    print("\t\t2) View High Scores\n");
    print("\t\t3) Instructions\n");
    print("\t\t4) Exit");
    print("\n\t\tSelect your option:  ")
    opt=int(input());
    if(opt==1):
        play();
    elif(opt==2):
        print("Leaderboard for ?\n")
        print("1. for Easier level\n")
        print("2. for Medium level\n")
        print("3. for Harder level\n")
        print("Enter 4 for main_menu\n")
        print("Enter 5 to exit\n")
        print("Enter option:\n")
        optl=int(input())
        if(optl==1):
            Easy_Leaderboard();
        elif(optl==2):
            Med_Leaderboard();
        elif(optl==3):
            Hard_Leaderboard();
        elif(optl==4):
            
            main_menu();
        elif(optl==5):
            exit()
            
        else:
            print("Enter valid option:");
    elif(opt==3):
        instructions()
        time.sleep(5)
        print("\n\nDo you want to play the game?(y/n)\n")
        ch=input()
        if(ch=='y'):
            play()
        elif(ch=='n'):
            exit()
            
    elif(opt==4):
        exit()
main_menu()
