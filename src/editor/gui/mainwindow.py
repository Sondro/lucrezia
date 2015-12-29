# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(549, 1031)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.treeWidget = QtGui.QTreeWidget(self.splitter)
        self.treeWidget.setAnimated(True)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        self.tabWidget = QtGui.QTabWidget(self.splitter)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.texturesTab = QtGui.QWidget()
        self.texturesTab.setObjectName(_fromUtf8("texturesTab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.texturesTab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.texturesFilter = QtGui.QLineEdit(self.texturesTab)
        self.texturesFilter.setObjectName(_fromUtf8("texturesFilter"))
        self.verticalLayout_2.addWidget(self.texturesFilter)
        self.label = QtGui.QLabel(self.texturesTab)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.texturePool = QtGui.QListWidget(self.texturesTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.texturePool.sizePolicy().hasHeightForWidth())
        self.texturePool.setSizePolicy(sizePolicy)
        self.texturePool.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.texturePool.setTabKeyNavigation(False)
        self.texturePool.setTextElideMode(QtCore.Qt.ElideLeft)
        self.texturePool.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.texturePool.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerItem)
        self.texturePool.setResizeMode(QtGui.QListView.Fixed)
        self.texturePool.setViewMode(QtGui.QListView.ListMode)
        self.texturePool.setUniformItemSizes(True)
        self.texturePool.setObjectName(_fromUtf8("texturePool"))
        self.verticalLayout_2.addWidget(self.texturePool)
        self.tabWidget.addTab(self.texturesTab, _fromUtf8(""))
        self.charactersTab = QtGui.QWidget()
        self.charactersTab.setObjectName(_fromUtf8("charactersTab"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.charactersTab)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.characterPool = QtGui.QListWidget(self.charactersTab)
        self.characterPool.setObjectName(_fromUtf8("characterPool"))
        self.verticalLayout_3.addWidget(self.characterPool)
        self.tabWidget.addTab(self.charactersTab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 549, 42))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuWorkspace = QtGui.QMenu(self.menubar)
        self.menuWorkspace.setObjectName(_fromUtf8("menuWorkspace"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        self.menuShaders = QtGui.QMenu(self.menubar)
        self.menuShaders.setObjectName(_fromUtf8("menuShaders"))
        MainWindow.setMenuBar(self.menubar)
        self.actionScene = QtGui.QAction(MainWindow)
        self.actionScene.setObjectName(_fromUtf8("actionScene"))
        self.actionLoad = QtGui.QAction(MainWindow)
        self.actionLoad.setObjectName(_fromUtf8("actionLoad"))
        self.actionNew_2 = QtGui.QAction(MainWindow)
        self.actionNew_2.setObjectName(_fromUtf8("actionNew_2"))
        self.actionSave_Scene = QtGui.QAction(MainWindow)
        self.actionSave_Scene.setObjectName(_fromUtf8("actionSave_Scene"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionRefresh = QtGui.QAction(MainWindow)
        self.actionRefresh.setObjectName(_fromUtf8("actionRefresh"))
        self.actionAdvanced_featues = QtGui.QAction(MainWindow)
        self.actionAdvanced_featues.setObjectName(_fromUtf8("actionAdvanced_featues"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionPPL = QtGui.QAction(MainWindow)
        self.actionPPL.setCheckable(True)
        self.actionPPL.setChecked(False)
        self.actionPPL.setObjectName(_fromUtf8("actionPPL"))
        self.actionToonShading = QtGui.QAction(MainWindow)
        self.actionToonShading.setCheckable(True)
        self.actionToonShading.setObjectName(_fromUtf8("actionToonShading"))
        self.actionAmbientOcclusion = QtGui.QAction(MainWindow)
        self.actionAmbientOcclusion.setCheckable(True)
        self.actionAmbientOcclusion.setObjectName(_fromUtf8("actionAmbientOcclusion"))
        self.menuFile.addAction(self.actionNew_2)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave_Scene)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuWorkspace.addAction(self.actionRefresh)
        self.menuSettings.addAction(self.actionAdvanced_featues)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionAbout)
        self.menuShaders.addAction(self.actionPPL)
        self.menuShaders.addAction(self.actionToonShading)
        self.menuShaders.addAction(self.actionAmbientOcclusion)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuWorkspace.menuAction())
        self.menubar.addAction(self.menuShaders.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "PandaRPG Engine Editor", None))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Tools", None))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "Texturing", None))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "add texture to ground", None))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "clear textures", None))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "Objects", None))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "add object with texture in tile", None))
        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "Lightning", None))
        self.treeWidget.topLevelItem(2).child(0).setText(0, _translate("MainWindow", "add Light", None))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.texturesFilter.setPlaceholderText(_translate("MainWindow", "filter string", None))
        self.label.setText(_translate("MainWindow", "Image preview...", None))
        self.texturePool.setSortingEnabled(True)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.texturesTab), _translate("MainWindow", "Textures", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.charactersTab), _translate("MainWindow", "Characters", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuWorkspace.setTitle(_translate("MainWindow", "Workspace", None))
        self.menuSettings.setTitle(_translate("MainWindow", "?", None))
        self.menuShaders.setTitle(_translate("MainWindow", "Shaders", None))
        self.actionScene.setText(_translate("MainWindow", "Scene", None))
        self.actionLoad.setText(_translate("MainWindow", "Load", None))
        self.actionNew_2.setText(_translate("MainWindow", "New", None))
        self.actionSave_Scene.setText(_translate("MainWindow", "Save", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionRefresh.setText(_translate("MainWindow", "Refresh", None))
        self.actionAdvanced_featues.setText(_translate("MainWindow", "Visit website...", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionPPL.setText(_translate("MainWindow", "PerPixel Lighting", None))
        self.actionToonShading.setText(_translate("MainWindow", "Toon Shading", None))
        self.actionAmbientOcclusion.setText(_translate("MainWindow", "Ambient Occlusion", None))

