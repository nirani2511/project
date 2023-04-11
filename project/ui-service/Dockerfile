# Base image
FROM nginx:1.21.1-alpine

# Copy nginx configuration file
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy HTML files to container
COPY index.html /usr/share/nginx/html/
