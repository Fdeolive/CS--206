import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1

x = 0
y = 0
z = .5

def Create_World():
        pyrosim.Start_SDF("world.sdf")

        

        pyrosim.Send_Cube(name="Box", pos=[x+3, y+3, z], size=[
                          length, width, height])
        pyrosim.End()



def Create_Robot():
#This is where we are going to store the robots body
        
        # pyrosim.Start_URDF("body.urdf")
        # #back leg
        # pyrosim.Send_Cube(name="BackLeg", pos=[0, 0, .5], size=[length, width, height])

        # #link between leg and torso   
        # pyrosim.Send_Joint( name = "BackLeg_Torso" , parent= "BackLeg" , child = "Torso" , type = "revolute", position = [0,.5,1]) 
 
        # #toso
        # pyrosim.Send_Cube(name="Torso", pos=[0, .5, .5], size=[length, width, height])

        # # #link to front leg and torso
        # pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,1,-1]) 
 
        #  #front leg
        # pyrosim.Send_Cube(name="FrontLeg", pos=[x, .5, 0.5], size=[length, width, height])

        pyrosim.Start_URDF("body.urdf")

         #toso
        
        pyrosim.Send_Cube(name="BackLeg", pos=[.5, 0, .5], size=[length, width, height])
       
        # # # #link between leg and torso   
        pyrosim.Send_Joint( name = "BackLeg_Torso" , parent= "BackLeg" , child = "Torso" , type = "revolute", position = [1,0,1]) 

         # #  #back leg
        
        pyrosim.Send_Cube(name="Torso", pos=[.5, 0, .5], size=[length, width, height])
 
       
        # # #link to front leg and torso
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [1,0,0]) 
 
        #  #front leg
        pyrosim.Send_Cube(name="FrontLeg", pos=[.5, 0, -.5], size=[length, width, height])

        

#         pyrosim.Send_Cube(name="Link0", pos=[x, y, z], size=[length, width, height])
#        #link (Position of the joint is in between them)
#         pyrosim.Send_Joint( name = "Link0_Link1" , parent= "Link0" , child = "Link1" , type = "revolute", position = [0,0,1.0])
# #        #leg
#         pyrosim.Send_Cube(name="Link1", pos=[0, 0, .5], size=[length, width, height])
       
#         pyrosim.Send_Joint( name = "Link1_Link2" , parent= "Link1" , child = "Link2" , type = "revolute", position = [0,0,1.0])
       
#         pyrosim.Send_Cube(name="Link2", pos=[0, 0, .5], size=[length, width, height])
        
#         pyrosim.Send_Joint( name = "Link2_Link3" , parent= "Link2" , child = "Link3" , type = "revolute", position = [0,0.5,.5])
        
#         pyrosim.Send_Cube(name="Link3", pos=[0, 0.5, 0], size=[length, width, height])

#         #connect between 3 and 4
#         pyrosim.Send_Joint( name = "Link3_Link4" , parent= "Link3" , child = "Link4" , type = "revolute", position = [0,1,0])

#         #Link 4
#         pyrosim.Send_Cube(name="Link4", pos=[0, 0.5, 0], size=[length, width, height])

#         #connection between 4 and 5 

#         pyrosim.Send_Joint( name = "Link4_Link5" , parent= "Link4" , child = "Link5" , type = "revolute", position = [0,0,-1])
        
#         #link 5
#         pyrosim.Send_Cube(name="Link5", pos=[0, 0.5, 0], size=[length, width, height])

#         # #connection between 5 and 6 
#         pyrosim.Send_Joint( name = "Link5_Link6" , parent= "Link5" , child = "Link6" , type = "revolute", position = [0,0,-1])
        
#         pyrosim.Send_Cube(name="Link6", pos=[0, 0.5, 0], size=[length, width, height])
        pyrosim.End()

Create_World()
Create_Robot()
