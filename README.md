# haselmaier.at
## Installation

    cd /path/to/directory
    virtualenv dj_haselmaier
    cd dj_haselmaier/
    source bin/activate
    pip install Django==1.6.2
    git clone https://bitbucket.org/mathiascfrey/haselmaier.at/
 

## Deployment

### Restart

    sudo su -
    touch /etc/uwsgi/apps-enabled/hasel.ini

### Logging

    tail -f /var/log/uwsgi/emperor.log /var/log/nginx/error.log


# Blog: cheat sheet

### Create animation

    convert '*.jpg[400x]' resized%03d.png
    convert -delay 100 -loop 0 resized00*.png animation.gif


### Markdown
    ![alt text](/path/to/file)
    
    *Caption*

### Author images

    convert -size  500x500 wolfgang_haselmaier.jpg -thumbnail 200x200  -bordercolor MintCream -background black -pointsize 12 -density 96x96 +polaroid -resize 70%  -gravity center -background white -extent 340x340 -trim t_wolfgang_haselmaier.jpg