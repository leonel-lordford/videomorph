# -*- coding: utf-8 -*-
#
# File name: __init__.py
#
#   VideoMorph - A PyQt5 frontend to ffmpeg and avconv.
#   Copyright 2016-2017 VideoMorph Development Team

#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at

#       http://www.apache.org/licenses/LICENSE-2.0

#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""This module defines the converter package."""

from collections import namedtuple
from os import cpu_count

ConvLib = namedtuple('ConvLib', 'ffmpeg avconv')
CONV_LIB = ConvLib('ffmpeg', 'avconv')


VIDEO_FILTERS = ('*.mov *.f4v *.webm *.dat *.ogg *.mkv *.wv *.wmv'
                ' *.flv *.vob *.ts *.3gp *.ogv *.mpg *.mp4 *.avi')

VALID_VIDEO_EXT = {ext[1:] for ext in VIDEO_FILTERS.split()}

Prober = namedtuple('Prober', 'ffprobe avprobe')
PROBER = Prober('ffprobe', 'avprobe')

MediaFileStatus = namedtuple('MediaFileStatus', 'todo done stopped')
STATUS = MediaFileStatus('To convert', 'Done!', 'Stopped!')


CPU_CORES = (cpu_count() - 1 if
             cpu_count() is not None
             else 0)

PLAYERS = ['vlc',
           'xplayer',
           'totem',
           'kmplayer',
           'smplayer',
           'mplayer',
           'banshee',
           'mpv',
           'gxine',
           'xine-ui',
           'gmlive',
           'dragon',
           'ffplay']
