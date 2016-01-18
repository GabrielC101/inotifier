#!/usr/bin/env python

from twisted.internet import inotify
from twisted.python import filepath
from twisted.internet import reactor
import os
import shutil
import datetime
import sys

intoify_tags = {1: 'IN_ACCESS', 2: 'IN_MODIFY', 4: 'IN_ATTRIB', 8: 'IN_CLOSE_WRITE', 16: 'IN_CLOSE_NOWRITE', 32: 'IN_OPEN', 64: 'IN_MOVED_FROM', 128: 'IN_MOVED_TO', 256: 'IN_CREATE', 512: 'IN_DELETE', 1024: 'IN_DELETE_SELF', 8192: 'IN_UNMOUNT', 16384: 'IN_Q_OVERFLOW', 32768: 'IN_IGNORED',  1073741824: 'IN_ISDIR', 2147483648: 'IN_ONESHOT' }
"""
class FileSystemWatcher(object):

  def __init__(self, path_to_watch):
    self.path = path_to_watch
    self.masks = {1: 'IN_ACCESS', 2: 'IN_MODIFY', 4: 'IN_ATTRIB', 8: 'IN_CLOSE_WRITE', 16: 'IN_CLOSE_NOWRITE', 32: 'IN_OPEN', 64: 'IN_MOVED_FROM', 128: 'IN_MOVED_TO', 256: 'IN_CREATE', 512: 'IN_DELETE', 1024: 'IN_DELETE_SELF', 8192: 'IN_UNMOUNT', 16384: 'IN_Q_OVERFLOW', 32768: 'IN_IGNORED',  1073741824: 'IN_ISDIR', 2147483648: 'IN_ONESHOT' }
"""
class FileSystemWatcher(object):

	def __init__(self, path_to_watch):
		self.path = path_to_watch
		self.inotify_list = []
		
		self.masks = {1: 'IN_ACCESS', 2: 'IN_MODIFY', 4: 'IN_ATTRIB', 8: 'IN_CLOSE_WRITE', 16: 'IN_CLOSE_NOWRITE', 32: 'IN_OPEN', 64: 'IN_MOVED_FROM', 128: 'IN_MOVED_TO', 256: 'IN_CREATE', 512: 'IN_DELETE', 1024: 'IN_DELETE_SELF', 8192: 'IN_UNMOUNT', 16384: 'IN_Q_OVERFLOW', 32768: 'IN_IGNORED',  1073742080: 'IN_ISDIR', 2147483648: 'IN_ONESHOT' }
		self.created_times = {}
		self.create_list = []
		self.moved_to_list = []
		self.attrib_list = []
		self.name_changed_list = []
	def Start(self):
		notifier = inotify.INotify()
		notifier.startReading()
		notifier.watch(filepath.FilePath(self.path),
                   callbacks=[self.OnChange],autoAdd=True,recursive=True)

	def OnChange(self, watch, path, mask):
		
		if path.exists():
			try:
				inode = path.getInodeNumber()
			except:
				inode = 0
		else:
			inode = 0
			
		t = datetime.datetime.today()
		date_time = str(t.year) + '-' + str(t.month) + '-' +  str(t.day) + '---' +  str(t.hour) + ':' +  str(t.minute) + ':' +  str(t.second)
		date_time = str(date_time)
		
		extension = os.path.splitext(path.path)[1]
		
		basename = path.basename()
		
		dirname = path.dirname()
		
		mask_trans = self.masks[mask]
		
		info = {'inode':inode, 'path':path.path, 'dirname':dirname, 'extension':extension, 'basename':basename, 'mask':mask, 'mask_trans':mask_trans, 'date_time':date_time}
		
		self.inotify_list.append(info)
		
		#if info['mask_trans'] is not "IN_MODIFY":
		#	print info['mask_trans']
		
		if mask_trans == 'IN_CREATE':
			self.OnCreate(info)
			
		if mask_trans == 'IN_MOVED_TO':
			self.OnMovedTo(info)
		
		if mask_trans == 'IN_ATTRIB':
			self.OnAttrib(info)
			
		
			
		'''
		if self.masks[mask] is not 'IN_MODIFY':
			
			if self.masks[mask] == 'IN_CREATE':
				self.created_times[inode] = date_time			

					
			info = (inode, path.path, dirname, extension, basename, mask, mask_trans, date_time,  )
			print info
			self.inotify_list.append(info)
		'''
	def OnCreate(self, info):
		inode = info['inode']
		date_time = info['date_time']
		self.create_list.append(inode)
		
		self.created_times[inode] = date_time
			
	def OnMovedTo(self, info):
		self.moved_to_list.append(info['inode'])
		
	def OnAttrib(self, info):
		self.attrib_list.append(info)
		
		
		if info['inode'] in self.create_list:
			in_create_list = True
		else:
			in_create_list = False
		#print "in_create_list is " + str(in_create_list)
		
		'''
		if info['inode'] in self.moved_to_list:
			in_moved_to_list = True
		else:
			in_moved_to_list = False
		print "in_moved_to_list is " + str(in_create_list)
		'''
		
		#if in_create_list and in_moved_to_list:
		if in_create_list:
			self.Change_Name(info)
			
	def Change_Name(self, info):
		if info['inode'] not in self.name_changed_list:
			old_basename = info['basename']
			#old_base = os.path.splitext(old_name)[0]
			#old_extension = info['extension']
			new_basename = self.created_times[info['inode']] + '---' + old_basename
			old_name = os.path.join(info['dirname'], old_basename)
			new_name = os.path.join(info['dirname'], new_basename)
			shutil.move(old_name,new_name)
			self.name_changed_list.append(info['inode'])
			#print "renamed " + old_basename + " to " + new_basename
		


if __name__ == '__main__':
	if len(sys.argv) > 1:
		dir_watch = str(sys.argv[1])
	else:
		dir_watch = '/home/me/Downloads/'
	fs = FileSystemWatcher(dir_watch)
	fs.Start()
	reactor.run()
