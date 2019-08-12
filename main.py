
import webapp2
import os
import random
import jinja2


temp = []
temp1 = []
hold1 = []
hold2 = []
moves = []

def bringin(player1q, player2q,hold1 , hold2, player, need):
    if player == 1:
        if hold1 < need:
            return(11)
        else:
            for i in hold1:
                player1q.append(i)
    elif player == 2:
        if hold2 < need:
            return(22)
        else:
            for i in hold2:
                player2q.append(i)
    else: raise NameError('in BringIn: player var is wrong')
def startgamebasic():
    myDictBasic = {
    "A" : 'r', "A" : 'r', "A":'b', "A" : 'b',
    2: 'r' , 1: 'r' , 1:'b', 1 : 'b',
    3: 'r' , 1: 'r' , 1:'b', 1 : 'b',
    4: 'r' , 1: 'r' , 1:'b', 1 : 'b',
    5: 'r' , 1: 'r' , 1:'b', 1 : 'b',
    6: 'r' , 1: 'r' , 1:'b', 1 : 'b',
    7: 'r' , 1: 'r' , 1:'b', 1 : 'b',
    8: 'r' , 1: 'r' , 1:'b', 1 : 'b',
    9: 'r' , 1: 'r' , 1:'b', 1 : 'b',
    10: 'r' , 1: 'r', 1:'b', 1 : 'b',
    'J': 'r' , 'J': 'r' , 'J':'b', 'J' : 'b',
    'Q': 'r' , 'Q': 'r' , 'Q':'b', 'Q' : 'b',
    'K': 'r' , 'K': 'r' , 'K':'b', 'K' : 'b',


    }
    return myDictBasic

def setmoves(database):
    player1q = []
    player2q = []
    p =0
    for i in database:
        if p % 2 == 0:

            player1q.append(i)

        if p % 2 == 1 :
            player2q.append(i)
        #else: raise NameError('Function: setmoves broken')
        p +=1

    return player1q, player2q
#run per move
def playmove(player1q, player2q, hold1, hold2):
    if len(player1q) < 1:
        if bringin(player1q, player2q, hold1, hold2, 1, 3) == 11:
            return(11)
    if len(player2q) < 1:
        if bringin(player1q, player2q, hold1, hold2, 2, 3) == 22:
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
        y = war(player1q, player2q, hold1, hold2, stake)
        if y == 1:
            return 11
        if y == 2:
            return 22

    else: raise NameError('Function: playmove broken')

def war(player1q, player2q, hold1, hold2, stake):
    if len(player1q) < 3:
        if bringin(player1q, player2q, hold1, hold2, 1, 3) == 11:
            return(11)
    if len(player2q) < 3:
        if bringin(player1q, player2q, hold1, hold2, 2, 3) == 22:
            return(22)
    war1= ()
    war2 = ()


    war1 = (player1q[0], player1q[1], player1q[2])
    war2 = (player2q[0], player2q[1], player2q[2])
    player1q.pop[0]
    player1q.pop[1]
    player1q.pop[2]
    player2q.pop[0]
    player2q.pop[1]
    player2q.pop[2]

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

game = startgamebasic()
player11, player22 = setmoves(game)





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
        t = playmove(player11, player22, hold1, hold2)
    #    if t == 11:
    #        template = jinja_current_directory.get_template('///')
    #    if t == 22:
    #        template = jinja_current_directory.get_template('///')
        replaces={"moves": moves}
        self.response.write(template.render(replaces))


    # Add a post method
    # def post(self):

class Main(webapp2.RequestHandler):
    def get(self):
        template = jinja_current_directory.get_template("/templates/mainpage.html") #ready template check path
        self.response.write(template.render())


# Route mapping
app = webapp2.WSGIApplication([
    # This line routes the main url ('/')  - also know as
    # The root route - to the Fortune Handler
    ('/', Main),
    ('/playBasic', playBasic),
    #('/farewell', GoodbyeHandler) #maps '/predict' to the FortuneHandler
], debug=True)
