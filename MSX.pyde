models = []
mind_offsets = []
theta = 0
timer = 0.0
def setup():
    frameRate(30)
    global models,mind_offsets
    size(1920, 1080, P3D)
    colorMode(HSB,360,100,100,255)
       
    sakura_model = Model("sakura.obj", 425, 450, 0, 30, random(256),PI,0)
    head_model_1 = Model("Head.obj", 400, 700, 0, 10, random(256),PI/2,-PI+PI/4+PI/8)
    head_model_2 = Model("Head.obj", 1500, 800, 20, 10, random(256),PI/2,PI/2)
    liberty_model = Model("LibertStatue.obj", 1450, 550, 20, 30, random(256),PI,PI)
    models.append(sakura_model)
    models.append(head_model_1)
    models.append(head_model_2)
    models.append(liberty_model)
    
    for i in range(6):
        mind_offsets.append(random(0,250))
               
def draw():
    global models, theta, mind_offsets,timer
    timer+=1.0/30.0
    print(timer)
    colorMode(HSB)
    background(0)
    lights()
    strokeWeight(2)
    
    scale(min(timer*0.1+0.1,1))
    
    #1 head
    pushMatrix()
    rotateY(sin(timer)*0.15)
    fill(348,28,100,255)
    noStroke()
    models[0].render()
    fill(200,128)
    noStroke()
    models[1].render()
    popMatrix()
    
    #2 head
    pushMatrix()
    
    rotateY(sin(timer-10.5)*0.01)
    noFill()
    stroke(255,128)
    models[2].render()
    fill(197,43.3,67.1,255)
    noStroke()
    models[3].render()
    popMatrix()
    
    
    
    #wave
    theta += 0.08
    noStroke()
    fill(255)
    for m in range(5):
        angle = theta;
        
        for x in range(int(models[1].pos.x),int(models[2].pos.x)+100,20):    
            y = map(sin(angle), -0.5, 0.5, 200,250) + mind_offsets[m]
            transparency = map(cos(angle),0,1,0,255)
            z = map(sin(angle),0,20,0,500)
            pushMatrix()
            translate(x,y,z)
            fill(200,255,255,transparency)   
            sphere(10)
            popMatrix()
              
            
            angle += mind_offsets[m]/0.01 +0.1;    
            
    
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
        
class Cube:
    def __init__(self,x, y, z, s, h):
        self.pos = PVector(x, y, z)
        self.s = s
        self.h = h
        self.y = 0
    def render(self):
        while(self.y<=100):
            pushMatrix()
            translate(self.pos.x, self.pos.y + self.y, self.pos.z)
            scale(self.s)
            
            stroke(self.h, 255, 255)
            noFill()
            box(10)
            popMatrix()
            self.y+=1
            
                    
        
