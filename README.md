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


