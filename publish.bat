pelican content -s publishconf.py -t pelican-themes/antonyholmes -o publish
aws s3 sync --size-only publish s3://www.antonyholmes.com