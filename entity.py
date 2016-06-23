from math import sqrt
from pygame.transform import rotozoom

class Entity:
	def __init__(self, surface, pixelsPerUnit):
		# Position is in game units, not pixels.  Angle is 0 to 360, proceeding
		# counterclockwise from the right.  Velocities are per second.
		self.position = (0, 0)
		self.velocity = (0, 0)
		self.angle = 0
		self.angularVelocity = 0
		
		self.surface = surface
		self.pixelsPerUnit = pixelsPerUnit
	
	def speed(self):
		return sqrt(self.velocity[0]**2 + self.velocity[1]**2)
	
	def update(self, timestep):
		self.position = (self.position[0]+self.velocity[0]*timestep, self.position[1]+self.velocity[1]*timestep)
		self.angle += self.angularVelocity*timestep
	
	def draw(self, destinationSurface, pixelsPerUnit):
		scale = pixelsPerUnit / self.pixelsPerUnit
		transformedSurface = rotozoom(self.surface, self.angle, scale)
		pixelX = destinationSurface.get_width()/2 + self.position[0]*pixelsPerUnit - transformedSurface.get_width()/2
		pixelY = destinationSurface.get_height()/2 + self.position[1]*pixelsPerUnit - transformedSurface.get_height()/2
		destinationSurface.blit(transformedSurface, (pixelX, pixelY))
