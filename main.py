
import webapp2
import os
import random
import jinja2

myDictBasic = {
    1:("A",'r'), 14:("A" , 'r'), 27:("A",'b'), 40:("A" , 'b'),
    2:(2, 'r') , 15:(2, 'r') , 28:(2,'b'), 41:(2 , 'b'),
    3:(3, 'r') , 16:(3, 'r') , 29:(3,'b'),42:(3 , 'b'),
    4:(4, 'r') , 17:(4, 'r') , 30:(4,'b'), 43:(4 , 'b'),
    5:(5, 'r') ,18:( 5, 'r' ), 31:(5,'b'), 44:(5 , 'b'),
    6:(6, 'r') , 19:(6, 'r') , 32:(6,'b'),45:( 6 , 'b'),
    7:(7, 'r') , 20:(7, 'r') ,33:( 7,'b'), 46:(7 , 'b'),
    8:(8, 'r') ,21:(8, 'r') ,34:( 8,'b'), 47:(8 , 'b'),
    9:(9, 'r') , 22:(9, 'r') , 35:(9,'b'), 48:(9 , 'b'),
    10:(10, 'r') ,23 :(10, 'r'), 36:(10,'b'), 49:(10 , 'b'),
    11:(11, 'r') ,24: (11,'r') , 37:(11,'b'), 50:(11 ,'b'),
    12:(12, 'r') , 25:(12, 'r' ),38: (12,'b'), 51:(12 , 'b'),
    13:(13, 'r') , 26:(13, 'r') , 39:(13,'b'), 52:(13 , 'b')}

temp = []
temp1 = []
hold1 = []
hold2 = []
moves = []
player1q = []
player2q = []
def bringin(player1q, player2q,hold1 , hold2, player, need):
    if player == 1:
        if hold1 < need:
            return(11)
        else:
            for i in hold1:
                player1q.append(i[0])
    elif player == 2:
        if hold2 < need:
            return(22)
        else:
            for i in hold2:
                player2q.append(i[0])
    else: raise NameError('in BringIn: player var is wrong')






def setmoves(database):

    p =0
    for i in database:
        if p % 2 == 0:

            player1q.append(database[i])

        if p % 2 == 1 :
            player2q.append(database[i])
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


    war1 = (player1q[0], player1q[1], player1q[2][0])
    war2 = (player2q[0], player2q[1], player2q[2][0])
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
        t = playmove(player1q, player2q, hold1, hold2)
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
