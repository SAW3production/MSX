models = []
leaves = []
stars = []
mind_offsets = []
theta = 0
timer = 0.0
characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()-=_+[]{}|;':,.<>?/ "
matrix_rain = []
def setup():
    frameRate(30)
    global models,mind_offsets,leaves,characters,matrix_rain
    size(1920, 1080, P3D)
    colorMode(HSB,360,100,100,255)
       
    sakura_model = Model("sakura.obj", 425, 450, 0, 30, random(256),PI,0)
    head_model_1 = Model("Head.obj", 400, 700, 0, 10, random(256),PI/2,-PI+PI/4+PI/8)
    head_model_2 = Model("Head.obj", 1500, 800, 20, 10, random(256),PI/2,PI/2)
    liberty_model = Model("LibertStatue.obj", 1450, 550, 20, 30, random(256),PI,PI)
    models.append(sakura_model)
    models.append(head_model_1)
    models.append(liberty_model)
    models.append(head_model_2)
    
    for i in range(-200, width+400, 20):
        column = []
        for j in range(0, height*2, 20):
            column.append(MatrixChar(i, j))
        matrix_rain.append(column)
    
    for i in range(6):
        mind_offsets.append(random(0,250))
    
    
    for _ in range(200):
        leaves.append(Leaf())
        
    for _ in range(100):
        stars.append(Star())
               
def draw():
    global models, theta, mind_offsets,timer,leaves,characters,matrix_rain,stars
    timer+=1.0/30.0
    r = 10
    c = 1
    print(timer)
    colorMode(HSB)
    background(0)
    pushMatrix()
    translate(0,0,-100)
    for column in matrix_rain:
        for matrix_char in column:
            matrix_char.display()
            matrix_char.fall()
    popMatrix()
    lights()
    strokeWeight(2)
    
    scale(min(timer*0.1+0.1,1))
    
    #1 head
    pushMatrix()
    rotateY(sin(timer)*0.1)
    fill(348,28,100,255)
    noStroke()
    models[0].render()
    fill(200,128)
    noStroke()
    models[1].render()
    translate(400,300)
    for leaf in leaves:
        leaf.update()
        leaf.display()
    popMatrix()
    
    #2 head
    pushMatrix()
    
    rotateY(sin(timer-10.5)*0.01)
    fill(197,43.3,67.1,255)
    noStroke()
    models[2].render()
    fill(200,128)
    noStroke()
    models[3].render()
    translate(1450,450)
    for star in stars:
        star.update()
        star.display()
    
    popMatrix()
    
    
    
    #wave
    theta += 0.08
    noStroke()
    fill(255)
    for m in range(5):
        angle = theta;
        
        for x in range(int(models[1].pos.x),int(models[2].pos.x)+50,20):    
            y = map(sin(angle), -0.5, 0.5, 220,250) + mind_offsets[m]
            transparency = map(cos(angle),0,1,0,255)
            z = map(sin(angle),0,20,0,500)
            pushMatrix()
            translate(x,y,z)
            fill(200,255,255,transparency)   
            sphere(random(5,10))
            popMatrix()
              
            
            angle += mind_offsets[m+1]*0.01 +0.5;    
            
    
class Model:
    def __init__(self, file_name, x, y, z, s, h,angleX,angleY):
        self.pos = PVector(x, y, z)
        self.s = s
        self.h = h
        self.sh = loadShape(file_name)
        self.sh.disableStyle()
        self.angleX = angleX
        self.angleY = angleY
        
    def render(self):
        pushMatrix()
        translate(self.pos.x, self.pos.y, self.pos.z)
        rotateY(self.angleY)
        rotateX(self.angleX)
        
        scale(self.s)        
        shape(self.sh)
        popMatrix()
        
           
class Leaf:
    def __init__(self):
        theta = random(0, TWO_PI)
        phi = random(0, PI)
        radius = 100
        self.position = PVector(
            radius * sin(phi) * cos(theta),
            radius * sin(phi) * sin(theta),
            radius * cos(phi)
        )
        self.velocity = PVector(0, 0, random(1, 5))

    def update(self):
        self.position.add(self.velocity)
        if self.position.z > 200:
            self.position.z = -200

    def display(self):
        fill(348,28,100,255)
        noStroke()
        pushMatrix()
        translate(self.position.x, self.position.y, self.position.z)
        
        circle(0,0,5)
        popMatrix()
        
class Star:
    def __init__(self):
        theta = random(0, TWO_PI)
        phi = random(0, PI)
        radius = 100
        self.position = PVector(
            radius * sin(phi) * cos(theta),
            radius * sin(phi) * sin(theta),
            radius * cos(phi)
        )
        self.velocity = PVector(0, 0, random(1, 5))

    def update(self):
        self.position.add(self.velocity)
        if self.position.z > 200:
            self.position.z = -200

    def display(self):
        fill(255,128)
        noStroke()
        pushMatrix()
        translate(self.position.x, self.position.y, self.position.z)
        
        star(0,0,5,10,4)
        popMatrix()
def star(x, y, radius1, radius2, npoints):
    angle = TWO_PI / npoints;
    halfAngle = angle/2.0;
    beginShape();
    a = 0
    while (a<TWO_PI):
        sx = x + cos(a) * radius2;
        sy = y + sin(a) * radius2;
        vertex(sx, sy);
        sx = x + cos(a+halfAngle) * radius1;
        sy = y + sin(a+halfAngle) * radius1;
        vertex(sx, sy);
        a+=angle
    endShape(CLOSE);        
class MatrixChar:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random(1, 5)
        self.value = characters[int(random(len(characters)))]

    def fall(self):
        self.y = (self.y + self.speed) % height
        if random(1) < 0.01: 
            self.value = characters[int(random(len(characters)))]

    def display(self):
        fill(255, 255, 30,128)
        noStroke()
        textSize(20)
        text(self.value, self.x, self.y)                
        
