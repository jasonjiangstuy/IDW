
import webapp2
import os
import random
import jinja2


def startgame():
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
    y =0
    for i in database:
        if y %2 == 0:

            player1q.append(i)

        if y % 2 ==1 :
            player2q.append(i)
        else: raise NameError('Function: setmoves broken')
        y +=1

    return player1q, player2q

def playmove(player1q, player2q):
    play1 = player1q[0]
    player1q.pop[0]
    play2 = player2q[0]
    player2q.pop[0]
    




# Remember, you can get this by searching for jinja2 google app engine
jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class playBasic(webapp2.RequestHandler):
    def get(self):
        # In part 2, instead of returning this string,
        # make a function call that returns a random fortune.
        template = jinja_current_directory.get_template('templates/fortune-results.html')
        replace = {"title" : "What is your Astrological Sign", "message" : ""}
        self.response.write(template.render(replace))

    def post(self):
        user_astro_sign = self.request.get('user_astrological_sign')

        template = jinja_current_directory.get_template('templates/fortune-results.html')
        message = get_fortune()
        replaces = {"title" : user_astro_sign, "message" : message}
        self.response.write(template.render(replaces))


    # Add a post method
    # def post(self):

class Main(webapp2.RequestHandler):
    def get(self):
        template = jinja_current_directory.get_template("frontend/mainpage.html") #ready template check path
        self.response.write(template.render())


class GoodbyeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('My response is Goodbye world')
# Route mapping
app = webapp2.WSGIApplication([
    # This line routes the main url ('/')  - also know as
    # The root route - to the Fortune Handler
    ('/', Main),
    ('/playBasic', playBasic),
    ('/farewell', GoodbyeHandler) #maps '/predict' to the FortuneHandler
], debug=True)
