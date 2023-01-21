import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("world.sdf")


length=1
width=1
height=1 

x=1
y=1
z=.5

pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
#pyrosim.Send_Cube(name="Box2", pos=[2,1,2] , size=[length,width,height])
# for i in range (5):
#         for i in range(5):
#                 for i in range(10):
#                         pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])

#                         width=width*.90
#                         length=length*.90
#                         height=height*.90
#                         z=z+1
#                 z=.5
#                 x=x+1
#                 width=1
#                 length=1
#                 height=1
#         x=x-5
#         y=y+1        

pyrosim.End()