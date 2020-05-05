from maya import cmds

# Reload an imported module:
import objectRenamer as ore
reload(ore)

cmds.help("polySphere") # help on polySphere command

# List items
cmds.ls() # list objects in the scene
cmds.ls(long=True) # list objects in the scene, long format
cmds.ls(shapes=True) # list shape objects
cmds.ls(selection=True) # list objects that are currently selected

# object info
cmds.listRelatives("pSphere1") # list related objects
# If type if None, then create an empty list:
children = cmds.listRelatives("pSphereShape1", children=True, fullPath=True) or []
cmds.objectType("pSphere1") # get object type

cmds.listAttr('pPipe1') # list attributes on the object
cmds.getAttr('polyExtrudeFace1.inputComponents') # get attributes, a list of faces here


# Selection
cmds.select(clear=True) # clear the current selection
cmds.select("pCube1") # select pCube1
cmds.select("pSphere*", add=True) # add all pSphere* itmes to the current selection
cmds.select(cmds.ls(shapes=True)) # select all shapes

cmds.rename("pSphere1", "ball1") # rename object

# Nurbs
cmds.sphere(radius=3) # create a nurbs sphere

# polyCube
cube1 = cmds.polyCube(width=2,height=3) # create a polyCube
cubeShape1 = cube1[0] # assign the geometry to a varaible

# polySphere
cmds.polySphere(radius=3) # create a polySphere
sphere1_radius = cmds.polySphere("polySphere1", query=True, radius=True) # assign its radius to a variable
cmds.polySphere("polySphere1", edit=True, radius=5) # change the radius size

# Create ten posts along the Z axis between -9 and 9 spaced 2 units apart:
Z=-1
for i in range(0,5):
    Z += 2
    cmds.polyCube(width=0.25,depth=0.25,height=10)
    cmds.move(0,5,Z)
    cmds.polyCube(width=0.25,depth=0.25,height=10)
    cmds.move(0,5,-Z)

# Parent a cube to a circle and lock translate, rotate, and scale on the cube:
cube1 = cmds.polyCube()
cubeShape1 = cube1[0]
circle1 = cmds.circle()
circleShape1 = circle1[0]
cmds.parent(cubeShape1, circleShape1)
cmds.setAttr(cubeShape1+".translate", lock=True)
cmds.setAttr(cubeShape1+".rotate", lock=True)
cmds.setAttr(cubeShape1+".scale", lock=True)
