import os
import shutil
from pathlib import Path
from unittest.mock import patch

os.environ['WHISPER_MODEL'] = 'small'
os.environ['WHISPER_LANGUAGE'] = 'es'
os.environ['WHISPER_DOWNLOAD_ROOT'] = str(Path('bot-happy/models').resolve())
os.environ['WHISPER_LOCAL_FILES_ONLY'] = 'false'
from app.transcription import transcribe_audio

source = Path('.tools/transcription-smoke.wav')
paths = []
def download(media_id, destination, maximum):
    paths.append(destination)
    shutil.copyfile(source, destination)
with patch('app.transcription.download_audio', side_effect=download):
    text = transcribe_audio('synthetic-test')
print('Transcripción local real:', text)
assert 'necesito ayuda' in text.lower(), text
assert all(not path.exists() for path in paths)
print('Audio temporal eliminado correctamente.')

