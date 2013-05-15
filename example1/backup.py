#!/usr/bin/python
# -*- encoding: utf-8 -*-

import logging
logging.basicConfig(level=logging.INFO)

from bakthat.helper import BakHelper

TARGET_DIR = "/home/dummy"
BACKUP_NAME = "home_dummy"

#password for encryption
BACKUP_PASSWORD = "password"

with BakHelper(BACKUP_NAME,
               password=BACKUP_PASSWORD,
               destination="swift",
               profile="default"
               ) as bh:
    bh.backup(filename=TARGET_DIR)
    bh.rotate(filename=BACKUP_NAME)
