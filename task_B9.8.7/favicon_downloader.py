import wget

# Define the remote file to retrieve
remote_url = 'https://www.google.kz/favicon.ico'

# Download remote and save locally
wget.download(remote_url)