#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
author: Guilherme Marques LSA 2014
Based in tutorials of Jan Bodnar
"""
import rospy
from std_msgs.msg import String
from std_msgs.msg import UInt8
from std_msgs.msg import UInt16
from std_msgs.msg import Int16
from ttk import Frame, Label, Scale, Style, Entry, Button
from Tkinter import *
#from Tkinter import Tk, BOTH, IntVar

gripperSpeed = UInt16()
gripperForce = UInt16()
gripperPosition = Int16()
gripperDistance = UInt8()
gripperRotationX = Int16()
gripperCurrent = Int16()
    
class GripperDemo(Frame):
  
    def __init__(self, parent1):
        Frame.__init__(self, parent1)   
        self.parent = parent1
        self.initUI()
        
    def initUI(self):
        self.parent.title("Gripper Demo")
        self.style = Style()
        self.style.theme_use("default")        
        self.pack(fill=BOTH, expand=1)

        #scale1 - Gripper Pos
        ScaleGripperPos = Scale(self, from_=0, to=100, orient=HORIZONTAL, length=300, resolution=1, command=self.onScaleGripperPos)
        ScaleGripperPos.grid(row=1, column=2)
        
        self.label = Label(self, text="Gripper Pos ")        
        self.label.grid(row=1, column=1)
        
        self.GripperPos = IntVar()
        self.labelScaleGripperPos = Label(self, text=0, textvariable=self.GripperPos)        
        self.labelScaleGripperPos.grid(row=1, column=3)

        #scale2 - X ROTATION 
        scaleRotX = Scale(self, from_=0, to=650, orient=HORIZONTAL, length=300, resolution=1, command=self.onScaleXAxisRot)
        scaleRotX.grid(row=2, column=2)
        scaleRotX.set(450)
        
        self.label = Label(self, text="X Axis Rotation ")        
        self.label.grid(row=2, column=1)
        
        self.labelRotX = Label(self)        
        self.labelRotX.grid(row=2, column=3)

        #Entry1 - Force
        self.entryForce = Entry(self);
        self.entryForce.grid(row=3, column=2)
        self.entryForce.insert(0,"50") #35=700

        #self.forceString = StringVar()
        #self.forceString.set(1023);
        self.labelForce = Label(self)        
        self.labelForce.grid(row=3, column=3)
        #self.entryForce.insert(1023,self.force.get())
        #self.entry1.delete(0,END) #delete entry text
        #entry.bind("<Return>", callback) #calls callback function after hit "enter"

        self.label = Label(self, text="Current (A)")        
        self.label.grid(row=6, column=1)
        self.labelCurrent = Label(self)        
        self.labelCurrent.grid(row=6, column=3)

        #Entry2 - Speed
        self.entrySpeed = Entry(self);
        self.entrySpeed.grid(row=4, column=2)
        self.entrySpeed.insert(0,"4000")
        self.labelSpeed = Label(self)        
        self.labelSpeed.grid(row=4, column=3)

        #Entry2 - Active Distance   
        self.entryDistance = Entry(self);
        self.entryDistance.grid(row=5, column=2)

        #Entry3 - Send Command
        self.entrySendCommand = Entry(self);
        self.entrySendCommand.grid(row=8, column=2)

        self.activeDistance = IntVar()
        self.activeDistance.set(15)
        self.labelActiveDistance = Label(self)        
        self.labelActiveDistance.grid(row=5, column=3)
        self.entryDistance.insert(0,self.activeDistance.get())

        #Button1 - close
        self.button1 = Button(self, text="close", command=self.gripperClose)
        self.button1.grid(row=7, column=1)
        #Button2 - open
        self.button2 = Button(self, text="open", command=self.gripperOpen)
        self.button2.grid(row=7, column=2)
        #Button3 - home
        self.button3 = Button(self, text="home", command=self.gripperHomeRoutine)
        self.button3.grid(row=7, column=3)
        #Button4 - send command
        self.button4 = Button(self, text="send", command=self.sendCommand)
        self.button4.grid(row=8, column=3)
        #Button3
        self.buttonForce = Button(self, text="forceSetPoint (mg)", command=self.gripperSetForce)
        self.buttonForce.grid(row=3, column=1)
        #Button4
        self.buttonSpeed = Button(self, text="speedSetPoint (mseg/close)", command=self.gripperSetSpeed) 
        #80degree each finger = to move 40 degree to close
        self.buttonSpeed.grid(row=4, column=1)
        #Button5
        self.buttonDistance = Button(self, text="distanceSetPoint (Cm)", command=self.gripperSetDistance)
        self.buttonDistance.grid(row=5, column=1)

    def gripperOpen(self):
        message = "open"
        rospy.loginfo(message)
        pub.publish(message)

    def gripperClose(self):
        message = "close_101" #101 is the auto close command
        rospy.loginfo(message)
        pub.publish(message)

    def gripperHomeRoutine(self):
        message = "home"
        rospy.loginfo(message)
        pub.publish(message)

    def sendCommand(self):
        message = self.entrySendCommand.get()
        rospy.loginfo(message)
        pub.publish(message)

    def gripperSetForce(self):
        aux = map(int(self.entryForce.get()),0,1200,0,1023)
        message = "setForce_"+str(aux)
        rospy.loginfo(message)
        pub.publish(message)

    def gripperSetSpeed(self):
        #0.174seg 80graus (6.0V sem carga)
        #4s 80 graus na velocidade minima 50ms
        aux = map(int(self.entrySpeed.get()),4000,174,50,0)
        if aux < 0:
            aux = 0
        message = "setSpeed_"+str(aux)
        rospy.loginfo(message)
        pub.publish(message)

    def gripperSetDistance(self):
        aux = self.entryDistance.get()
        message = "setDistance_"+str(aux)
        rospy.loginfo(message)
        pub.publish(message)
        
    def onScaleGripperPos(self, x):
        aux = int(float(x))
        self.GripperPos.set(aux)
        message = "close_"+str(aux)
        rospy.loginfo(message)
        pub.publish(message)
        
    def onScaleXAxisRot(self, x):
        aux = int(float(x))
        message = "rotate_"+str(aux)
        rospy.loginfo(message)
        pub.publish(message)

    def updateLabels(self):
        aux = map(gripperForce.data,0,1023,0,1200)
        self.labelForce.config(text=str(aux))
        aux = int(self.entrySpeed.get())
        if aux < 174:
            aux = 174
        self.labelSpeed.config(text=str(aux))
        self.labelActiveDistance.config(text=str(gripperDistance.data))
        self.labelRotX.config(text=str(gripperRotationX.data))
        self.labelCurrent.config(text=str((gripperCurrent.data-511)*0.024))

    
def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

#ROS callbacks
def callSpeed(msg):
    gripperSpeed.data = msg.data

def callForce(msg):
    gripperForce.data = msg.data

def callPosition(msg):
    gripperPosition.data = msg.data

def callDistance(msg):
    gripperDistance.data = msg.data

def callRotationX(msg):
    gripperRotationX.data = msg.data

def callCurrent(msg):
    gripperCurrent.data = msg.data

def main():
    root = Tk()
    ex = GripperDemo(root)
    root.geometry("650x300+300+300")
    #root.mainloop() # the option is root.update()
    #talker
    try:
        global pub
        pub = rospy.Publisher('gripperCommands', String, queue_size=10)
        rospy.init_node('gripperDemo', anonymous=True)
        rospy.Subscriber("gripperSpeed", UInt16, callSpeed)
        rospy.Subscriber("gripperForce", UInt16, callForce)
        rospy.Subscriber("gripperPosition", Int16, callPosition)
        rospy.Subscriber("gripperDistance", UInt8, callDistance)
        rospy.Subscriber("gripperRotationX", Int16, callRotationX)
        rospy.Subscriber("gripperCurrent", Int16, callCurrent)
        r = rospy.Rate(1/0.1) # 0.5 = 500ms
        #r.sleep()
        while not rospy.is_shutdown():
            ex.updateLabels()
            root.update() #update GUI
            #str = "test%s"
            #rospy.loginfo(str)
            #pub.publish(str)
            r.sleep()
            
    except rospy.ROSInterruptException:
        pass
    ##talker


         


if __name__ == '__main__':
    main()  
