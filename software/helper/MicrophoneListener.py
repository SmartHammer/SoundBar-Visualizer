# This Python file uses the following encoding: utf-8
import pyaudio
import wave
import logging
from pydub import AudioSegment
from helper.singletondecorator import singleton


class MicrophoneListenerException(Exception):
    """Parent MicrophoneListener Exception."""

    def __init__(self):
        """MicrophoneListener Exception."""
        super(MicrophoneListenerException, self).__init__()


@singleton
class MicrophoneListener:
    def __init__(self, format=pyaudio.paInt16, channels=1, rate=44100):
        self._format = format
        self._channels = channels
        self._rate = rate
        self._pyAudio = pyaudio.PyAudio()
        self._sampleWidth = self._pyAudio.get_sample_size(self._format)
        self._inputDeviceIndex = self._findMicrophone()
        if not self._inputDeviceIndex:
            raise MicrophoneListenerException()

    def __del__(self):
        self._pyAudio.terminate()

    def _findMicrophone(self):
        _index = None
        for i in range(self._pyAudio.get_device_count()):
            _device_info = self._pyAudio.get_device_info_by_index(i)
            for _keyword in ['mic', 'input', 'usb audio device']:
                if _keyword in _device_info['name'].lower():
                    _index = i
                    return _index
        return _index

    def record(self, duration: int = 2) -> bytes:
        _frames: bytes = bytes()
        _chunk = self._rate * self._channels * duration * self._sampleWidth
        _stream: pyaudio.Stream = None
        try:
            _stream = self._pyAudio.open(format=self._format,
                                         channels=self._channels,
                                         rate=self._rate,
                                         input=True,
                                         input_device_index=self._inputDeviceIndex,
                                         frames_per_buffer=_chunk)
            _frames = _stream.read(_chunk, exception_on_overflow=False)
        except (Exception) as exception:
            logging.error(exception)
            logging.info(self._pyAudio.get_device_info_by_index(self._inputDeviceIndex))
        finally:
            if _stream is not None:
                _stream.stop_stream()
                _stream.close()
            return _frames

    def convertMonoToWav(self, path: str, data: bytes) -> bool:
        assert(path.endswith(".wav"))
        result: bool = len(data) > 0
        if result:
            with wave.open(path, 'wb') as wf:
                wf.setnchannels(1)
                wf.setsampwidth(self._sampleWidth)
                wf.setframerate(self._rate)
                wf.writeframes(data)
        return result

    def convertMonoToMp3(self, path: str, data: bytes) -> bool:
        assert(path.endswith(".mp3"))
        _path: str = path + ".wav"
        result: bool = self.convertMonoToWav(_path, data)
        if result:
            _sound = AudioSegment.from_wav(_path)
            _sound.export(path, format="mp3")
        return result

    def recordMonoToMp3(self, path: str, duration: int = 2) -> bool:
        _frames = self.record(duration)
        return self.convertMonoToMp3(path, _frames)
