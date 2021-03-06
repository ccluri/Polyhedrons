import sys
from PyQt4 import QtCore, QtGui
from PyGLWidget import PyGLWidget
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class GLWidget(PyGLWidget):
	
    def paintGL(self):
        PyGLWidget.paintGL(self)
#        self.lights()
        scale = 8
        glColor3f(1,0,0)
        #glEnable(GL_BLEND)
        #glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        #gluSphere(gluNewQuadric(),0.95/scale, 20, 20)
        glColor(0,0,1)
        glPointSize(3)
#        glDisable(GL_LIGHTING)
        glBegin(GL_POINTS)
        #glPoint(1,1,1)
        for location in self.location:
        	glVertex3f(location[0]/scale,location[1]/scale,location[2]/scale)
        glEnd()

        for line in self.lines:
            glColor(0, 1, 0)
            glLineWidth(4)
            glBegin(GL_LINES)
            glVertex3f(line[0][0]/scale,line[0][1]/scale,line[0][2]/scale)
            glVertex3f(line[1][0]/scale,line[1][1]/scale,line[1][2]/scale)
            glEnd()
#	glEnable(GL_LIGHTING)
	
    def lights(self):
    	glMatrixMode(GL_MODELVIEW)
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
	glEnable(GL_COLOR_MATERIAL)

	light0_pos = 200.0, 200.0, 300.0, 0
	diffuse0 = 1.0, 1.0, 1.0, 1.0
	specular0 = 1.0, 1.0, 1.0, 1.0
	ambient0 = 0, 0, 0, 1

	glMatrixMode(GL_MODELVIEW)
	glLightfv(GL_LIGHT0, GL_POSITION, light0_pos)
	glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse0)
	glLightfv(GL_LIGHT0, GL_SPECULAR, specular0)
	glLightfv(GL_LIGHT0, GL_AMBIENT, ambient0)
    
    def update(self,p):
	self.location = p

    def drawLines(self,p1,p2):
        self.lines.append([p1,p2])
        
