from ipywidgets import widgets

from ..viewernd import ViewerND
from ..viewer1d import Viewer1D


class CubeViz:

    def __init__(self, filename, vizapp):

        self._vizapp = vizapp

        self._main_box = widgets.VBox()

        self._create_menubar()

        self._v3d = ViewerND(filename, self._vizapp)

        self._main_box.widgets = [self._menu_bar, self._v3d]

    def _create_menubar(self):
        self._menu_bar = widgets.HBox()

        self._menu_bar_file = widgets.Dropdown(
            options=['File', 'Load', 'Save'],
            value='File',
            description='File:',
        )
        self._menu_bar_file.observe(self._on_change_menubar)

    def _on_change_menubar(self, change):
        print(change)

    def show(self):
        return self._main_box
