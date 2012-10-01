## geturl  - provide path. get url.
### A CLI tool to get a public link for any file

Uses [filepicker.io](https://www.filepicker.io) to store the files. It's a cool uploading tool that I've been using on my website and this is a hack on top of it.

#### Use Cases

- You need a quick way to send a file to someone. Instead of attaching it to an email or starting up your FTP server, use this to get a public URL.

- Another tool in your arsenal of `scp`, yousendit, and flash drives for quickly exchanging files.

#### Usage

You provide a path, it returns a URL

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

#### Notes

It uses Filepicker.io as a storage backend. (They have a 5000 file free limit so it shouldn't be a problem)
