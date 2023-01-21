import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")
x=1
y=2
z=1

pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[x,y,z])

pyrosim.End()