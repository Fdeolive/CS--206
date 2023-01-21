import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1

x = 1
y = 1
z = .5

def Create_World():
        pyrosim.Start_SDF("world.sdf")

        

        pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[
                          length, width, height])
        pyrosim.End()



def Create_Robot():
#This is where we are going to store the robots body
        
       pyrosim.Start_URDF("body.urdf")
       pyrosim.Send_Cube(name="Torso", pos=[x, y, z], size=[length, width, height])
       pyrosim.End()

Create_World()
Create_Robot()
