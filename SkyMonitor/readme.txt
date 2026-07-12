Virtual Machine was set up as ubuntu server 26.04 with 4GB RAM allocated.
nginx and gunicorn was installed xfce4 and lightdm for ease of management.

nginx was configured as follows:

the server listens to port 9090 and when it recieves a request it redirects it to port 443 to enable HTTPS
communication

after the server was redirected to port 443 it uses a self signed SSL certificate and key:

the server listens to port 443 and communicates with gunicorn via unix socket
and acts as a load balancer, limiting requests per second, and allowed connections per user

server {
    listen 9090;
    server_name _;
    return 301 https://$host:443$request_uri;
}


server {
    listen 443 ssl;
    server_name _;

    ssl_certificate /etc/nginx/ssl/selfsigned.crt;
    ssl_certificate_key /etc/nginx/ssl/selfsigned.key;

    location / {
        deny 123.45.67.89;
        allow all;
        limit_conn addr 5;
        limit_conn_status 429;

        limit_req zone=one burst=5 nodelay;
        limit_req_status 429;

        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        proxy_pass http://unix:/run/gunicorn.sock;
    }
}

socket implementation:

[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock
SocketUser=www-data
SocketGroup=www-data
SocketMode=0660

[Install]
WantedBy=sockets.target

Deployment instructions:
sudo systemctl daemon-reload
sudo systemctl enable --now gunicorn.socket


sudo nginx -t
sudo systemctl reload nginx
