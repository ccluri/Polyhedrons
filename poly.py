from numpy import math,sqrt,fabs,sin,cos
from scipy import random#, randint
from updatepaintGL import *

class poly(object):
	def __init__(self,parent=None):
		self.window = GLWidget()
		#self.window.translate([0.0, 0.0, 100.0])
		self.window.show()
		#self.mCarlo(20,100)
		
	def distanceSqr(self,a,b=[0,0,0]):
		return (a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2
	
	def distance(self,a,b=[0,0,0]):
		return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2)
	
	def disperseRand(self,n):
		a=[]	
		c=[]
		i=0
		while i<n:
			xy=[random.uniform(-1,1),random.uniform(-1,1)]
			if (xy[0]**2+xy[1]**2)<=1:
				a.append(xy)
				i+=1		
		for i in range(0,len(a)):
			c.append([a[i][0],a[i][1],sqrt(1-(a[i][0]**2+a[i][1]**2))])
		for i in range(0,len(c)):	#randomly change sign of the z coord
			if random.randint(0,1):
				c[i][2]=c[i][2]*-1
		return c

		
	def forceVectors(self,c):
		force=[]
		energy = 0
		for i in range(0,len(c)):
			f=[]
			force.append([0,0,0])
			for j in range(0,len(c)):	#i is self, j is the other charge
				if j!=i:
					r=self.distance(c[i],c[j])
					r3=(r**3) 
					f.append([(c[i][0]-c[j][0])/r3,(c[i][1]-c[j][1])/r3,(c[i][2]-c[j][2])/r3])
					
					energy = energy + (1/r)
				else: 
					f.append([0,0,0])
					
				force[i][0]=force[i][0]+f[j][0]
				force[i][1]=force[i][1]+f[j][1]	
				force[i][2]=force[i][2]+f[j][2]	
		energy = energy/2 # each counted twice
		return force,energy
		
	def energySystem(self,c):
		energy =0
		for i in range(0,len(c)):
			for j in range(0,len(c)):	#i is self, j is the other charge
				if j!=i:
					rInv = 1/self.distance(c[i],c[j])
					#if math.isnan(rInv):
					#	rInv = 20
					energy = energy + rInv
		return energy/2
		


	def rotateBy(self,a,b,theta): #rotates a abt b by theta.
		cT = cos(theta)
		sT = sin(theta)
		c = [0,0,0]
		c[0] = a[0]*(cT+(1-cT)*b[0]**2) + a[1]*(b[0]*b[1]*(1-cT)-b[2]*sT) + a[2]*(b[0]*b[2]*(1-cT)+b[1]*sT)
		c[1] = a[0]*(b[1]*b[0]*(1-cT)+b[2]*sT) + a[1]*(cT+(1-cT)*b[1]**2) + a[2]*(b[1]*b[2]*(1-cT)-b[0]*sT)
		c[2] = a[0]*(b[2]*b[0]*(1-cT)-b[1]*sT) + a[1]*(b[2]*b[1]*(1-cT)+b[0]*sT) + a[2]*(cT+(1-cT)*b[2]**2)
		return c
	
	def mCarlo(self,n_pts,runs=100):
		p = self.disperseRand(n_pts)
		#eOld = energySystem(p)
		f,eOld = self.forceVectors(p)
		count = 0
		angle = 0.3
		number = [len(p)*runs]
		randIndxs = random.randint(0,len(p),[len(p)*runs])
#		print len(randIndxs)
		for r in range(0,runs):
			
			#for i in range(0,len(p)):
			for q in range(0,len(p)):
				#print q*(r+1)
				i = randIndxs[q*(r+1)]	
				#print i
				magnitude = self.distance(f[i])			
				dirForce = [f[i][0]/magnitude,f[i][1]/magnitude,f[i][2]/magnitude]
				
				pOld = p[i]
				p[i] = self.rotateBy(p[i],dirForce,angle)
				
				eNew = self.energySystem(p)
				
				if eNew > eOld:	#revert back
					p[i] = pOld
					count +=1
				else:
					eOld = eNew
			
			self.window.update(p)
			self.window.updateGL()
			self.window.show()
			self.window.raise_()
			
			f,e = self.forceVectors(p)			
			print eOld,count		
		print count
		
app = QtGui.QApplication(sys.argv)
mainWindow = poly()
mainWindow.mCarlo(5,500)
sys.exit(app.exec_())

