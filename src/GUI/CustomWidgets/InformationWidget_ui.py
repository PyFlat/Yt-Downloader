# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InformationWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QListWidgetItem,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

from qfluentwidgets import (BodyLabel, CardWidget, HyperlinkLabel, IconWidget,
    LineEdit, ListWidget, PixmapLabel, PrimaryPushButton,
    PushButton, SearchLineEdit, StrongBodyLabel, TitleLabel)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(700, 420)
        Form.setMaximumSize(QSize(16777215, 420))
        Form.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.TitleLabel = TitleLabel(self.widget)
        self.TitleLabel.setObjectName(u"TitleLabel")
        self.TitleLabel.setTextFormat(Qt.RichText)
        self.TitleLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.TitleLabel.setWordWrap(True)

        self.horizontalLayout.addWidget(self.TitleLabel)


        self.verticalLayout.addWidget(self.widget)

        self.widget_4 = QWidget(Form)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.widget_4)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 8, 10, 8)
        self.youtube_icon = IconWidget(self.frame)
        self.youtube_icon.setObjectName(u"youtube_icon")
        self.youtube_icon.setMinimumSize(QSize(25, 25))

        self.horizontalLayout_7.addWidget(self.youtube_icon)

        self.HyperlinkLabel = HyperlinkLabel(self.frame)
        self.HyperlinkLabel.setObjectName(u"HyperlinkLabel")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.HyperlinkLabel.setFont(font)

        self.horizontalLayout_7.addWidget(self.HyperlinkLabel)


        self.horizontalLayout_3.addWidget(self.frame)

        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 8, 10, 8)
        self.author_icon = IconWidget(self.widget_5)
        self.author_icon.setObjectName(u"author_icon")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.author_icon.sizePolicy().hasHeightForWidth())
        self.author_icon.setSizePolicy(sizePolicy)
        self.author_icon.setMinimumSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.author_icon)

        self.StrongBodyLabel_2 = StrongBodyLabel(self.widget_5)
        self.StrongBodyLabel_2.setObjectName(u"StrongBodyLabel_2")

        self.horizontalLayout_4.addWidget(self.StrongBodyLabel_2)


        self.horizontalLayout_3.addWidget(self.widget_5)

        self.widget_7 = QWidget(self.widget_4)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, 8, 10, 8)
        self.duration_icon = IconWidget(self.widget_7)
        self.duration_icon.setObjectName(u"duration_icon")
        sizePolicy.setHeightForWidth(self.duration_icon.sizePolicy().hasHeightForWidth())
        self.duration_icon.setSizePolicy(sizePolicy)
        self.duration_icon.setMinimumSize(QSize(25, 25))

        self.horizontalLayout_5.addWidget(self.duration_icon)

        self.BodyLabel_3 = BodyLabel(self.widget_7)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")

        self.horizontalLayout_5.addWidget(self.BodyLabel_3)


        self.horizontalLayout_3.addWidget(self.widget_7)

        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 8, 10, 8)
        self.calender_icon = IconWidget(self.widget_6)
        self.calender_icon.setObjectName(u"calender_icon")
        sizePolicy.setHeightForWidth(self.calender_icon.sizePolicy().hasHeightForWidth())
        self.calender_icon.setSizePolicy(sizePolicy)
        self.calender_icon.setMinimumSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.calender_icon)

        self.BodyLabel_4 = BodyLabel(self.widget_6)
        self.BodyLabel_4.setObjectName(u"BodyLabel_4")

        self.horizontalLayout_6.addWidget(self.BodyLabel_4)


        self.horizontalLayout_3.addWidget(self.widget_6)


        self.verticalLayout.addWidget(self.widget_4, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.widget_3 = QWidget(Form)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, 0, 15, 0)
        self.widget_8 = QWidget(self.widget_3)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy1)
        self.verticalLayout_4 = QVBoxLayout(self.widget_8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(25, 25, 25, 25)
        self.PixmapLabel_2 = PixmapLabel(self.widget_8)
        self.PixmapLabel_2.setObjectName(u"PixmapLabel_2")
        sizePolicy.setHeightForWidth(self.PixmapLabel_2.sizePolicy().hasHeightForWidth())
        self.PixmapLabel_2.setSizePolicy(sizePolicy)
        self.PixmapLabel_2.setMinimumSize(QSize(400, 225))
        self.PixmapLabel_2.setMaximumSize(QSize(400, 225))
        self.PixmapLabel_2.setStyleSheet(u"")
        self.PixmapLabel_2.setScaledContents(True)
        self.PixmapLabel_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.PixmapLabel_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)


        self.horizontalLayout_2.addWidget(self.widget_8)

        self.stackedWidget = QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_8 = QHBoxLayout(self.page)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.page)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 35, 0, 0)
        self.best_video_btn = PushButton(self.widget_2)
        self.best_video_btn.setObjectName(u"best_video_btn")
        self.best_video_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.best_video_btn, 0, Qt.AlignLeft)

        self.best_audio_btn = PushButton(self.widget_2)
        self.best_audio_btn.setObjectName(u"best_audio_btn")
        self.best_audio_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.best_audio_btn, 0, Qt.AlignLeft)

        self.quick_dl_btn = PushButton(self.widget_2)
        self.quick_dl_btn.setObjectName(u"quick_dl_btn")
        self.quick_dl_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.quick_dl_btn, 0, Qt.AlignLeft)

        self.custom_dl_btn = PushButton(self.widget_2)
        self.custom_dl_btn.setObjectName(u"custom_dl_btn")
        self.custom_dl_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.custom_dl_btn, 0, Qt.AlignLeft)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout_8.addWidget(self.widget_2)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_3 = QVBoxLayout(self.page_2)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 25, 0, 25)
        self.SearchLineEdit = SearchLineEdit(self.page_2)
        self.SearchLineEdit.setObjectName(u"SearchLineEdit")

        self.verticalLayout_3.addWidget(self.SearchLineEdit)

        self.ListWidget = ListWidget(self.page_2)
        self.ListWidget.setObjectName(u"ListWidget")
        self.ListWidget.setMaximumSize(QSize(16777215, 125))

        self.verticalLayout_3.addWidget(self.ListWidget)

        self.widget_9 = QWidget(self.page_2)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_9.setSpacing(15)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.PushButton = PushButton(self.widget_9)
        self.PushButton.setObjectName(u"PushButton")

        self.horizontalLayout_9.addWidget(self.PushButton, 0, Qt.AlignTop)

        self.PrimaryPushButton_4 = PrimaryPushButton(self.widget_9)
        self.PrimaryPushButton_4.setObjectName(u"PrimaryPushButton_4")

        self.horizontalLayout_9.addWidget(self.PrimaryPushButton_4, 0, Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.widget_9)

        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.widget_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("Form", u"Paris Saint-Germain - Borussia Dortmund | UEFA Champions League 2023/24, Halbfinale | sportstudio", None))
        self.HyperlinkLabel.setText(QCoreApplication.translate("Form", u"YouTube Video", None))
        self.StrongBodyLabel_2.setText(QCoreApplication.translate("Form", u"by sportstudio fu\u00dfball", None))
        self.BodyLabel_3.setText(QCoreApplication.translate("Form", u"05 minutes, 05 seconds", None))
        self.BodyLabel_4.setText(QCoreApplication.translate("Form", u"09.05.2024", None))
        self.best_video_btn.setText(QCoreApplication.translate("Form", u"Best Video", None))
        self.best_audio_btn.setText(QCoreApplication.translate("Form", u"Best Audio", None))
        self.quick_dl_btn.setText(QCoreApplication.translate("Form", u"Quick Download", None))
        self.custom_dl_btn.setText(QCoreApplication.translate("Form", u"Custom", None))
        self.SearchLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Select your format", None))
        self.PushButton.setText(QCoreApplication.translate("Form", u"Back", None))
        self.PrimaryPushButton_4.setText(QCoreApplication.translate("Form", u"Download", None))
    # retranslateUi

