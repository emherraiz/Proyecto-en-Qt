from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFormLayout, QWidget, QLabel,
    QRadioButton, QCheckBox, QLineEdit, QSpinBox, QDoubleSpinBox,
    QPushButton, QComboBox, QFontComboBox, QDateEdit, QDateTimeEdit,
    QLCDNumber, QProgressBar, QDial, QSlider, QGridLayout, QStyle)
from PySide6.QtCore import Qt
from pathlib import Path
import sys
import qtawesome as qta

iconos = ['SP_ArrowBack', 'SP_ArrowDown', 'SP_ArrowForward', 
'SP_ArrowLeft', 'SP_ArrowRight', 'SP_ArrowUp', 'SP_BrowserReload', 
'SP_BrowserStop', 'SP_CommandLink', 'SP_ComputerIcon', 
'SP_CustomBase', 'SP_DesktopIcon', 'SP_DialogApplyButton', 
'SP_DialogCancelButton', 'SP_DialogCloseButton', 
'SP_DialogDiscardButton', 'SP_DialogHelpButton', 'SP_DialogNoButton', 
'SP_DialogOkButton', 'SP_DialogOpenButton', 'SP_DialogResetButton', 
'SP_DialogSaveButton', 'SP_DialogYesButton', 'SP_DirClosedIcon', 
'SP_DirHomeIcon', 'SP_DirIcon', 'SP_DirLinkIcon', 'SP_DirOpenIcon', 
'SP_DockWidgetCloseButton', 'SP_DriveCDIcon', 'SP_DriveDVDIcon', 
'SP_DriveFDIcon', 'SP_DriveHDIcon', 'SP_DriveNetIcon', 
'SP_FileDialogBack', 'SP_FileDialogContentsView', 
'SP_FileDialogDetailedView', 'SP_FileDialogEnd', 
'SP_FileDialogInfoView', 'SP_FileDialogListView', 
'SP_FileDialogNewFolder', 'SP_FileDialogStart', 
'SP_FileDialogToParent', 'SP_FileIcon', 'SP_FileLinkIcon', 
'SP_MediaPause', 'SP_MediaPlay', 'SP_MediaSeekBackward', 
'SP_MediaSeekForward', 'SP_MediaSkipBackward', 'SP_MediaSkipForward', 
'SP_MediaStop', 'SP_MediaVolume', 'SP_MediaVolumeMuted', 
'SP_MessageBoxCritical', 'SP_MessageBoxInformation', 
'SP_MessageBoxQuestion', 'SP_MessageBoxWarning', 
'SP_TitleBarCloseButton', 'SP_TitleBarContextHelpButton', 
'SP_TitleBarMaxButton', 'SP_TitleBarMenuButton', 
'SP_TitleBarMinButton', 'SP_TitleBarNormalButton', 
'SP_TitleBarShadeButton', 'SP_TitleBarUnshadeButton', 
'SP_ToolBarHorizontalExtensionButton', 
'SP_ToolBarVerticalExtensionButton', 'SP_TrashIcon', 'SP_VistaShield']


def absPath(file):
    return str(Path(__file__).parent.absolute() / file)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # creo un layaout en cuadrícula
        layout = QGridLayout()

        # recorro los iconos con un contador de posicion
        for contador, nombre in enumerate(iconos):
            # recupero el icono a partir de su nombre
            icono = self.style().standardIcon(getattr(QStyle, nombre))
            # creo un botón con el icono y su nombre del icono
            boton = QPushButton(icono, nombre)
            # añado el boton en una cuadrícula de 5 columnas
            # divido el contador entre 5 para conseguir la fila
            # con el módulo de la divisón entre 5 conseguiré la columna
            layout.addWidget(boton, contador // 5, contador % 5)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


        widget = QWidget()

        self.cargarQSS("qss/ElegantDark.qss")
        self.cargarQSS("qss/ChatBee.qss")
        self.cargarQSS("qss/EasyCode.qss")


    def cargarQSS(self, file):
        # guardamos la ruta absoluta al fichero
        path = absPath(file)
        # intentamos abrirlo y volcar el contenido
        try:
            with open(path) as styles:
                self.setStyleSheet(styles.read())
        # si hay algún fallo lo capturamos con una excepción genérica
        except:
            print("Error abriendo estilos", path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
