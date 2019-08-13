
import webapp2
import os
import random
import jinja2

myDictBasic = [
    (1,'r'), (1 , 'r'), (1,'b'), (1, 'b'),
    (2, 'r') , (2, 'r') , (2,'b'), (2 , 'b'),
    (3, 'r') , (3, 'r') , (3,'b'),(3 , 'b'),
    (4, 'r') , (4, 'r') , (4,'b'), (4 , 'b'),
    (5, 'r') ,( 5, 'r' ), (5,'b'), (5 , 'b'),
    (6, 'r') , (6, 'r') , (6,'b'),( 6 , 'b'),
    (7, 'r') , (7, 'r') ,( 7,'b'), (7 , 'b'),
    (8, 'r') ,(8, 'r') ,( 8,'b'), (8 , 'b'),
    (9, 'r') , (9, 'r') , (9,'b'), (9 , 'b'),
    (10, 'r') ,(10, 'r'), (10,'b'), (10 , 'b'),
    (11, 'r') ,(11,'r') , (11,'b'), (11 ,'b'),
    (12, 'r') , (12, 'r' ), (12,'b'), (12 , 'b'),
    (13, 'r') , (13, 'r') , (13,'b'), (13 , 'b')]

temp = []
temp1 = []
hold1 = []
hold2 = []
moves = []
player1q = []
player2q = []
def bringin(player1q, player2q,hold1 , hold2, player, need, game):
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
def playmove(player1q, player2q, hold1, hold2, game):
    if game == 1:

        if len(player1q) < 1:
            if bringin(player1q, player2q, hold1, hold2, 1, 3, game) == 11:
                return(11)
        if len(player2q) < 1:
            if bringin(player1q, player2q, hold1, hold2, 2, 3, game) == 22:
                return(22)
        play1 = player1q[0]
        player1q.pop(0)
        play2 = player2q[0]
        player2q.pop(0)

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
        if len(player1q) < 1:
            return("stop")
        if len(player2q) < 1:
            return("stop")
        play1 = player1q[0][0]
        player1q.pop(0)
        play2 = player2q[0][0]
        player2q.pop(0)

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
            if bringin(player1q, player2q, hold1, hold2, 1, 3) == 11:
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

            war(player1q, player2q, hold1, hold2, stake)
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
        template = jinja_current_directory.get_template('/templates/IDW.html')#play template
        self.response.write(template.render())




    def post(self):
        template = jinja_current_directory.get_template('/templates/IDW.html')
        lost = ""
        if lost == "":
            t = playmove(player1q, player2q, hold1, hold2, 1)

        if t == 11:
            lost = "player1"
        if t == 22:
            lost = "player2"
        deck1 = len(player1q)
        deck2 = len(player2q)
        holding1 = len(hold1)
        holding2 = len(hold2)
        test = myDictBasic
        replaces={"moves": moves, "player1":deck1, "player2":deck2, "player1hold":holding1, "player2hold":holding2, "test":test, "lost": lost}
        self.response.write(template.render(replaces))


    # Add a post method
    # def post(self):

class Main(webapp2.RequestHandler):
    def get(self):
        template = jinja_current_directory.get_template("/templates/mainpage.html") #ready template check path
        self.response.write(template.render())

class playShort(webapp2.RequestHandler):
    def get(self):
        template = jinja_current_directory.get_template('/templates/IDW.html')#play template
        self.response.write(template.render())

    def post(self):
        template = jinja_current_directory.get_template('/templates/IDW.html')
        t = playmove(player1q, player2q, hold1, hold2, 2)
    #    if t == 11:
    #        template = jinja_current_directory.get_template('///')
    #    if t == 22:
    #        template = jinja_current_directory.get_template('///')
        deck1 = len(player1q)
        deck2 = len(player2q)
        holding1 = len(hold1)
        holding2 = len(hold2)
        test = myDictBasic
        replaces={"moves": moves, "player1":deck1, "player2":deck2, "player1hold":holding1, "player2hold":holding2, "test":test}
        self.response.write(template.render(replaces))


    # Add a post method
    # def post(self):

# Route mapping
app = webapp2.WSGIApplication([
    # This line routes the main url ('/')  - also know as
    # The root route - to the Fortune Handler
    ('/', Main),
    ('/playBasic', playBasic),
    #('/farewell', GoodbyeHandler) #maps '/predict' to the FortuneHandler
], debug=True)
