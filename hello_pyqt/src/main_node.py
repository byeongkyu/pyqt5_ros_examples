#!/usr/bin/env python3
#-*- encoding: utf8 -*-

import sys
import os
import rospkg
import rospy
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic

from std_msgs.msg import String

class HelloPyQt5Widget(QtWidgets.QWidget):
    def __init__(self):
        super(HelloPyQt5Widget, self).__init__()

        # ROS
        self.pub_test = rospy.Publisher('test_hello', String, queue_size=10)
        rospy.Subscriber('sub_hello', String, self.handle_sub_hello)

        # Load UI
        ui_file = os.path.join(rospkg.RosPack().get_path('hello_pyqt'), 'resource', 'hello_pyqt.ui')
        uic.loadUi(ui_file, self)

        self.buttonTestPub.clicked.connect(self.handle_clicked_button)


    def handle_clicked_button(self):
        msg = String()
        msg.data = "Hello PyQt5"
        self.pub_test.publish(msg)

    def handle_sub_hello(self, msg):
        self.textSub.setText(msg.data)



if __name__ == '__main__':
    rospy.init_node('hello_pyqt_node', anonymous=False)

    app = QtWidgets.QApplication(sys.argv)
    window = HelloPyQt5Widget()
    window.showFullScreen()
    sys.exit(app.exec_())