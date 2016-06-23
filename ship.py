import math
from entity import Entity

class Ship(Entity):
	def __init__(self, surface, pixelsPerUnit):
		Entity.__init__(self, surface, pixelsPerUnit)
		self.topSpeed = 0.5
		self.topAngularSpeed = 180.0
		self.maxAcceleration = 1.0
		self.maxAngularAcceleration = 180
	
	def update(self, timestep, target):
		displacementX = target[0]-self.position[0]
		displacementY = target[1]-self.position[1]
		distance = math.sqrt(displacementX**2 + displacementY**2)
		if distance == 0: distance = 1
		normalX = displacementX/distance
		normalY = displacementY/distance
		
		accelerationX = normalX*self.maxAcceleration
		accelerationY = normalY*self.maxAcceleration
		self.velocity = self.velocity[0]+accelerationX*timestep, self.velocity[1]+accelerationY*timestep
		
		angleTo = math.atan2(normalY, normalX)*180/math.pi+180
		angleDifference = angleTo - self.angle
		if angleDifference > 180: angleDifference -= 360
		
		angularAcceleration = angleDifference/180*self.maxAngularAcceleration
		
		self.angularVelocity += angularAcceleration*timestep
		
		relativeSpeed = self.speed()/self.topSpeed
		if relativeSpeed > 1:
			self.velocity = (self.velocity[0]/relativeSpeed, self.velocity[1]/relativeSpeed)
		
		if self.angularVelocity > self.topAngularSpeed:
			self.angularVelocity = self.topAngularSpeed
		elif self.angularVelocity < -self.topAngularSpeed:
			self.angularVelocity = -self.topAngularSpeed
		
		Entity.update(self, timestep)
