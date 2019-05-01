import logging

from .simple_bqplot_profile import simple_profile
from .viewer import Viewer

logging.basicConfig(filename='/tmp/vizapp.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
logger = logging.getLogger('viewer1d')


class Viewer1D(Viewer):

    def __init__(self, filename, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._cube = self._app.load_data(filename)[0]
        self._v1d = simple_profile(self._app, data=self._cube)

    def show(self):
        return self._v1d

    def show_widget(self):
        return self._v1d.main_widget
