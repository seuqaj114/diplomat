#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sender
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler

username="iris"
password="laranja"

def test_sync_file(full_path):
	s=full_path.split("/")
	for x in s[:-1]:
		if "." in x:
			return False
			
	return True

class MyHandler(FileSystemEventHandler):
	def on_created(self,event):
		print event.src_path+" created"
		#sender.warning(event.src_path)
		if test_sync_file(event.src_path):
			sender.post_open(event.src_path,username)
	def on_deleted(self,event):
		print event.src_path+" deleted"
		if test_sync_file(event.src_path):
			sender.delete_open(event.src_path,username)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
			time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
