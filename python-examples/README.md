## Description

Use `updateDeliverAllCheck.py` to update the `DeliverAllCheck` spreadsheet without opening Excel. It can be be run from the server.

## Usage
```
	./updateDeliverAllCheck.py

    To Run from command line:
    To run a single command (UpdateTooFast)
    python -c 'import updateDeliverAllCheck; updateDeliverAllCheck.UpdateTooFast()'
    or
    python updateDeliverAllCheck.py allcheck
    python updateDeliverAllCheck.py fast
    python updateDeliverAllCheck.py slow
    
    To run all updates
    python updateDeliverAllCheck.py

```

## Required files
The directory must contain the file `DeliverAllCheck-source.xlsm`.

A copy of this file with current data will be placed in `DeliverAllCheck.xlsm`.

## TODO
Set up a `cron` job to run this on the hour

```
0 * * * * python26 '/home/bvartanian/dev/models/projects/db-excel-update/updateDeliverAllCheck.py' > /home/bvartanian/dev/models/projects/db-excel-update/updateLog.log 2>&1
```

## Dropbox
To set up Dropbox, see instructions here: `http://xmodulo.com/2013/09/access-dropbox-command-line-linux.html`.

install the shell script `dropbox_uploader.sh` using:

`wget https://raw.github.com/andreafabrizi/Dropbox-Uploader/master/dropbox_uploader.sh --no-check-certificate`

An app must be created to allow updates to my dropbox folder.

The app needs folder level access.

## Configuration
Passwords, etc are stored in `my.cnf`

_Do not save the my.cnf file to cvs_

This file has the form

```
[group-name-to-use]
host='host-name-goes-here'
port='port-goes-here'
user='username-goes-here'
password='password-goes-here'

[msql-from-server]
host='ssm-db-vip'
user='om_ro'
password='password-goes-here'
```

## Files
`DeliverAllCheck-source.xlsm`  <-- this file get's read, edited, then saved as another name

`testDeliverAllCheck.xlsm`	<-- The modified file gets saved as this

`my.cnf`						<-- login credentials for mysql (not in CVS)

`dropbox_uploader.sh`			<-- Needed for uploading to dropbox from linux

`cronUpdateDeliver.sh`		<-- Shell script to run

### required libraries
mysqldb
setuptools ?
openpyxl

## Uploading to Box.com
email address = upload.test_up.anqecdijvi@u.box.com