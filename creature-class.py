# class World:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#         self.creatures = []

#     def addCreature(creature):
#         self.creatures.append(creature)

#     def move():
#         for creature in self.creatures():
#             creature.move(1)
#         ...code to draw all the creatures here...


# class Creature:
#     def __init__(self, x, y, direction):
#         self.x = x
#         self.y =     y
#         self.direction  = 0   #an angle, maybe measured from 0 to 1 or 0 to 360 degrees

#     def move(distance):
#         self.x += distance*math.cos(2*pi*self.direction/360) #this formula might not be quite right
#         self.y += distance*math.sin(2*pi*self.direction/360)  #this formula might not be quite right


# if __name__ == “__main__”:

# c1 = Creature(0,0,0)
# c2 = Creature(3,2,17)

# world  = World(100, 50)
# world.addCreature(c1)
# world.addCreature(c2)

# for i in xrange(10):
#     world.move()
