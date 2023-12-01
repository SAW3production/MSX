models = []
leaves = []
stars = []
mind_offsets = []
theta = 0
timer = 0.0
characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()-=_+[]{}|;':,.<>?/ "
matrix_rain = []

#Marko
scale_factor = 0.0  # Start with zero scale
rotation_angle = 0.0  # Initial rotation angle
depth_scaling = 1.0  # Initial depth scaling factor
depth_scaling_direction = 1  # Initial direction for depth scaling (1 for increasing, -1 for decreasing)

num_copies = 20  # Number of copies
copies = []  # List to store copies

def setup():
    frameRate(30)
    global models,mind_offsets,leaves,characters,matrix_rain
    fullScreen(P3D)
    colorMode(HSB,360,100,100,255)
    
    #Ihor's part
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
        
    #Alex's
    global gates,eagle
    gates = Model("18370_Shinto-Torii_Gate_v1.obj",500,height/2,0,50,255,PI/2,0)
    eagle=Model("20433_Bald_Eagle_v1.obj",1420,height/2,0,25,255,PI/2,PI - PI/4)
    
    #Marko
    global msx_model
    msx_model = ModelScale("msx.obj", 0, 0, 0, 50, 200)  # Start at (0, 0, 0)

    # Create copies with different scales and positions
    for _ in range(num_copies):
        scale_factor = random(0.1, 0.5)  # Random scale between 0.1 and 0.5
        x_pos = random(-width / 2, width / 2)
        y_pos = random(-height / 2, height / 2)
        z_pos = random(-200, 200)
        copies.append(ModelRotating("msx.obj", x_pos, y_pos, z_pos, 50 * scale_factor, 200))
               
def draw():
    global msx_model, models, theta, mind_offsets,timer,leaves,characters,matrix_rain,stars,scale_factor, rotation_angle, depth_scaling, depth_scaling_direction
    timer+=1.0/30.0
    if(int(timer)< 0.2 or sin(timer)<-0.2):
            background(0)
    print(timer)
    lights()
    colorMode(HSB)
    #1 Scene
    if(timer<10):
        
        r = 10
        c = 1
        
        
        #Matrix
        pushMatrix()
        translate(0,-100,-200)
        scale(1.2)
        for column in matrix_rain:
            for matrix_char in column:
                matrix_char.display()
                matrix_char.fall()
        popMatrix()
        
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
    #2 Scene
    if(timer>10 and timer <17):
        global gates, eagle 
        pushMatrix()
        translate(0,-100,-200)
        scale(1.2)
        for column in matrix_rain:
            for matrix_char in column:
                matrix_char.display()
                matrix_char.fall()
        popMatrix()
        pushMatrix()
        fill(20,70,60)
        if(not eagle.move_to_center()):
            eagle.render()
        popMatrix()
        pushMatrix()
        fill(0,100,100)
        if(not gates.move_to_center()):
            gates.render()
        
        popMatrix()
        
    #Scene 3
    if(timer>17):
        strokeWeight(5)
        translate(width / 2, height / 2)
        
        # Automatically adjust scale_factor using a slower increase
        scale_factor = min(scale_factor + 0.002, 1.0)  # Increase scale gradually up to 1.0
    
        # Move the entire object in circles in terms of X, Y, and Z
        x_offset = sin(rotation_angle) * 100
        y_offset = cos(rotation_angle) * 100
        z_offset = depth_scaling * 100
        translate(x_offset, y_offset, z_offset)
    
        # Depth scaling to create back-and-forth motion
        depth_scaling += 0.01 * depth_scaling_direction
        if depth_scaling > 3 or depth_scaling < 0.8:
            depth_scaling_direction *= -1
    
        # Render the main object
        msx_model.render(scale_factor)
    
        # Increment rotation angle for the next frame (faster rotation)
        rotation_angle += radians(2.0)
        scale(1, 1, depth_scaling)
    
        # Render the copies
        for copy in copies:
            pushMatrix()
            copy.render(scale_factor)
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
        
class ModelScale:
    def __init__(self, file_name, x, y, z, s, h):
        self.pos = PVector(x, y, z)
        self.s = s
        self.h = h
        self.sh = loadShape(file_name)
        self.sh.disableStyle()

    def render(self, scale_factor):
        pushMatrix()
        translate(self.pos.x, self.pos.y, self.pos.z)
        rotateX(-HALF_PI)

        scale(self.s * scale_factor)  # Apply scaling
        stroke((self.h + frameCount) % 256, 255, 255)  # Use frameCount for automatic color change
        fill((self.h + frameCount) % 256, 255, 255)
        shape(self.sh)
        popMatrix()
        
class ModelRotating:
    def __init__(self, file_name, x, y, z, s, h):
        self.pos = PVector(x, y, z)
        self.s = s
        self.h = h
        self.sh = loadShape(file_name)
        self.sh.disableStyle()
        self.theta = 0

    def render(self, scale_factor):
        pushMatrix()
        translate(self.pos.x, self.pos.y, self.pos.z)
        rotateX(-HALF_PI)
        rotateZ(self.theta)

        scale(self.s * scale_factor)  # Apply scaling
        stroke((self.h + frameCount) % 256, 255, 255)  # Use frameCount for automatic color change
        fill((self.h + frameCount) % 256, 255, 255)
        shape(self.sh)
        self.theta +=0.1
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
        
        star(0,0,5,10,5)
        popMatrix()
def star(x, y, radius1, radius2, npoints):
    angle = TWO_PI / npoints
    halfAngle = angle/2.0
    beginShape()
    a = 0
    while (a<TWO_PI):
        sx = x + cos(a) * radius2
        sy = y + sin(a) * radius2
        vertex(sx, sy)
        sx = x + cos(a+halfAngle) * radius1
        sy = y + sin(a+halfAngle) * radius1
        vertex(sx, sy)
        a+=angle
    endShape(CLOSE)       
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
        
