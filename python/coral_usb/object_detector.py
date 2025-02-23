from dynamic_reconfigure.server import Server

from coral_usb.cfg import EdgeTPUObjectDetectorConfig
from coral_usb.detector_base import EdgeTPUDetectorBase
from coral_usb.detector_base import EdgeTPUPanoramaDetectorBase


class EdgeTPUObjectDetector(EdgeTPUDetectorBase):
    def __init__(self, namespace='~'):
        super(EdgeTPUObjectDetector, self).__init__(None, None, namespace)

        # dynamic reconfigure
        dyn_namespace = namespace
        if namespace == '~':
            dyn_namespace = ''
        self.srv = Server(
            EdgeTPUObjectDetectorConfig,
            self.config_callback, namespace=dyn_namespace)


class EdgeTPUPanoramaObjectDetector(EdgeTPUPanoramaDetectorBase):
    def __init__(self, namespace='~'):
        super(EdgeTPUPanoramaObjectDetector, self).__init__(
            None, None, namespace)

        # dynamic reconfigure
        dyn_namespace = namespace
        if namespace == '~':
            dyn_namespace = ''
        self.srv = Server(
            EdgeTPUObjectDetectorConfig,
            self.config_callback, namespace=dyn_namespace)
