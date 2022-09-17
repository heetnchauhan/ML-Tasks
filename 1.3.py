class Titandex:
        def __init__(self,name,height,strength,win_Streak):
                self.n = name
                self.h = height
                self.s = strength
                self.ws = win_Streak
        
        def TitanvsScout(self):
                scout_Name = input("Enter the name of the scout:- ")
                scout_Strength = int(input("Enter the strength of the scout:- "))

                r = t.fight(titan_Strength,scout_Strength)
                if r==-1:
                        print("{} is the WINNER!".format(scout_Name))
                        t.ws = 0
                elif r==0:
                        print("Its a draw between {} and {}".format(titan_Name,scout_Name))
                        t.ws = 0
                elif r==1:
                        print("{} is the WINNER!".format(titan_Name))
                        t.ws+=1
                        print("Winning streak of {} is {}".format(titan_Name,t.ws))

        def fight(self,a,b):
                if a<b:
                        return -1
                elif a>b:
                        return 1
                else:
                        return 0


        def TitanvsTitan(self):
                opp_Titan = input("Enter the opponent Titan: ")
                opp_Titan_s = int(input("Enter the opponet Titan's strength: "))
                if opp_Titan!=t.n:
                        x = t.fight(titan_Strength,opp_Titan_s)
                        if x==-1:
                                print("{} is the WINNER!".format(opp_Titan))
                                t.ws = 0
                        elif x==0:
                                print("Its a draw between {} and {}".format(titan_Name,opp_Titan))
                                t.ws = 0
                        elif x==1:
                                print("{} is the WINNER!".format(titan_Name))
                                t.ws+=1
                                print("Winning streak of {} is {}".format(titan_Name,t.ws))
                else:
                        print("A titan cant fight itself")



titan_Name = input("Enter the name of the Titan:- ")
titan_Height = int(input("Enter the height of the Titan:- "))
titan_Strength = int(input("Enter the strength of the Titan:- "))

t = Titandex(titan_Name,titan_Height,titan_Strength,0)
n_opp = int(input("Enter the number of opponents:- "))
while n_opp!=0:
        opp = int(input("Enter the opponent:\n1.Scout\n2.Titan\n"))
        if opp==1:
                t.TitanvsScout()
                n_opp-=1
        elif opp==2:
                t.TitanvsTitan()
                n_opp-=1
print("The final winning streak of Titan is ",t.ws)



    