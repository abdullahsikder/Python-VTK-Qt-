#!/usr/bin/env python

import sys
import vtk
from PySide2 import QtGui, QtWidgets
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor 


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        
        self.frame = QtWidgets.QFrame()

        self.vl = QtWidgets.QVBoxLayout()
        self.vtkWidget = QVTKRenderWindowInteractor(self.frame)
        self.vl.addWidget(self.vtkWidget)

        self.ren = vtk.vtkRenderer()
        self.vtkWidget.GetRenderWindow().AddRenderer(self.ren)
        self.iren = self.vtkWidget.GetRenderWindow().GetInteractor()

        # Create source
        source = vtk.vtkSphereSource()
        source.SetCenter(0, 0, 0)
        source.SetRadius(5.0)

        #reader = vtk.vtkPLYReader()
        reader = vtk.vtkXMLImageDataReader()
        reader.SetFileName(path10 + filename)
        opacityTransferFunction = vtk.vtkPiecewiseFunction()
        opacityTransferFunction.AddPoint(2440, 0.0)
        opacityTransferFunction.AddPoint(2550, 0.8)
        # Create a mapper
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(reader.GetOutputPort())

        volumeMapper = vtk.vtkSmartVolumeMapper()
        volumeMapper.SetInputConnection(reader.GetOutputPort())
        # Create an actor
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        volume = vtk.vtkVolume()
        volume.SetMapper(volumeMapper)
        volumeProperty = vtk.vtkVolumeProperty()
        volumeProperty.SetScalarOpacity(opacityTransferFunction)
        volume.SetProperty(volumeProperty)

        self.ren.AddActor(volume)

        self.ren.ResetCamera()

        self.frame.setLayout(self.vl)
        self.setCentralWidget(self.frame)

        self.show()
        self.iren.Initialize()


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()

    sys.exit(app.exec_())
