import random


class Leg:
    """
    Leg class - Represents one leg of the robotic dog

    Students should implement movement and control logic for each leg.
    """

    def __init__(self, leg_id, position):
        """
        Initialize a leg

        Args:
            leg_id (int): Unique identifier for this leg (1-4)
            position (str): Position of the leg ("front-left", "front-right", "back-left", "back-right")
        """
        self.id = leg_id
        self.position = position
        self.status = "active"
        self._angle = 0

    def move(self, angle):
        """
        Move the leg to a specific angle

        Args:
            angle (float): The angle to move the leg to
        """
        self._angle = angle

    def reset(self):
        """Reset the leg to its default position"""
        self._angle = 0

    def __str__(self):
        """String representation of the leg"""
        return f"Leg {self.id} ({self.position}) at angle {self._angle}°"


# ====== INHERITANCE EXAMPLE 1 ======
class AdvancedLeg(Leg):
    """
    AdvancedLeg class - Inherits from Leg and adds advanced movement features.
    Demonstrates inheritance and polymorphism.
    """

    def move(self, angle):
        """
        Override the base move() method with smoother motion.
        """
        print(f"[AdvancedLeg] Moving {self.position} smoothly to angle {angle}°")
        super().move(angle)

    def jump(self):
        """
        Makes the leg perform a jump-like motion.
        """
        print(f"[AdvancedLeg] {self.position} leg is jumping!")
        self._angle = 45  # temporary lifted angle
        self.reset()


class Sensor:
    """
    Sensor class - Represents sensors on the robotic dog
    """

    def __init__(self, sensor_type):
        """
        Initialize a sensor

        Args:
            sensor_type (str): Type of sensor ("ultrasonic", "IMU", "camera", etc.)
        """
        self.sensor_type = sensor_type
        self.reading = 0

    def read_data(self):
        """Read data from the sensor"""
        self.reading = random.uniform(0, 100)
        return self.reading

    def calibrate(self):
        """Calibrate the sensor"""
        self.reading = 0


# ====== INHERITANCE EXAMPLE 2 ======
class CameraSensor(Sensor):
    """
    CameraSensor class - Inherits from Sensor and adds image capture functionality.
    Demonstrates inheritance and polymorphism.
    """

    def read_data(self):
        """
        Override to simulate visual data (instead of numeric readings)
        """
        self.reading = f"Image captured at resolution 640x480"
        return self.reading

    def capture_image(self):
        """
        Simulates taking a photo.
        """
        print("[CameraSensor] Capturing image... Done!")


class RoboticDog:
    """
    RoboticDog class - Main class representing the robotic dog

    ============================================================================
    STUDENT TODO: Implement the move() and find_ball() methods to navigate!
    ============================================================================
    """

    def __init__(self, name):
        """Initialize the robotic dog"""
        self.name = name
        self.legs = {}
        self.sensors = []
        self.battery_level = 100

        # Position attributes
        self.x = 100
        self.y = 300
        self.target_x = 100
        self.target_y = 100
        self.size = 20
        self.velocity_x = 0
        self.velocity_y = 0
        self.prevx = 0
        self.prevy = 0
        self.success = [True]
        self.ideal = [True]
        self.up=[True]
        self.down=[True]
        self.right=[True]
        self.left=[True]
        self.prevdir=["x"]
        self.log=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    def add_leg(self, leg):
        """Add a leg to the robotic dog"""
        self.legs[leg.position] = leg

    def add_sensor(self, sensor):
        """Add a sensor to the robotic dog"""
        self.sensors.append(sensor)

    def help(self,dir,i):
        if self.log[i]==0:
            self.success = self.success + [0]
            self.ideal = self.ideal + [True]
            self.right = self.right + [True]
            self.down = self.down + [True]
            self.up = self.up + [True]
            self.left = self.left + [True]
            self.prevdir = self.prevdir + ["x"]
            self.log = self.log + [0]
            self.log[i]=1
        
        
        if self.prevx == self.x and self.prevy == self.y and self.success[i]==1 and self.ideal[i]==True:
            if self.prevdir[i]=="r":
                self.right[i]=False
            elif self.prevdir[i]=="l":
                self.left[i]=False
            elif self.prevdir[i]=="u":
                self.up[i]=False
            elif self.prevdir[i]=="d":
                self.down[i]= False
            if (self.right[i]==False and self.left[i] == False) or (self.up[i] == False and self.down[i] == False):
                 self.ideal[i]=False
                 self.success[i]=0
        if self.success[i]==1 and self.ideal[i]==True:
            self.move_dir(dir)
            self.prevdir[i]= dir
            self.success[i]=0
            return
        elif self.success[i]==0:
            if ((self.x!=self.prevx and (dir == "r" or dir =="l")) or (self.y!=self.prevy and (dir == "u" or dir=="d"))) and self.ideal[i]==True:
                    print("hi")
                 
                    self.ideal[i-1]=True 
                    self.right[i-1]=True
                    self.left[i-1]=True
                    self.up[i-1]=True
                    self.down[i-1]=True
                    self.ideal.pop(i)
                    self.success.pop(i)
                    self.right.pop(i)
                    self.down.pop(i)
                    self.up.pop(i)
                    self.left.pop(i)
                    self.prevdir.pop(i)
                    self.log[i]=0
                    return
            if True:
                if self.ideal[i]:
                    if dir == "u" or dir == "d":
                        if self.right[i]:
                         self.move_dir("r")
                         self.prevdir[i] = "r"
                        else:
                         self.move_dir("l")
                         self.prevdir[i] = "l"
                    else:
                         if self.up[i]:
                          self.move_dir("u")
                          self.prevdir[i] = "u"
                         else:
                          self.move_dir("d")
                          self.prevdir[i] = "d"
                    self.success[i]=1
                    self.prevx = self.x 
                    self.prevy = self.y 
                else:
                    if dir=="d" or dir =="u":
                         self.help("r",i+1)
                    else:
                         self.help("u",i+1)
    
    def move_dir(self,a):
        if a == "r":
            self.target_x += 5
            self.target_y = self.y

        elif a == "l":

            self.target_x += -5
            self.target_y = self.y 

        elif a == "u":

            self.target_y += -5
            self.target_x = self.x 

        elif a == "d":
            self.target_y += 5
            self.target_x = self.x 

    def find_ball(self, ball_pos, obstacle_data):
        dx = ball_pos[0] - self.x
        dy = ball_pos[1] - self.y
        move_speed = 2
        if self.x  == self.prevx and self.y == self.prevy:
            self.ideal[0] = False

        
        if abs(dx) > 5 and self.ideal[0]:
                 
                 if dx>0:
                     self.prevdir[0]="r"
                     self.move_dir("r")
                 else:
                     self.prevdir[0]="l"
                     self.move_dir("l")
                    
        elif abs(dy) > 5 and self.ideal[0]:
                 
                 if dy<0:
                     self.prevdir[0]="u"
                     self.move_dir("u")
                 else:
                     self.prevdir[0]="d"
                     self.move_dir("d")
        if self.ideal[0]:
            self.prevx = self.x 
            self.prevy = self.y
            return
        elif not self.ideal[0]:
             self.help(self.prevdir[0],1)

    def check_status(self):
        """Print the current status of the robotic dog"""
        print(f"\n{'=' * 50}")
        print(f"Robot: {self.name}")
        print(f"{'=' * 50}")
        print(f"Battery: {self.battery_level}%")
        print(f"Position: ({self.x}, {self.y})")
        print(f"Legs: {len(self.legs)}")
        print(f"Sensors: {len(self.sensors)}")
        print(f"{'=' * 50}\n")

    def recharge(self):
        """Recharge the battery to 100%"""
        self.battery_level = 100


if __name__ == "__main__":
    print("Testing RoboticDog implementation...")

    test_dog = RoboticDog("TestBot")

    # Add legs (showing inheritance)
    test_dog.add_leg(AdvancedLeg(1, "front-left"))
    test_dog.add_leg(Leg(2, "front-right"))
    test_dog.add_leg(Leg(3, "back-left"))
    test_dog.add_leg(AdvancedLeg(4, "back-right"))

    # Add sensors (including camera)
    test_dog.add_sensor(Sensor("ultrasonic"))
    test_dog.add_sensor(CameraSensor("camera"))

    test_dog.check_status()

    print("Testing movement...")
    test_dog.move(5, 0)
    print(f"New target position: ({test_dog.target_x}, {test_dog.target_y})")

    print("\nTesting leg behaviors...")
    for leg in test_dog.legs.values():
        leg.move(30)
        if isinstance(leg, AdvancedLeg):
            leg.jump()

    print("\nTesting sensors...")
    for sensor in test_dog.sensors:
        print(f"{sensor.sensor_type} reading: {sensor.read_data()}")

    print("\nTesting obstacle data format...")
    test_obstacles = [
        {'x': 200, 'y': 40, 'width': 30, 'height': 200},
        {'x': 400, 'y': 160, 'width': 30, 'height': 200}
    ]
    print(f"Sample obstacle: {test_obstacles[0]}")
    print(f"Obstacle at x={test_obstacles[0]['x']}, y={test_obstacles[0]['y']}")
    print(f"Size: {test_obstacles[0]['width']} x {test_obstacles[0]['height']}")

    print("\nImplementation test complete!")
    print("Run main.py to see your dog in action in the maze!")
