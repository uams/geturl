## geturl
### A Share Link Generator. Command Line Tool
 
This tool allows you to get a share link to any file. It uses Filepicker.io as a storage backend. (They have a 5000 file free limit so it shouldn't be a problem)

#### Usage

    >>> geturl path/to/file
    https://www.filepicker.io/api/file/RANDOMSTRING

It also tries to use pbcopy on a mac, xsel or xclip on linux to put the url into your clipboard.


#### Installation

    sudo curl https://raw.github.com/uams/geturl/master/geturl -o /usr/local/bin/geturl
    sudo chmod +x /usr/local/bin/geturl
