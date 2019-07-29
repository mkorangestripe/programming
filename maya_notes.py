import maya.cmds
import maya.cmds as cmds
cmds.ls()

maya.cmds.sphere(radius=4)
maya.cmds.polySphere()

maya.cmds.polyCube()
maya.cmds.polyCube(width=2,height=3)

cmds.help("polySphere")

maya.cmds.polySphere("polySphere1", query=True, radius=True)

maya.cmds.polySphere("polySphere1", edit=True, radius=5)
cmds.ls(shapes=True)
cmds.ls(selection=True)

cmds.select(clear=True)
cmds.select("*pSphere1", add=True)


Z=-1
for i in range(-1,9,2):
    cmds.polyCube(width=0.25,depth=0.25,height=10)
    Z=Z+2
    cmds.move(0,5,Z)
    cmds.polyCube(width=0.25,depth=0.25,height=10)
    cmds.move(0,5,-Z)


cmds.select("pCube*", add=True)
