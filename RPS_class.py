from random import choice 

class Rps:
    lost = "OPPS!! you lose"
    win = "YAYY!! you win"
    p_points = 0
    c_points = 0

    def __init__(self):
        while True:
            self.player =  input("Make your move: ").lower()
            if self.player != "rock" and self.player != "paper" and self.player != "scissors":
                print("!Make the right move!")
            break
        self.comp = choice(["rock","paper","scissors"])
        Rps.play(self)

    def play(self):
            print(f"Computer plays {self.comp}")
            if self.player == self.comp:
                print("IT'S A DRAW")
            elif self.player == "rock":
                if self.comp == "paper":
                    print(Rps.lost)
                    Rps.c_points+=1
                else:
                    print(Rps.win)
                    Rps.p_points+=1
            elif self.player == "paper":
                if self.comp == "rock":
                    print(Rps.win)
                    Rps.p_points+=1
                else:
                    print(Rps.lost)
                    Rps.c_points += 1
            elif self.player == "scissors":
                if self.comp == "rock":
                    print(Rps.lost)
                    Rps.c_points+=1
                else:
                    print(Rps.win)
                    Rps.p_points+=1
            ask = input("Do you wanna continue playing? (y/n): ").lower()
            if ask[0] != "y":
                print(f"player: {Rps.p_points}\t computer: {Rps.c_points}")        
            Rps()
        
        

# comp = choice(["rock","paper","scissors"])
# player = input("Make your move: ").lower()
# if player != "rock" and player != "paper" and player != "scissors":
#     print("!Make the right move!")
playing = Rps()
playing.play()    