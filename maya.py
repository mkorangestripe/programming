from maya import cmds

cmds.help("polySphere") # help on polySphere command

# List items
cmds.ls() # list itmes in the scene
shapes = cmds.ls(shapes=True) # assign all shapes in scene to a variable
selection1 = cmds.ls(selection=True) # assign the current selected itmes to a variable

# Selection
cmds.select(clear=True) # clear the current selected items
sphere1 = cmds.select("*pSphere1", add=True) # assign pSphere1 to a variable

# Nurbs
cmds.sphere(radius=3) # create a nurbs sphere

# polyCube
cube1 = cmds.polyCube(width=2,height=3) # create a polyCube
cubeShape1 = cube1[0] # assign the geometry to a varaible

# polySphere
cmds.polySphere(radius=3) # create a polySphere
sphere1_radius = cmds.polySphere("polySphere1", query=True, radius=True) # assign its radius to a variable
cmds.polySphere("polySphere1", edit=True, radius=5) # change the radius size

# Create ten posts in a row:
Z=-1
for i in range(-1,9,2):
    cmds.polyCube(width=0.25,depth=0.25,height=10)
    Z=Z+2
    cmds.move(0,5,Z)
    cmds.polyCube(width=0.25,depth=0.25,height=10)
    cmds.move(0,5,-Z)

# Select all pCube* itmes:
cmds.select("pCube*", add=True)
