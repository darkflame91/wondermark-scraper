# wondermark-scraper
Downloads all the comic images from Wondermark [wondermark.com] for offline reading

This script has not been under version control(till now!)

This script requires the requests and BeautifulSoup python libraries.

This can be read as is, but I prefer rar'ing them, changing the extension to .cbr, and reading them on a comic book reader.

Unlike the other webcomic scrapers I've written, this webcomic has an odd and non-sequential way of naming image files. However, the page links are sequential. For this reason, I've used BeautifulSoup to parse the entire webpage of each comic, extract the link to the comic image and store it. This might be a little slower than the other ones.

TODO:
- Store images in folders in groups of 100's or 1000's
- Try finding a way to convert to cbr programmatically
