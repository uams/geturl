## geturl
### A Share Link Generator. Command Line Tool
 
This tool allows you to get a share link to any file. It uses Filepicker.io as a storage backend. (They have a 5000 file free limit so it shouldn't be a problem)

#### Usage

    geturl path/to/file

It also tries to use `pbcopy` on a mac, `xsel` or `xclip` on Linux to put the url into your clipboard.

<img src="https://raw.github.com/uams/geturl/master/static/example.png">

#### Installation

    sudo curl https://raw.github.com/uams/geturl/master/geturl -o /usr/local/bin/geturl;
    sudo chmod +x /usr/local/bin/geturl

Enable Clipboard Access (Only necessary on Linux)

    sudo apt-get install xclip

I'll submit it to `brew` and `apt-get` if enough people are interested.

<img src="https://raw.github.com/uams/geturl/master/static/install.png">
