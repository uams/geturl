## Share Link Generator - A Command Line Tool
#### Using Filepicker.io as storage
 
This tool allows you to get a share link to any file. It uses Filepicker.io as a storage backend. (They have a 5000 file free limit so it shouldn't be a problem)

#### Usage

    >>> filepicker <filename>
    https://www.filepicker.io/api/file/RANDOMSTRING

It also tries to use pbcopy on a mac, xsel or xclip on linux to put the url into your clipboard.


#### Installation

    sudo curl browser://raw.github.com/uams/filepicker-cli/master/filepicker -o /usr/local/bin/filepicker
    sudo chmod +x /usr/local/bin/filepicker

Submitted and under review for Homebrew and Apt-Get Universal
