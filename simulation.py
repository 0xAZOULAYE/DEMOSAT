import time
import FreeCAD as App
import FreeCADGui as Gui
import FreeCAD.a2plus.a2p_solversystem as a2p_solver

step = 1.0
timeout = 0.001
angle = 0

def update():
  global angle
  angle += step


doc = FreeCAD.activeDocument()
sw = doc.getObject("star_wheel_001")


while angle < 360:
	update()
	position = App.Base.Vector(50.0,0.0,85.0)
	center = App.Base.Vector(50.0,0.0,85.0)
	axis = App.Base.Vector(-1.0,0.0,0.0)
	rotation = App.Rotation(axis,angle)
	sw.Placement = App.Placement(position,rotation,center)
	a2p_solver.solveConstraints(
		doc,
		useTransaction=False
		)
	Gui.updateGui()
	time.sleep(timeout)

