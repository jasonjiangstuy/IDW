
import webapp2
import os
import random
import jinja2

myDictBasic = [
    (1, 1), (1 , 14), (1,27), (1, 40),
    (2, 2) , (2, 15) , (2,28), (2 , 41),
    (3, 3) , (3, 16) , (3,29),(3 , 42),
    (4, 4) , (4, 17) , (4,30), (4 , 43),
    (5, 5) ,( 5, 18 ), (5,31), (5 , 44),
    (6, 6) , (6, 19) , (6,32),( 6 , 45),
    (7, 7) , (7, 20) ,( 7,33), (7 , 46),
    (8, 8) ,(8, 21) ,( 8,34), (8 , 47),
    (9, 9) , (9, 22) , (9,35), (9 , 48),
    (10, 10) ,(10, 23), (10,36), (10 , 49),
    (11, 11) ,(11,24) , (11,37), (11 ,50),
    (12, 12) , (12, 25 ), (12,38), (12 , 51),
    (13, 13) , (13, 26) , (13,40), (13 , 52)]

temp = []
temp1 = []
hold1 = []
hold2 = []
moves = []
player1q = []
player2q = []

def reset():
    for i in range(len(temp)):
        temp.pop()
    for i in range(len(temp1)):
        temp1.pop()
    for i in range(len(hold1)):
        hold1.pop()
    for i in range(len(hold2)):
        hold2.pop()
    for i in range(len(moves)):
        moves.pop()

    player1q, player2q = setmoves(myDictBasic)

def bringin(player1q, player2q,hold1 , hold2, player, need, game):
    if game == 1:

        if player == 1:
            if len(hold1) < need:
                return(11)
            else:
                for i in hold1:
                    player1q.append(i)
                for i in range(len(hold1)):
                    hold1.pop()
        elif player == 2:
            if len(hold2) < need:
                return(22)
            else:
                for i in hold2:
                    player2q.append(i)
                for i in range(len(hold2)):
                    hold2.pop()
        else: raise NameError('in BringIn: player var is wrong')

    if game == 2:

        if player == 1:
            if len(hold1) < need:
                return('stop')
            else:
                for i in hold1:
                    player1q.append(i)
                    for i in range(len(hold1)):
                        hold1.pop()
        elif player == 2:
            if len(hold2) < need:
                return('stop')
            else:
                for i in hold2:
                    player2q.append(i)
                for i in range(len(hold2)):
                    hold2.pop()
        else: raise NameError('in BringIn: player var is wrong')

def setmoves(database):
    p =0
    random.shuffle(database)
    for i in database:
        if p % 2 == 0:
            player1q.append(i)

        if p % 2 == 1 :
            player2q.append(i)
        #else: raise NameError('Function: setmoves broken')
        p +=1

    return player1q, player2q
#run per move
def playmove(player1q, player2q, hold1, hold2, game, index):
    if game == 1:
        if len(player1q) < 1:
            if bringin(player1q, player2q, hold1, hold2, 1, 3, game) == 11:
                return(11)
        if len(player2q) < 1:
            if bringin(player1q, player2q, hold1, hold2, 2, 3, game) == 22:
                return(22)
        play1 = player1q[index]
        player1q.pop(index)
        play2 = player2q[index]
        player2q.pop(index)

        if play1 > play2:
            hold1.append(play1)
            hold1.append(play2)
            moves.append((play1))
            moves.append((play2))
            return
        elif play2 > play1:
            hold2.append(play1)
            hold2.append(play2)
            moves.append((play1))
            moves.append((play2))
            return

        elif play2 == play1:
            temp.append(play1)
            temp1.append(play2)
            stake = [play1, play2]
            y = war(player1q, player2q, hold1, hold2, stake, game)
            if y == 1:
                return 11
            if y == 2:
                return 22

        else: raise NameError('Function: playmove broken')
    if game == 2:
        if len(player1q) < index + 1:
            return("stop")
        if len(player2q) < index +1:
            return("stop")
        play1 = player1q[index]
        player1q.pop(index)
        play2 = player2q[index]
        player2q.pop(index)

        if play1 > play2:
            hold1.append(play1)
            hold1.append(play2)
            moves.append((play1))
            moves.append((play2))
            return
        elif play2 > play1:
            hold2.append(play1)
            hold2.append(play2)
            moves.append((play1))
            moves.append((play2))
            return

        elif play2 == play1:
            temp.append(play1)
            temp1.append(play2)
            stake = [play1, play2]
            y = war(player1q, player2q, hold1, hold2, stake, game)
            if y == 'stop':
                return 'stop'

        else: raise NameError('Function: playmove broken')
def war(player1q, player2q, hold1, hold2, stake, game):
    if game == 1:
        if len(player1q) < 3:
            if bringin(player1q, player2q, hold1, hold2, 1, 3, game) == 11:
                return(11)
        if len(player2q) < 3:
            if bringin(player1q, player2q, hold1, hold2, 2, 3, game) == 22:
                return(22)
        war1= ()
        war2 = ()


        war1 = (player1q[0], player1q[1], player1q[2][0])
        war2 = (player2q[0], player2q[1], player2q[2][0])
        player1q.pop(0)
        player1q.pop(1)
        player1q.pop(2)
        player2q.pop(0)
        player2q.pop(1)
        player2q.pop(2)

        if war1[-1] > war2[-1]:
            for i in war1:
                hold1.append(i)
                temp.append(i)

            for i in war2:
                hold1.append(i)
                temp1.append(i)
            for i in stake:
                hold1.append(i)
            return

        if war2[-1] > war1[-1]:
            for i in war1:
                hold2.append(i)
                temp.append(i)
            for i in war2:
                hold2.append(i)
                temp1.append(i)
            for i in stake:
                hold2.append(i)
            return
        if war2[-1] == war1[-1]:

            for i in war1:
                stake.append(i)
                temp.append(i)
            for i in war2:
                stake.append(i)
                temp1.append(i)


            war(player1q, player2q, hold1, hold2, stake)
            return

    if game ==2:
        if len(player1q) < 3:
            if bringin(player1q, player2q, hold1, hold2, 1, 3, game) == 11:
                return('stop')
        if len(player2q) < 3:
                return('stop')
        war1= ()
        war2 = ()


        war1 = (player1q[0], player1q[1], player1q[2][0])
        war2 = (player2q[0], player2q[1], player2q[2][0])
        player1q.pop(0)
        player1q.pop(1)
        player1q.pop(2)
        player2q.pop(0)
        player2q.pop(1)
        player2q.pop(2)

        if war1[-1] > war2[-1]:
            for i in war1:
                hold1.append(i)
                temp.append(i)
            for i in war2:
                hold1.append(i)
                temp1.append(i)
            for i in stake:
                hold1.append(i)
            return

        if war2[-1] > war1[-1]:
            for i in war1:
                hold2.append(i)
                temp.append(i)
            for i in war2:
                hold2.append(i)
                temp1.append(i)
            for i in stake:
                hold2.append(i)
            return
        if war2[-1] == war1[-1]:

            for i in war1:
                stake.append(i)
                temp.append(i)
            for i in war2:
                stake.append(i)
                temp1.append(i)

            war(player1q, player2q, hold1, hold2, stake, game)
            return

#setting global var for the queues


player1q, player2q = setmoves(myDictBasic)



# Remember, you can get this by searching for jinja2 google app engine
jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class playBasic(webapp2.RequestHandler):
    def get(self):
        
        template = jinja_current_directory.get_template('/templates/IDW2.html')#play template
        self.response.write(template.render())




    def post(self):
        template = jinja_current_directory.get_template('/templates/IDW2.html')
        lost = ""
        if lost == "":
            t = playmove(player1q, player2q, hold1, hold2, 1, 0)

        if t == 11:
            lost = "player2 wins"
        if t == 22:
            lost = "player1 wins"
        deck1 = len(player1q)
        deck2 = len(player2q)
        holding1 = len(hold1)
        holding2 = len(hold2)
        test = myDictBasic
        player1move = moves[len(moves)-2]
        player2move = moves[-1]
        img1 = '/cards/'+str(player1move[1]) + '.png'
        img2 = '/cards/'+str(player2move[1])+'.png'
        replaces={"test":test,"moves": moves, "player1":deck1, "player2":deck2, "player1hold":holding1, "player2hold":holding2, "test":test, "lost": lost, "p1move":player1move[0], "p2move":player2move[0], "img1":img1, "img2":img2}
        self.response.write(template.render(replaces))




class Main(webapp2.RequestHandler):
    def get(self):
        template = jinja_current_directory.get_template("/templates/mainpage.html") #ready template check path
        self.response.write(template.render())

        

class playShort(webapp2.RequestHandler):
    def get(self):
        template = jinja_current_directory.get_template('/templates/IDW2.html')#play template
        deck1 = len(player1q)
        deck2 = len(player2q)
        holding1 = len(hold1)
        holding2 = len(hold2)
        test = myDictBasic
        player1move = 'n/a'
        player2move = 'n/a'
        lost = ""
        img1 = "/cards/0.jpeg"
        img2 = "/cards/0.jpeg"
        replaces={"moves": moves, "player1":deck1, "player2":deck2, "player1hold":holding1, "player2hold":holding2, "test":test, "lost": lost, "p1move":player1move[0], "p2move":player2move[0], "img1":img1, "img2":img2}

        self.response.write(template.render())

    def post(self):
        template = jinja_current_directory.get_template('/templates/IDW2.html')
        t = playmove(player1q, player2q, hold1, hold2, 2, 0)
    #    if t == 11:
    #        template = jinja_current_directory.get_template('///')

        lost = " "
        if t == 'stop':
            if hold2 > hold1:
                lost = "player1 wins"
        
            if hold2 < hold1:
                lost = "player2 wins"
                
                
            if hold2 == hold1:
                lost = "tie"
            reset()
            template = jinja_current_directory.get_template('/templates/IDW2.html')#play template
            deck1 = len(player1q)
            deck2 = len(player2q)
            holding1 = len(hold1)
            holding2 = len(hold2)
            test = myDictBasic
            player1move = 'n/a'
            player2move = 'n/a'

            img1 = "/cards/0.jpeg"
            img2 = "/cards/0.jpeg"
            replaces={"moves": moves, "player1":deck1, "player2":deck2, "player1hold":holding1, "player2hold":holding2, "test":test, "lost": lost, "p1move":player1move[0], "p2move":player2move[0], "img1":img1, "img2":img2}               
            self.response.write(template.render(replaces))
#copy to simple --basic
        else:
            deck1 = len(player1q)
            deck2 = len(player2q)
            holding1 = len(hold1)
            holding2 = len(hold2)
            test = myDictBasic
            player1move = moves[len(moves)-2]
            player2move = moves[-1]

            img1 = '/cards/'+str(player1move[1]) + '.png'
            img2 = '/cards/'+str(player2move[1])+'.png'
            replaces={"moves": moves, "player1":deck1, "player2":deck2, "player1hold":holding1, "player2hold":holding2, "test":test, "lost": lost, "p1move":player1move[0], "p2move":player2move[0], "img1":img1, "img2":img2}
            self.response.write(template.render(replaces))



    # Add a post method
    # def post(self):

class coolwar(webapp2.RequestHandler):
    def get(self):
        template = jinja_current_directory.get_template('/templates/coolwar.html')
        deck1 = len(player1q)
        deck2 = len(player2q)
        holding1 = len(hold1)
        holding2 = len(hold2)
        test = myDictBasic
        player1move = 'n/a'
        player2move = 'n/a'
        lost = ""
        img1 = "/cards/0.jpeg"
        img2 = "/cards/0.jpeg"
        show1 = "/cards/0.jpeg"
        show2 = "/cards/0.jpeg"
        replaces={"moves": moves, "player1":deck1, "player2":deck2, "player1hold":holding1, "player2hold":holding2, "test":test, "lost": lost, "p1move":player1move[0], "p2move":player2move[0], "img1":img1, "img2":img2, "show1" : show1, "show2":show2}
        self.response.write(template.render())
    def post(self):
        template = jinja_current_directory.get_template('/templates/coolwar.html')
        b1 = self.request.get('b1')
        b2 = self.request.get('b2')
        if b1 == "1":
            t = playmove(player1q, player2q, hold1, hold2, 2, 0)
            lost = " "
            if t == 'stop':
                if hold2 > hold1:
                    lost = "player1 wins"
        
                if hold2 < hold1:
                    lost = "computer wins"
                    
                
                if hold2 == hold1:
                    lost = "tie"
                reset()
                template = jinja_current_directory.get_template('/templates/coolwar.html')#play template
                deck1 = len(player1q)
                deck2 = len(player2q)
                holding1 = len(hold1)
                holding2 = len(hold2)
                test = myDictBasic
                player1move = 'n/a'
                player2move = 'n/a'
                show1 = "/cards/0.jpeg"
                show2 = "/cards/0.jpeg"
                img1 = "/cards/0.jpeg"
                img2 = "/cards/0.jpeg"
                replaces={"moves": moves, "player1":deck1, "player2":deck2, "player1hold":holding1, "player2hold":holding2, "test":test, "lost": lost, "p1move":player1move[0], "p2move":player2move[0], "img1":img1, "img2":img2, "show1" : show1, "show2":show2}               
                self.response.write(template.render(replaces))
            else:
                show1 = "/cards/0.jpeg"
                show2 = "/cards/0.jpeg"
                deck1 = len(player1q)
                deck2 = len(player2q)
                holding1 = len(hold1)
                holding2 = len(hold2)
                test = myDictBasic
                player1move = moves[len(moves)-2]
                player2move = moves[-1]
                if len(player1q) > 0:
                    show1 = '/cards/'+str(player1q[0][1])+'.png'
                if len(player1q) > 1:
                    show2 = '/cards/'+str(player1q[1][1])+'.png'
                img1 = '/cards/'+str(player1move[1]) + '.png'
                img2 = '/cards/'+str(player2move[1])+'.png'
                replaces={"moves": moves, "player1":deck1, "player2":deck2, "player1hold":holding1, "player2hold":holding2, "test":test, "lost": lost, "p1move":player1move[0], "p2move":player2move[0], "img1":img1, "img2":img2, "show1" : show1, "show2":show2}
                self.response.write(template.render(replaces))

        if b2 == "1":
            t = playmove(player1q, player2q, hold1, hold2, 2, 1)
            lost = " "
            if t == 'stop':
                if hold2 > hold1:
                    lost = "player1 wins"
        
                if hold2 < hold1:
                    lost = "player2 wins"
                
                
                if hold2 == hold1:
                    lost = "tie"
                reset()
                template = jinja_current_directory.get_template('/templates/coolwar.html')#play template
                deck1 = len(player1q)
                deck2 = len(player2q)
                holding1 = len(hold1)
                holding2 = len(hold2)
                test = myDictBasic
                player1move = 'n/a'
                player2move = 'n/a'
                show1 = "/cards/0.jpeg"
                show2 = "/cards/0.jpeg"
                img1 = "/cards/0.jpeg"
                img2 = "/cards/0.jpeg"
                replaces={"moves": moves, "player1":deck1, "player2":deck2, "player1hold":holding1, "player2hold":holding2, "test":test, "lost": lost, "p1move":player1move[0], "p2move":player2move[0], "img1":img1, "img2":img2, "show1" : show1, "show2":show2}               
                self.response.write(template.render(replaces))
            else:
                show1 = "/cards/0.jpeg"
                show2 = "/cards/0.jpeg"
                deck1 = len(player1q)
                deck2 = len(player2q)
                holding1 = len(hold1)
                holding2 = len(hold2)
                test = myDictBasic
                player1move = moves[len(moves)-2]
                player2move = moves[-1]
                if len(player1q) > 0:
                    show1 = '/cards/'+str(player1q[0][1])+'.png'
                if len(player1q) > 1:
                    show2 = '/cards/'+str(player1q[1][1])+'.png'
                img1 = '/cards/'+str(player1move[1]) + '.png'
                img2 = '/cards/'+str(player2move[1])+'.png'
                replaces={"moves": moves, "player1":deck1, "player2":deck2, "player1hold":holding1, "player2hold":holding2, "test":test, "lost": lost, "p1move":player1move[0], "p2move":player2move[0], "img1":img1, "img2":img2, "show1" : show1, "show2":show2}
                self.response.write(template.render(replaces))



        
# Route mapping
app = webapp2.WSGIApplication([
    # This line routes the main url ('/')  - also know as
    # The root route - to the Fortune Handler
    ('/', Main),
    ('/playBasic', playBasic),
    ('/playShort', playShort),
    ('/playCool', coolwar)
    #('/farewell', GoodbyeHandler) #maps '/predict' to the FortuneHandler


], debug=True)
