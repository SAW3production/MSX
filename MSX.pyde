matrix_rain = []
characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()-=_+[]{}|;':,.<>?/ "
def setup():
    global gates,eagle
    size(1920,1080,P3D)
    gates = Model("18370_Shinto-Torii_Gate_v1.obj",500,height/2,0,50,255,PI/2,0)
    eagle=Model("20433_Bald_Eagle_v1.obj",1500,height/2,0,25,255,PI/2,PI - PI/4)
    
    #matrix
    for i in range(-200, width+400, 20):
        column = []
        for j in range(0, height*2, 20):
            column.append(MatrixChar(i, j))
        matrix_rain.append(column)

def draw():
    background(0)
    lights()
    global gates, eagle 
    pushMatrix()
    fill(50,10,5)
    if(not eagle.move_to_center()):
        eagle.render()
    popMatrix()
    pushMatrix()
    fill(255,0,0)
    if(not gates.move_to_center()):
        gates.render()
    
    popMatrix()
    
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
        
    def move_to_center(self):
        target_x = width / 2
        target_y = height / 2
        speed = 2
         
        if self.pos.x < target_x:
            self.pos.x += speed
        elif self.pos.x > target_x:
            self.pos.x -= speed
    
        if self.pos.y < target_y:
            self.pos.y += speed
        elif self.pos.y > target_y:
            self.pos.y -= speed  
                    
        if abs(self.pos.x - target_x) < 2 and abs(self.pos.y - target_y) < 2:
            return True
        else:
            return False
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
