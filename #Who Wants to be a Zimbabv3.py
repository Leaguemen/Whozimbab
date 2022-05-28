#Who Wants to be a Zimbab
from ast import While
from operator import index
import random
class Player:
    def __init__(self,question = " ",gindex= 234,answer = "", points = 0, live = 3):
        self.question= question
        self.gindex= gindex
        self.answer= answer
        self.points= points
        self.live = live
        
    def generate_gindex(self):
        self.gindex = random.randint(0,len(question_list)-1)

    def generate_question(self):
        self.question = question_list[self.gindex]
        print(self.question)
        print("Input your answer")
        self.answer = input()
        self.answer = self.answer.lower()
        if self.answer in answer_list:
            player_one.point_nambah()
            question_list.remove(self.question)
        elif self.answer in wrong_answer_list:
            player_one.wrong_ans()
            question_list.remove(self.question)
        else:
            print("Whoops, it seems like your answer doesn't match up to any of the options")
            
    def point_nambah(self):
        self.points+= 100000
        print("Congrats, correct answer. You have accumulated "+str(self.points)+" ZWD On to the next one")
    
    def wrong_ans(self):
        self.live = self.live-1
        if self.live >0 :
            print("Aw darn it, lost a life. Don't worry you still have "+ str(self.live) +" left!")
        else :
            print("GAME OVER, your score is "+ str(self.points)+" ZWD")
            exit()

print("################################")
print("# Who Wants To be a Zimbabwean #")
print("################################")

question_list = ["What is the height of the Eifell Tower? 200 m | 300 m | 250 m", "Who is the first President of Indonesia? Soekarno | B.J. Habiebie | Salman", "On what year did the bomb of Hiroshima was dropped ? 1944|1947|1945", "Table salt has the scientifical name of ... Magnesium Sulfide | Sodium Chloride | Sulfuric Acid", "Momentum is the product of mass and ... Velocity | Acceleration | Position","To connect a harddisk to the motherboard, we usually use a ... cable  DATA | USB | SATA", "This program was written using what langguage ? Python|C#|Java",'The character "Ziggy Stardust" is a nickname of which of these artist    Freddy Mercury | David Bowie | Elton John', "What nation, of these three, border argentina?  Uruguay | Jamaica | Mexico","Which of these is a famous drink from Mexico?  Es teh | Los Pollos Hermanos | Horchata"]
wrong_answer_list = ["200 m", "250 m", "b.j. habiebie", "salman","1944", "1947", "magnesium sulfide", "sulfuric acid", "acceleration","position", "data","usb","c#","java","freddy mercury", "elton john", "jamaica", "mexico", "es teh", "los pollos hermanos"]
answer_list = ["300 m", "soekarno", "1945", "sodium chloride","velocity", "sata","python","david bowie","uruguay","horchata"]
player_one = Player()
while question_list !=[] :
    player_one.generate_gindex()
    player_one.generate_question()
print("CONGRATULATION !!! You've become the richest man in Zimbabwe")