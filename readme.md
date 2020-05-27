# xCGSM
xCGSM, short for Cross-platform Central Game Server Manager.
The sole purpose for this project is to be able to install game servers from an central point, with little to none knowledge about CLI:s such as bash, shell, powershel, cmd etc.

# Roadmap
Roadmap can be found at https://trello.com/b/a1joIfi0/xcgsm-roadmap

# Generate secretkey
```
python -c 'import os;import binascii;print(binascii.hexlify(os.urandom(32)).decode())'
```

# Create migrations
flask db init
(For windows you need to specify enviorment variable: FLASK_APP: $env:FLASK_APP = 'application')

# To generate migratetion files
flask db migrate

# To upgrade database (create new tables and columns and such)
flask db upgrade

# Downgrade database
flask db downgrade