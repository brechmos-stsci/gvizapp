import logging

from .viewer import Viewer

logging.basicConfig(filename='/tmp/vizapp.log',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)
logger = logging.getLogger('viewernd')


class ViewerND(Viewer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._cube = self._app.load_data('/home/craig/Documents/STScI/cubeviz/data/manga-7495-12704-LOGCUBE_fixed.fits.gz')[0]
        self._v3d = self._app.imshow(data=self._cube)

    def show(self):
        return self._v3d.main_widget
