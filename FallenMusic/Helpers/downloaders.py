# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
from yt_dlp import YoutubeDL
from pyrogram.errors import BadRequest

# Initialize with default options
ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": "downloads/%(id)s.%(ext)s",
    "geo_bypass": True,
    "nocheckcertificate": True,
    "quiet": True,
    "no_warnings": True,
    "prefer_ffmpeg": True,
    "cookiefile": "cookies.txt",  # Add cookie support
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "320",
        }
    ],
}

def audio_dl(url: str) -> str:
    try:
        # Check if cookies file exists
        if not os.path.exists("cookies.txt"):
            ydl_opts.pop("cookiefile", None)  # Remove cookiefile if no cookies
        
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            x_file = os.path.join("downloads", f"{info['id']}.mp3")
            
            if os.path.exists(x_file):
                return x_file
                
            # Download if file doesn't exist
            ydl.download([url])
            return x_file
            
    except Exception as e:
        error_message = f"Failed to download audio: {str(e)}"
        if "Sign in to confirm you're not a bot" in str(e):
            error_message += "\n\n⚠️ YouTube is blocking requests. Please update cookies.txt with fresh YouTube cookies."
        raise BadRequest(error_message)
