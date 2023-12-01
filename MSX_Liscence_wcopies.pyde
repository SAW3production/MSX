scale_factor = 0.0  # Start with zero scale
rotation_angle = 0.0  # Initial rotation angle
depth_scaling = 1.0  # Initial depth scaling factor
depth_scaling_direction = 1  # Initial direction for depth scaling (1 for increasing, -1 for decreasing)

num_copies = 20  # Number of copies
copies = []  # List to store copies

def setup():
    global msx_model, copies
    size(1920, 1080, P3D)
    colorMode(HSB)
    msx_model = Model("msx.obj", 0, 0, 0, 50, 200)  # Start at (0, 0, 0)

    # Create copies with different scales and positions
    for _ in range(num_copies):
        scale_factor = random(0.1, 0.5)  # Random scale between 0.1 and 0.5
        x_pos = random(-width / 2, width / 2)
        y_pos = random(-height / 2, height / 2)
        z_pos = random(-200, 200)
        copies.append(Model("msx.obj", x_pos, y_pos, z_pos, 50 * scale_factor, 200))

def draw():
    global scale_factor, rotation_angle, depth_scaling, depth_scaling_direction

    colorMode(RGB)
    blendMode(SUBTRACT)
    fill(255, 50)
    rect(0, 0, width * 4, height * 4)
    blendMode(BLEND)
    colorMode(HSB)

    lights()
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

    scale(1, 1, depth_scaling)

    # Render the copies
    for copy in copies:
        pushMatrix()
        copy.render(scale_factor)
        rotateY(sin(rotation_angle))
        popMatrix()

    # Render the main object
    msx_model.render(scale_factor)

    # Increment rotation angle for the next frame (faster rotation)
    rotation_angle += radians(2.0)

class Model:
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
