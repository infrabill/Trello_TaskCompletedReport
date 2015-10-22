## Development Setup
You need to initialize your virtual environment. To do so run the following
commands from the root of the project

```bash
$ virtualenv2 .env
$ source .env/bin/activate
$ pip install -r requirements.txt
```

## config-gen.py
Takes the key and secret key from command line and generates an oauth key and
secret that will be set in the config.

### Example Usage
```bash
$ # Write oauth creds for trello
$ config-gen -c [CONFIG] init-trello [KEY] [SECRET]
$ # Write oauth creds for google
$ config-gen -c [CONFIG] init-drive [KEY] [SECRET]
```

## report.py
Using the credentials in config.ini, this application will pull all the cards
from a specific list and orginize them by owner.

The output report will be by task owner by task.

### Example Output

```
    -===========================================-
    -= [TASK OWNER ]                           =-
    -===========================================-
    -  [First Card Name]                        -
    -  [Second Card Name]                       -
    -  [Third Card Name]                        -
    -  [Fourth Card Name]                       -
    -===========================================-

    -===========================================-
    -= [TASK OWNER ]                           =-
    -===========================================-
    -  [First Card Name]                        -
    -  [Second Card Name]                       -
    -  [Third Card Name]                        -
    -  [Fourth Card Name]                       -
    -===========================================-
```

## publish.py
Publish will publish any string of text on STDIN to a google drive location
specified in the config file.

### Example Usage
```bash
echo "My cool report" | publish.py -c config.ini
```

## Configuration File Layout
The configuration file will hold the following keys:
- Trello API Key
- Trello API Key Secret
- Trello OAuth Key
- Trello OAuth Secret
- Board Names
- Lists under board
- Google drive publish location

### Example Configuration File:
```ini
[DEFAULT]
trello_key: abc123
trello_key_secret: 321cba
trello_oauth_key: xyz789
trello_oauth_secret: 987zyx

google_key: abc123
google_key_secret: abc123
google_oauth_key: abc123
google_oauth_secret: abc123

drive_path: /some/path/in/google/drive

[BOARD:BoardAlias]
board_id: hash123
list_id: hash321

[BOARD:AnotherBoardAlias]
board_id: hash789
list_id: hash987
```
