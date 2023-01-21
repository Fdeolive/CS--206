import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")
height=3
width=2
length=1
x=1
y=1
z=1.5

pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])

pyrosim.End()