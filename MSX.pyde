models = []
theta = 0
def setup():
    global models
    size(1920, 1080, P3D)
    colorMode(HSB,360,100,100,255)
       
    sakura_model = Model("sakura.obj", 450, 450, 100, 30, random(256),PI,0)
    head_model_1 = Model("Head.obj", 400, 700, 0, 10, random(256),PI/2,-PI+PI/4+PI/8)
    head_model_2 = Model("Head.obj", 1500, 800, 0, 10, random(256),PI/2,0)
    liberty_model = Model("LibertStatue.obj", 1500, 650, 0, 30, random(256),PI,PI)
    models.append(sakura_model)
    models.append(head_model_1)
    models.append(head_model_2)
    models.append(liberty_model)
               
def draw():
    global models, theta
    colorMode(HSB)
    background(0)
    lights()
    strokeWeight(2)
    fill(348,28,100,255)
    noStroke()
    models[0].render()
    fill(200,128)
    noStroke()
    models[1].render()
    noFill()
    stroke(255,128)
    models[2].render()
    fill(197,43.3,67.1,255)
    noStroke()
    models[3].render()
    
    
    
    #wave
    theta += 0.01
    noStroke()
    fill(255)
    for i in range(10):
        angle = theta;
        
        for x in range(int(models[1].pos.x),int(models[2].pos.x),10):    
            y = map(sin(angle), -1, 1, 0,200)
            ellipse(x, y, 16, 16);
            angle += 0.1;    
    
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
        
    
