"""libsoundtouch."""

try:
    from queue import Queue, Empty
except ImportError:
    from Queue import Queue, Empty  # type: ignore
from zeroconf import Zeroconf, ServiceBrowser
from .device import SoundTouchDevice
from .utils import SoundtouchDeviceListener
import logging


class SoundTouchSearcher:
    """ Class to find sound touch devices in your network
    """

    def __init__(self):
        """ Initialize SoundTouchSearcher
        """
        pass

    def _createSoundTouchDevice(host, port=8090):
        """Create a new Soundtouch device.

        :param host: Host of the device
        :param port: Port of the device. Default 8090

        """
        return SoundTouchDevice(host, port)

    def searchSoundTouchDevices(timeout=5):
        """Discover devices on the local network.

        :param timeout: Max time to wait in seconds. Default 5
        """
        _devices = []
        # Using Queue as a timeout timer
        _devicesQueue = Queue()

        def _appendSoundTouchDevice(name, host, port):
            """Add device callback."""
            logging.info("%s discovered (host: %s, port: %i)", name, host, port)
            _devices.append(SoundTouchSearcher._createSoundTouchDevice(host, port))

        _zeroconf = Zeroconf()
        _listener = SoundtouchDeviceListener(_appendSoundTouchDevice)
        logging.info("Starting discovery...")
        ServiceBrowser(_zeroconf, "_soundtouch._tcp.local.", _listener)
        try:
            _devicesQueue.get(timeout=timeout)
        except Empty:
            logging.info("End of discovery...")
        return _devices
