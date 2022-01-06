# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'channel_display_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChannelDiplay(object):
    def setupUi(self, ChannelDiplay):
        ChannelDiplay.setObjectName("ChannelDiplay")
        ChannelDiplay.resize(559, 64)
        ChannelDiplay.setMinimumSize(QtCore.QSize(40, 30))
        self.verticalLayout = QtWidgets.QVBoxLayout(ChannelDiplay)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.color_btn = QtWidgets.QPushButton(ChannelDiplay)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.color_btn.sizePolicy().hasHeightForWidth())
        self.color_btn.setSizePolicy(sizePolicy)
        self.color_btn.setMinimumSize(QtCore.QSize(16, 16))
        self.color_btn.setMaximumSize(QtCore.QSize(16, 16))
        self.color_btn.setAutoFillBackground(False)
        self.color_btn.setText("")
        self.color_btn.setFlat(False)
        self.color_btn.setObjectName("color_btn")
        self.horizontalLayout.addWidget(self.color_btn)
        self.range_indicator = QtWidgets.QLabel(ChannelDiplay)
        self.range_indicator.setMinimumSize(QtCore.QSize(16, 16))
        self.range_indicator.setMaximumSize(QtCore.QSize(16, 16))
        self.range_indicator.setText("")
        self.range_indicator.setPixmap(QtGui.QPixmap(":/paint.png"))
        self.range_indicator.setScaledContents(True)
        self.range_indicator.setObjectName("range_indicator")
        self.horizontalLayout.addWidget(self.range_indicator)
        self.name = QtWidgets.QLabel(ChannelDiplay)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy)
        self.name.setMinimumSize(QtCore.QSize(0, 24))
        self.name.setMouseTracking(False)
        self.name.setTextFormat(QtCore.Qt.PlainText)
        self.name.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.name.setObjectName("name")
        self.horizontalLayout.addWidget(self.name)
        self.value = QtWidgets.QLabel(ChannelDiplay)
        self.value.setMinimumSize(QtCore.QSize(75, 0))
        self.value.setText("")
        self.value.setTextFormat(QtCore.Qt.PlainText)
        self.value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.value.setObjectName("value")
        self.horizontalLayout.addWidget(self.value)
        self.ylink = QtWidgets.QCheckBox(ChannelDiplay)
        self.ylink.setText("")
        self.ylink.setObjectName("ylink")
        self.horizontalLayout.addWidget(self.ylink)
        self.individual_axis = QtWidgets.QCheckBox(ChannelDiplay)
        self.individual_axis.setText("")
        self.individual_axis.setObjectName("individual_axis")
        self.horizontalLayout.addWidget(self.individual_axis)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.details = QtWidgets.QLabel(ChannelDiplay)
        self.details.setObjectName("details")
        self.verticalLayout.addWidget(self.details)

        self.retranslateUi(ChannelDiplay)

    def retranslateUi(self, ChannelDiplay):
        _translate = QtCore.QCoreApplication.translate
        ChannelDiplay.setWindowTitle(_translate("ChannelDiplay", "Form"))
        self.name.setText(_translate("ChannelDiplay", "MAIN CLOCK"))
        self.ylink.setToolTip(_translate("ChannelDiplay", "enable common Y axis"))
        self.details.setText(_translate("ChannelDiplay", "details"))
from . import resource_rc
