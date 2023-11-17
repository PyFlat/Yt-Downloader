
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
    QSize, Qt)
from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QCheckBox,
    QComboBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy,
    QStackedWidget, QTableWidgetItem, QVBoxLayout, QWidget, QMenuBar, QMenu)

from src.CustomWidgets.CustomTableWidget import CustomTableWidget
from superqt import QLabeledRangeSlider, QLabeledSlider

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1150, 550)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1150, 550))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.topbar = QFrame(self.centralwidget)
        self.topbar.setObjectName(u"topbar")
        self.topbar.setMinimumSize(QSize(0, 50))
        self.topbar.setMaximumSize(QSize(16777215, 50))
        self.topbar.setStyleSheet(u"")
        self.topbar.setFrameShape(QFrame.NoFrame)
        self.topbar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.topbar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.toggle_sidebar_btn = QPushButton(self.topbar)
        self.toggle_sidebar_btn.setObjectName(u"toggle_sidebar_btn")
        self.toggle_sidebar_btn.setMaximumSize(QSize(70, 50))
        icon = QIcon()
        icon.addFile(u"appdata/images/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toggle_sidebar_btn.setIcon(icon)
        self.toggle_sidebar_btn.setIconSize(QSize(45, 45))

        self.horizontalLayout.addWidget(self.toggle_sidebar_btn)

        self.topframe = QFrame(self.topbar)
        self.topframe.setObjectName(u"topframe")
        self.topframe.setFrameShape(QFrame.StyledPanel)
        self.topframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.topframe)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 5, 0, 5)
        self.top_label = QLabel(self.topframe)
        self.top_label.setObjectName(u"top_label")

        self.horizontalLayout_7.addWidget(self.top_label, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.topframe)


        self.verticalLayout.addWidget(self.topbar)

        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setFrameShape(QFrame.NoFrame)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.main_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.sidebar = QFrame(self.main_frame)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setMaximumSize(QSize(70, 16777214))
        self.sidebar.setStyleSheet(u"")
        self.sidebar.setFrameShape(QFrame.NoFrame)
        self.sidebar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.sidebar)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.sb_top_frame = QFrame(self.sidebar)
        self.sb_top_frame.setObjectName(u"sb_top_frame")
        self.sb_top_frame.setFrameShape(QFrame.NoFrame)
        self.sb_top_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.sb_top_frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 25, 0, 0)
        self.search_btn = QPushButton(self.sb_top_frame)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setMinimumSize(QSize(0, 50))
        icon1 = QIcon()
        icon1.addFile(u"appdata/images/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search_btn.setIcon(icon1)
        self.search_btn.setIconSize(QSize(45, 45))
        self.search_btn.setCheckable(True)
        self.search_btn.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.search_btn)

        self.download_btn = QPushButton(self.sb_top_frame)
        self.download_btn.setObjectName(u"download_btn")
        self.download_btn.setEnabled(True)
        self.download_btn.setMinimumSize(QSize(0, 50))
        icon2 = QIcon()
        icon2.addFile(u"appdata/images/download.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u"appdata/images/download-disabled.png", QSize(), QIcon.Disabled, QIcon.Off)
        self.download_btn.setIcon(icon2)
        self.download_btn.setIconSize(QSize(45, 45))
        self.download_btn.setCheckable(True)
        self.download_btn.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.download_btn)

        self.file_btn = QPushButton(self.sb_top_frame)
        self.file_btn.setObjectName(u"file_btn")
        self.file_btn.setMinimumSize(QSize(0, 50))
        icon3 = QIcon()
        icon3.addFile(u"appdata/images/explorer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.file_btn.setIcon(icon3)
        self.file_btn.setIconSize(QSize(45, 45))
        self.file_btn.setCheckable(True)
        self.file_btn.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.file_btn)

        self.settings_btn = QPushButton(self.sb_top_frame)
        self.settings_btn.setObjectName(u"settings_btn")
        self.settings_btn.setMinimumSize(QSize(0, 50))
        icon4 = QIcon()
        icon4.addFile(u"appdata/images/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_btn.setIcon(icon4)
        self.settings_btn.setIconSize(QSize(45, 45))
        self.settings_btn.setCheckable(True)
        self.settings_btn.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.settings_btn)


        self.verticalLayout_3.addWidget(self.sb_top_frame, 0, Qt.AlignTop)

        self.sb_bottom_frame = QFrame(self.sidebar)
        self.sb_bottom_frame.setObjectName(u"sb_bottom_frame")
        self.sb_bottom_frame.setFrameShape(QFrame.NoFrame)
        self.sb_bottom_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.sb_bottom_frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.exit_btn = QPushButton(self.sb_bottom_frame)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setMinimumSize(QSize(70, 50))
        icon5 = QIcon()
        icon5.addFile(u"appdata/images/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_btn.setIcon(icon5)
        self.exit_btn.setIconSize(QSize(45, 45))

        self.verticalLayout_4.addWidget(self.exit_btn)


        self.verticalLayout_3.addWidget(self.sb_bottom_frame, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.sidebar)

        self.frame_5 = QFrame(self.main_frame)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.mainpages = QStackedWidget(self.frame_5)
        self.mainpages.setObjectName(u"mainpages")
        sizePolicy.setHeightForWidth(self.mainpages.sizePolicy().hasHeightForWidth())
        self.mainpages.setSizePolicy(sizePolicy)
        self.mpage1 = QWidget()
        self.mpage1.setObjectName(u"mpage1")
        sizePolicy.setHeightForWidth(self.mpage1.sizePolicy().hasHeightForWidth())
        self.mpage1.setSizePolicy(sizePolicy)
        self.verticalLayout_9 = QVBoxLayout(self.mpage1)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.mpage1)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setVerticalSpacing(25)
        self.gridLayout.setContentsMargins(25, 25, 25, 25)
        self.url_entry = QLineEdit(self.frame)
        self.url_entry.setObjectName(u"url_entry")
        self.url_entry.setEnabled(False)
        self.url_entry.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.url_entry, 0, 0, 1, 1)

        self.search_stack_widg = QStackedWidget(self.frame)
        self.search_stack_widg.setObjectName(u"search_stack_widg")
        sizePolicy.setHeightForWidth(self.search_stack_widg.sizePolicy().hasHeightForWidth())
        self.search_stack_widg.setSizePolicy(sizePolicy)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_10 = QVBoxLayout(self.page)
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.info_start_label = QLabel(self.page)
        self.info_start_label.setObjectName(u"info_start_label")
        self.info_start_label.setAlignment(Qt.AlignCenter)
        self.info_start_label.setWordWrap(False)

        self.verticalLayout_10.addWidget(self.info_start_label, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.search_stack_widg.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        sizePolicy.setHeightForWidth(self.page_2.sizePolicy().hasHeightForWidth())
        self.page_2.setSizePolicy(sizePolicy)
        self.page_2.setMinimumSize(QSize(0, 0))
        self.verticalLayout_12 = QVBoxLayout(self.page_2)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.page_2)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QSize(0, 375))
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 100, 375))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_12.addWidget(self.scrollArea, 0, Qt.AlignTop)

        self.search_stack_widg.addWidget(self.page_2)

        self.gridLayout.addWidget(self.search_stack_widg, 1, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.frame)

        self.mainpages.addWidget(self.mpage1)
        self.mpage2 = QWidget()
        self.mpage2.setObjectName(u"mpage2")
        self.verticalLayout_6 = QVBoxLayout(self.mpage2)
        self.verticalLayout_6.setSpacing(20)
        self.verticalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 0, 10, 0)
        self.download_1 = QFrame(self.mpage2)
        self.download_1.setObjectName(u"download_1")
        self.download_1.setFrameShape(QFrame.StyledPanel)
        self.download_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.download_1)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.image_frame = QFrame(self.download_1)
        self.image_frame.setObjectName(u"image_frame")
        self.image_frame.setMinimumSize(QSize(480, 270))
        self.image_frame.setFrameShape(QFrame.StyledPanel)
        self.image_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.image_frame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 10, 0, 0)
        self.image_label = QLabel(self.image_frame)
        self.image_label.setObjectName(u"image_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.image_label.sizePolicy().hasHeightForWidth())
        self.image_label.setSizePolicy(sizePolicy1)
        self.image_label.setMinimumSize(QSize(480, 270))
        self.image_label.setMaximumSize(QSize(480, 270))
        self.image_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.image_label)


        self.horizontalLayout_4.addWidget(self.image_frame)

        self.label_frame = QFrame(self.download_1)
        self.label_frame.setObjectName(u"label_frame")
        self.label_frame.setFrameShape(QFrame.StyledPanel)
        self.label_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.label_frame)
        self.verticalLayout_2.setSpacing(25)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 9, 0, 0)
        self.name_label = QLabel(self.label_frame)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.name_label)

        self.artist_label = QLabel(self.label_frame)
        self.artist_label.setObjectName(u"artist_label")
        self.artist_label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.artist_label)

        self.date_label = QLabel(self.label_frame)
        self.date_label.setObjectName(u"date_label")

        self.verticalLayout_2.addWidget(self.date_label)

        self.duration_label = QLabel(self.label_frame)
        self.duration_label.setObjectName(u"duration_label")

        self.verticalLayout_2.addWidget(self.duration_label)


        self.horizontalLayout_4.addWidget(self.label_frame, 0, Qt.AlignTop)


        self.verticalLayout_6.addWidget(self.download_1)

        self.download_2 = QStackedWidget(self.mpage2)
        self.download_2.setObjectName(u"download_2")
        self.download_2.setFrameShape(QFrame.StyledPanel)
        self.download_2.setFrameShadow(QFrame.Raised)
        self.download_bar_page1 = QWidget()
        self.download_bar_page1.setObjectName(u"download_bar_page1")
        self.verticalLayout_7 = QVBoxLayout(self.download_bar_page1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.selection_frame = QFrame(self.download_bar_page1)
        self.selection_frame.setObjectName(u"selection_frame")
        self.selection_frame.setFrameShape(QFrame.StyledPanel)
        self.selection_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.selection_frame)
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.format_selection = QComboBox(self.selection_frame)
        self.format_selection.setObjectName(u"format_selection")

        self.horizontalLayout_5.addWidget(self.format_selection)

        self.resolution_selection = QComboBox(self.selection_frame)
        self.resolution_selection.setObjectName(u"resolution_selection")

        self.horizontalLayout_5.addWidget(self.resolution_selection)

        self.change_location_btn = QPushButton(self.selection_frame)
        self.change_location_btn.setObjectName(u"change_location_btn")

        self.horizontalLayout_5.addWidget(self.change_location_btn)

        self.show_folder_btn = QPushButton(self.selection_frame)
        self.show_folder_btn.setObjectName(u"show_folder_btn")

        self.horizontalLayout_5.addWidget(self.show_folder_btn)


        self.verticalLayout_7.addWidget(self.selection_frame)

        self.download_btn_frame = QFrame(self.download_bar_page1)
        self.download_btn_frame.setObjectName(u"download_btn_frame")
        self.download_btn_frame.setFrameShape(QFrame.StyledPanel)
        self.download_btn_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.download_btn_frame)
        self.horizontalLayout_6.setSpacing(25)
        self.horizontalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.last_page_btn = QPushButton(self.download_btn_frame)
        self.last_page_btn.setObjectName(u"last_page_btn")

        self.horizontalLayout_6.addWidget(self.last_page_btn, 0, Qt.AlignLeft)

        self.download_button = QPushButton(self.download_btn_frame)
        self.download_button.setObjectName(u"download_button")

        self.horizontalLayout_6.addWidget(self.download_button)


        self.verticalLayout_7.addWidget(self.download_btn_frame, 0, Qt.AlignHCenter)

        self.download_2.addWidget(self.download_bar_page1)
        self.download_bar_page3 = QWidget()
        self.download_bar_page3.setObjectName(u"download_bar_page3")
        self.verticalLayout_8 = QVBoxLayout(self.download_bar_page3)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.info_range_slider_label = QLabel(self.download_bar_page3)
        self.info_range_slider_label.setObjectName(u"info_range_slider_label")
        self.info_range_slider_label.setMaximumSize(QSize(16777215, 40))
        self.info_range_slider_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.info_range_slider_label)

        self.playlist_range_slider = QLabeledRangeSlider(self.download_bar_page3)
        self.playlist_range_slider.setObjectName(u"playlist_range_slider")
        sizePolicy.setHeightForWidth(self.playlist_range_slider.sizePolicy().hasHeightForWidth())
        self.playlist_range_slider.setSizePolicy(sizePolicy)
        self.playlist_range_slider.setMinimumSize(QSize(0, 20))
        self.playlist_range_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_8.addWidget(self.playlist_range_slider)

        self.next_page_btn = QPushButton(self.download_bar_page3)
        self.next_page_btn.setObjectName(u"next_page_btn")
        self.next_page_btn.setMinimumSize(QSize(150, 0))

        self.verticalLayout_8.addWidget(self.next_page_btn, 0, Qt.AlignHCenter)

        self.download_2.addWidget(self.download_bar_page3)

        self.verticalLayout_6.addWidget(self.download_2)

        self.mainpages.addWidget(self.mpage2)
        self.mpage4 = QWidget()
        self.mpage4.setObjectName(u"mpage4")
        self.verticalLayout_13 = QVBoxLayout(self.mpage4)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(15, 15, 15, 15)
        self.tableWidget = CustomTableWidget(self.mpage4)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QFrame.Sunken)
        self.tableWidget.setLineWidth(0)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditKeyPressed)
        self.tableWidget.setTabKeyNavigation(True)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget.setTextElideMode(Qt.ElideRight)
        self.tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(160)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(0)
        self.tableWidget.verticalHeader().setDefaultSectionSize(39)

        self.verticalLayout_13.addWidget(self.tableWidget)

        self.frame_2 = QFrame(self.mpage4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.download_delete_btn = QPushButton(self.frame_2)
        self.download_delete_btn.setObjectName(u"download_delete_btn")
        self.download_delete_btn.setEnabled(False)

        self.horizontalLayout_8.addWidget(self.download_delete_btn)

        self.download_open_btn = QPushButton(self.frame_2)
        self.download_open_btn.setObjectName(u"download_open_btn")
        self.download_open_btn.setEnabled(False)

        self.horizontalLayout_8.addWidget(self.download_open_btn)

        self.download_download_btn = QPushButton(self.frame_2)
        self.download_download_btn.setObjectName(u"download_download_btn")
        self.download_download_btn.setEnabled(False)

        self.horizontalLayout_8.addWidget(self.download_download_btn)


        self.verticalLayout_13.addWidget(self.frame_2)

        self.mainpages.addWidget(self.mpage4)
        self.mpage3 = QWidget()
        self.mpage3.setObjectName(u"mpage3")
        self.verticalLayout_11 = QVBoxLayout(self.mpage3)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.selection_frame_2 = QFrame(self.mpage3)
        self.selection_frame_2.setObjectName(u"selection_frame_2")
        self.selection_frame_2.setFrameShape(QFrame.StyledPanel)
        self.selection_frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.selection_frame_2)
        self.gridLayout_3.setSpacing(10)
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(10)
        self.gridLayout_3.setVerticalSpacing(25)
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.max_thread_slider = QLabeledSlider(self.selection_frame_2)
        self.max_thread_slider.setObjectName(u"max_thread_slider")
        self.max_thread_slider.setStyleSheet(u"QSlider::groove:horizontal{background: #2A2D43}")
        self.max_thread_slider.setMinimum(1)
        self.max_thread_slider.setMaximum(10)
        self.max_thread_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.max_thread_slider, 1, 2, 1, 2)

        self.change_ffmpeg_path_btn = QPushButton(self.selection_frame_2)
        self.change_ffmpeg_path_btn.setObjectName(u"change_ffmpeg_path_btn")

        self.gridLayout_3.addWidget(self.change_ffmpeg_path_btn, 0, 0, 1, 1)

        self.download_ffmpeg_btn = QPushButton(self.selection_frame_2)
        self.download_ffmpeg_btn.setObjectName(u"download_ffmpeg_btn")

        self.gridLayout_3.addWidget(self.download_ffmpeg_btn, 0, 1, 1, 1)

        self.update_check_box = QCheckBox(self.selection_frame_2)
        self.update_check_box.setObjectName(u"update_check_box")
        self.update_check_box.setTristate(False)

        self.gridLayout_3.addWidget(self.update_check_box, 1, 0, 1, 1)

        self.search_for_update_btn = QPushButton(self.selection_frame_2)
        self.search_for_update_btn.setObjectName(u"search_for_update_btn")

        self.gridLayout_3.addWidget(self.search_for_update_btn, 0, 3, 1, 1)

        self.label = QLabel(self.selection_frame_2)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 1, 1, 1, 1)

        self.update_yt_dlp_btn = QPushButton(self.selection_frame_2)
        self.update_yt_dlp_btn.setObjectName(u"update_yt_dlp_btn")

        self.gridLayout_3.addWidget(self.update_yt_dlp_btn, 0, 2, 1, 1)

        self.thumbnail_check_box = QCheckBox(self.selection_frame_2)
        self.thumbnail_check_box.setObjectName(u"thumbnail_check_box")

        self.gridLayout_3.addWidget(self.thumbnail_check_box, 2, 0, 1, 1)


        self.verticalLayout_11.addWidget(self.selection_frame_2, 0, Qt.AlignTop)

        self.mainpages.addWidget(self.mpage3)

        self.horizontalLayout_3.addWidget(self.mainpages)


        self.horizontalLayout_2.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.main_frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1150, 37))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menuBar)
        QWidget.setTabOrder(self.search_btn, self.url_entry)
        QWidget.setTabOrder(self.url_entry, self.download_btn)
        QWidget.setTabOrder(self.download_btn, self.settings_btn)
        QWidget.setTabOrder(self.settings_btn, self.toggle_sidebar_btn)
        QWidget.setTabOrder(self.toggle_sidebar_btn, self.exit_btn)
        QWidget.setTabOrder(self.exit_btn, self.resolution_selection)
        QWidget.setTabOrder(self.resolution_selection, self.change_location_btn)
        QWidget.setTabOrder(self.change_location_btn, self.show_folder_btn)
        QWidget.setTabOrder(self.show_folder_btn, self.last_page_btn)
        QWidget.setTabOrder(self.last_page_btn, self.download_button)
        QWidget.setTabOrder(self.download_button, self.change_ffmpeg_path_btn)
        QWidget.setTabOrder(self.change_ffmpeg_path_btn, self.download_ffmpeg_btn)
        QWidget.setTabOrder(self.download_ffmpeg_btn, self.update_yt_dlp_btn)
        QWidget.setTabOrder(self.update_yt_dlp_btn, self.format_selection)
        QWidget.setTabOrder(self.format_selection, self.scrollArea)

        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)

        self.mainpages.setCurrentIndex(3)
        self.search_stack_widg.setCurrentIndex(1)
        self.download_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Youtube Downloader v1.3.0", None))
        self.toggle_sidebar_btn.setText("")
        self.top_label.setText("")
        self.search_btn.setText(QCoreApplication.translate("MainWindow", u"  Search", None))
        self.download_btn.setText(QCoreApplication.translate("MainWindow", u"  Download", None))
        self.file_btn.setText(QCoreApplication.translate("MainWindow", u"  Files", None))
        self.settings_btn.setText(QCoreApplication.translate("MainWindow", u"  Settings", None))
        self.exit_btn.setText(QCoreApplication.translate("MainWindow", u"  Exit", None))
        self.url_entry.setText("")
        self.url_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Insert Video or Playlist URL", None))
        self.info_start_label.setText("")
        self.image_label.setText(QCoreApplication.translate("MainWindow", u"Thumbnail", None))
        self.name_label.setText("")
        self.artist_label.setText("")
        self.date_label.setText("")
        self.duration_label.setText("")
        self.change_location_btn.setText(QCoreApplication.translate("MainWindow", u"Change Download Folder", None))
        self.show_folder_btn.setText(QCoreApplication.translate("MainWindow", u"Show Folder in Explorer", None))
        self.last_page_btn.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.download_button.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.info_range_slider_label.setText("")
        self.next_page_btn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Channel", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Video Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Format", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Resolution", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Progress", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"ETA", None));
        self.download_delete_btn.setText(QCoreApplication.translate("MainWindow", u"Delete File", None))
        self.download_open_btn.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.download_download_btn.setText(QCoreApplication.translate("MainWindow", u"Redownload File", None))
        self.change_ffmpeg_path_btn.setText(QCoreApplication.translate("MainWindow", u"Change FFmpeg Path", None))
        self.download_ffmpeg_btn.setText(QCoreApplication.translate("MainWindow", u"Download FFmpeg", None))
        self.update_check_box.setText(QCoreApplication.translate("MainWindow", u"Check For Updates", None))
        self.search_for_update_btn.setText(QCoreApplication.translate("MainWindow", u"Search For Updates", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Set Maximum Threads: ", None))
        self.update_yt_dlp_btn.setText(QCoreApplication.translate("MainWindow", u"Update yt-dlp", None))
        self.thumbnail_check_box.setText(QCoreApplication.translate("MainWindow", u"Show Thumbnails", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

