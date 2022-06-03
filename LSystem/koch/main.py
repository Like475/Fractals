import turtle

class LSystem:
    def __init__(self, t, axiom, width, length, angle):
        self.t = t
        self.axiom = self.state = axiom
        self.width = width
        self.length = length
        self.angle = angle
        self.rules = {}
        self.t.pensize(self.width)
    
    def initRules(self, *rules):
        for key, value in rules:
            self.rules[key] = value
        print(rules)
    
    def iterPath(self, nIter):
        for n in range(nIter):
            for key, value in self.rules.items():
                self.state = self.state.replace(key, value.lower())
            
            self.state = self.state.upper()
    
    def draw(self, start, angle):
        turtle.tracer(1, 0)
        self.t.up()
        self.t.setpos(start)
        self.t.seth(angle)
        self.t.down()

        for move in self.state:
            if move == 'F':
                self.t.fd(self.length)
            elif move == 'S':
                self.t.up()
                self.t.fd(self.length)
                self.t.up()
            elif move == '+':
                self.t.lt(self.angle)
            elif move == '-':
                self.t.rt(self.angle)

        turtle.done()

turtle.Screen().setup(1200, 600, 50, 50)
t = turtle.Turtle()
t.ht()

width = 2
len = 10
angle = 60
axiom = 'F'


fractal = LSystem(t, axiom, width, len, angle)
fractal.initRules(('F', 'F+F--F+F'))
fractal.iterPath(3)
fractal.draw((0, 0), 0)