# YT34

A simple YouTube downloader that just works.

![very basic ui with a box to input url, box to input download directory, and two download options mp3 and mp4](https://github.com/TrinhChiLan/yt34/blob/2a256a288b635291d7d68bfbc5b6ff11751c4267/preview.png)

## What is this?

YT34 is a GUI wrapper for yt-dlp. It does one thing: getting a video or audio file from YouTube onto your computer.

No codec menus. No quality selectors. No format codes. Just mp3 or mp4.

## Why?

Because I wanted to build an yt-dlp wrapper that is completely braindead to use.

If you need advanced options, you should check out the command-line version of yt-dlp or other wrappers. But if you just want to download something quickly without thinking about it, that's what this is for.

## Features

- Download from YouTube as MP4
- Download from YouTube as MP3
- Choose your download location
- That's it

## Installation

YT34 comes bundled with everything it needs, including ffmpeg binaries. 

1. Download the latest release
2. Run the executable
3. You're done

## Usage

1. Paste a YouTube URL
2. Choose mp3 (audio) or mp4 (video)
3. Select where to save it
4. Click Download

## Requirements

None. Everything is bundled.


## Credits

Built with:
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Does the actual downloading
- [FFmpeg](https://ffmpeg.org/) - Handles audio/video processing
- Python's Tkinter - For the interface

## Note

This is just a simple tool I made because I wanted something straightforward. If it helps you too, that's great. If you need more features, there are plenty of other excellent yt-dlp frontends out there with more options.

If you have already installed ffpmeg and included it in your system PATH, feel free to delete the bundled ffmpeg folder, it takes up so much damn space.
