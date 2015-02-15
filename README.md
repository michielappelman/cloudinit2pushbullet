cloudinit2pushbullet
====================

Listen on a certain port and wait for a virtual machine to 'phone home' after
completing a cloudinit configuration. This script will then log that activity
and send out a pushbullet notification using the API key in 'apikey.txt'.

Make sure a valid pushbullet API is present in 'apikey.txt'.

Additionally, I'm running this in an nginx configuration with a proxy to the 
specified port like so:

    server {
        listen   80;
        listen   [::]:80;
    
        server_name <PHONE HOME DOMAIN>;
    
        location / {
            proxy_pass http://127.0.0.1:5100;
        }
    }

Obviously the best thing would be to run it as an uWSGI application or something
but that is something I still have to figure out.
