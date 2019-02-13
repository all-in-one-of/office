# coding: utf-8

"""
`CGF Help > Publisher <>`_

------------

* временное расположение модуля:  **pipeline/python_libs**;
* self.page_top - спойлер родительского toolbox в родительском main_widget_ui;
* self.top_gridLayout - сетка в self.page_top

"""
from qt_import import *
from cgflib import paths
from string import zfill

from main_widget_ui import Ui_Dialog
from paths_widget_ui import Ui_PathWidget
from publish_widget_ui import Ui_publish_data
from task_widget_ui import Ui_task_data
from variant_widget_ui import Ui_variants_widget


class VariantWidget(QWidget, Ui_variants_widget):
    def __init__(self, asset_vars):
        super(VariantWidget, self).__init__()
        self.setupUi(self)
        self.asset_vars = asset_vars
        self.variant_list = self.asset_vars.keys()

        w = 70
        self.variant_lb.setFixedWidth(w)
        self.count_lb.setFixedWidth(w)
        self.variant_cbx.setMinimumWidth(w + 80)
        self.count_cbx.setMinimumWidth(w + 80)

        self.fill_variants()

        # connects
        self.variant_cbx.currentIndexChanged.connect(self.fill_count)

    def fill_variants(self):
        self.variant_cbx.clear()

        for i, variant in enumerate(self.variant_list):
            self.variant_cbx.addItem("")
            self.variant_cbx.setItemText(i, variant)

        self.fill_count()

    def fill_count(self):
        self.count_cbx.clear()
        variant = self.variant_cbx.currentText()
        count = self.asset_vars[variant][0]
        name = zfill(str(count), 2)
        name = 'Count : %s' % name
        self.count_lb.setText(name)

        if count:
            for i in range(0, count):
                self.count_cbx.addItem("")
                self.count_cbx.setItemText(i, str(i + 1))
        elif count == 0:
            self.count_cbx.addItem("")
            self.count_cbx.setItemText(0, str(0))


class PathsWidget(QWidget, Ui_PathWidget):
    """
    заполняет поля Paths Widget путями открытой сцены и выбранной ноды
    """
    def __init__(self):
        super(PathsWidget, self).__init__()
        self.setupUi(self)

        self.get_paths()

    def get_paths(self):
        scene_path = None
        node_path = None

        if soft_name == 'maya':
            # from pymel.core import sceneName, selected

            scene_path = sceneName()
            sel = selected()

            if sel:
                node_path = sel[0].name(long=True)

        if soft_name == 'houdini':
            scene_path = hou.hipFile.path()
            sel = hou.selectedNodes()

            if sel:
                node_path = ', '.join([n.path() for n in sel])

        if scene_path:
            self.scene_le.setText(scene_path)
        if node_path:
            self.node_le.setText(node_path)

        self.scene_le.setReadOnly(True)
        self.node_le.setReadOnly(True)


class PublishWidget(QWidget, Ui_publish_data):
    """
    заполняет поля Publish Widget значениями принятого ID Publish Event;
    например publish_event_id из ответа паблиш-сервера
    """
    def __init__(self, pub_id):
        super(PublishWidget, self).__init__()
        self.setupUi(self)

        self.fill_fields(pub_id)

    def fill_fields(self, pub_id=None):

        from cgflib import shotgun

        filters = [['id', 'is', pub_id]]
        fields = ['code', 'sg_version', 'sg_group_id', 'sg_linked_version']
        result = shotgun._SG.find_one('PublishEvent', filters, fields)

        if result:
            name = result['code']
            ver = result['sg_version']
            group_id = result['sg_group_id']
            ver_link = result['sg_linked_version']

            self.name_le.setText(name)
            self.ver_le.setText(str(ver))
            self.groupid_le.setText(str(group_id))
            self.verlink_le.setText(str(ver_link))

        self.name_le.setReadOnly(True)
        self.ver_le.setReadOnly(True)
        self.groupid_le.setReadOnly(True)
        self.verlink_le.setReadOnly(True)


class TaskWidget(QWidget, Ui_task_data):
    """
    заполняет поля Task Widget значениями текущего таска
    """
    def __init__(self):
        super(TaskWidget, self).__init__()
        self.setupUi(self)

        self.project = os.path.basename(os.getenv('FILM'))
        self.artist = os.getenv('USER')
        self.entity = None
        self.asset = None
        self.contype = None
        self.task_name = None

        self.fill_fields()

    def fill_fields(self):
        self.get_task_data()

        if self.contype == 'Asset':
            self.asset_lb.setText("Base asset")
            self.asset_le.setText(self.asset)  # Base asset
        else:
            self.asset_lb.setText("***")

        self.entity_lb.setText("Entity")
        self.project_lb.setText("Project")
        self.task_lb.setText("Task")
        self.contype_lb.setText("Content type")
        self.artist_lb.setText("Artist")

        self.entity_le.setText(self.entity)  # Entity
        self.task_le.setText(self.task_name)  # Task
        self.contype_le.setText(self.contype)  # Content type
        self.artist_le.setText(self.artist)  # Artist

        self.entity_le.setReadOnly(True)
        self.asset_le.setReadOnly(True)
        self.task_le.setReadOnly(True)
        self.contype_le.setReadOnly(True)
        self.artist_le.setReadOnly(True)

    def get_task_data(self):
        all_projects = paths.allProjects()
        self.fill_ProjectCbx(sorted(all_projects))

        task_id = int(os.getenv('SG_TASK_ID'))
        task_data = paths.get_task_data(task_id)
        task_dict = task_data.sg_task
        entity_obj = task_data.sg_entity

        if entity_obj.type == 'Asset':
            variant = entity_obj.sg_asset_variant
        else:
            variant = None

        self.entity = entity_obj.name
        self.asset = self.entity
        self.contype = entity_obj.type
        self.task_name = task_dict.content

        if variant:
            self.asset = variant['name']

    def fill_ProjectCbx(self, all_projects):
        self.project_cbx.clear()

        for i, project in enumerate(all_projects):
            self.project_cbx.addItem("")
            self.project_cbx.setItemText(i, project)

            # запрет выбора остальных
            if project != self.project:
                self.project_cbx.model().item(i).setEnabled(False)

        try:
            self.project_cbx.setCurrentText(self.project)
        except AttributeError:
            ind = all_projects.index(self.project)
            self.project_cbx.setCurrentIndex(ind)


class MainWidget(QDialog, Ui_Dialog):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.setupUi(self)

        # виджеты для top-page
        self.task_widget = TaskWidget()
        self.paths_widget = PathsWidget()
        # self.publish_widget = PublishWidget()
        self.variant_widget = None

        # добавление виджетов
        self.insertTaskWidget()
        self.insertPathsWidget()
        self.insertVariantWidget()
        # self.insertPublishWidget()

        # замена в QDialogButtonBox кнопки OK на Publish
        self.buttonBox.removeButton(self.buttonBox.button(QDialogButtonBox.Ok))
        self.publish_button = self.buttonBox.addButton("Publish", QDialogButtonBox.ActionRole)

        self.add_style()

        # connect
        # self.buttonBox.accepted.connect(self.do_publish)
        self.publish_button.clicked.connect(self.do_publish)
        # self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.close_win)

    def close_win(self):
        print '= CLOSE ='
        # w.close()

    def add_style(self):
        """ добавление стилей """

        css = """

        QToolBox:tab {
            /* background: #009deb;
            border-radius: 5px; */
            color: black;
        }


        QToolBox::tab:first {
            background: #b3b300;
            /* border-radius: 5px; 
            color: black; */
        }

        QToolBox::tab:last {
            background: #ff9900;
            /* border-radius: 5px;
            color: black; */
        }

        QToolBox::tab:selected { /* italicize selected tabs */
            font: italic;
            /* color: white; */
        }

        """
        self.setStyleSheet(css)

    def insertVariantWidget(self):
        if os.getenv('SG_ENTITY_TYPE') == 'asset':
            asset_vars = paths.get_asset_variants()

            if asset_vars:
                self.insertLine('bottom', 1)

                self.variant_widget = VariantWidget(asset_vars)
                self.gridLayout_bottom.addWidget(self.variant_widget, 2, 0, 1, 1)
                self.toolBox.setItemText(self.toolBox.indexOf(self.page_bottom), "Input Description / Select Variant")


    def insertTaskWidget(self):
        self.gridLayout_top.addWidget(self.task_widget, 0, 0, 1, 1)

    def insertLine(self, place, number):
        self.line = QFrame(self.page_top)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")

        if place == 'top':
            self.gridLayout_top.addWidget(self.line, number, 0, 1, 1)
            self.resize_window(100)

        if place == 'bottom':
            self.gridLayout_bottom.addWidget(self.line, number, 0, 1, 1)

    def insertPathsWidget(self):
        self.insertLine('top', 1)

        self.gridLayout_top.addWidget(self.paths_widget, 3, 0, 1, 1)
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_top), "Task information + Scene / Node paths")

    def insertPublishWidget(self):
        self.insertLine('bottom', 3)

        self.publish_widget = PublishWidget(74299)
        self.gridLayout_bottom.addWidget(self.publish_widget, 4, 0, 1, 1)

        self.resize_window(68)

    def do_publish(self):
        self.insertPublishWidget()

        self.toolBox.setCurrentIndex(1)
        w.show()

    def resize_window(self, increment):
        h = self.dialog.height()
        h += increment
        self.dialog.resize(700, h)
        self.dialog.setMinimumSize(600, h)

global w

w = MainWidget()
w.show()

