#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  inotifier.py
#  
# 


from twisted.internet import inotify
from twisted.python import filepath
from twisted.internet import reactor
import os
import shutil
import datetime
import sys


create_list = []

created_times = {}

moved_to_list = []

attrib_list = []

name_changed_list = []

def translate_mask(mask):
	
	mask_index = {
	1: 'IN_ACCESS', 
	2: 'IN_MODIFY', 
	4: 'IN_ATTRIB', 
	8: 'IN_CLOSE_WRITE', 
	16: 'IN_CLOSE_NOWRITE', 
	32: 'IN_OPEN', 
	64: 'IN_MOVED_FROM', 
	128: 'IN_MOVED_TO', 
	256: 'IN_CREATE', 
	512: 'IN_DELETE', 
	1024: 'IN_DELETE_SELF', 
	8192: 'IN_UNMOUNT', 
	16384: 'IN_Q_OVERFLOW', 
	32768: 'IN_IGNORED',  
	1073742080: 'IN_ISDIR', 
	2147483648: 'IN_ONESHOT' 
		}
		
	return mask_index[mask]

def process_inotify_parameters(watch, path, mask):

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
		
	mask_trans = translate_mask(mask)

	info = {
	'inode':inode, 
	'path':path.path, 
	'dirname':dirname, 
	'extension':extension, 
	'basename':basename, 
	'mask':mask, 
	'mask_trans':mask_trans, 
	'date_time':date_time}
	

	return info

def make_info_tuple(info):
	return (
	info['inode'],
	info['path'],
	info['dirname'],
	info['extension'],
	info['basename'],
	info['mask'],
	info['mask_trans'],
	info['date_time'],)

class FileSystemWatcher(object):

	def __init__(self, path_to_watch):
		self.path = path_to_watch
		self.inotify_list = []
		
		
	def Start(self):
		notifier = inotify.INotify()
		notifier.startReading()
		notifier.watch(filepath.FilePath(self.path),
                   callbacks=[self.SortInotifyCalls,self.AllInotifyCalls],autoAdd=True,recursive=False)
	
	
	def SortInotifyCalls(self, watch, path, mask):
		
		info = process_inotify_parameters(watch, path, mask)
		
		
		mask_trans = info['mask_trans']

		if mask_trans == 'IN_ACCESS':
			self.OnAccess(watch, path, mask)
			
		if mask_trans == 'IN_MODIFY':
			self.OnModify(watch, path, mask)
			
		if mask_trans == 'IN_ATTRIB':
			self.OnAttrib(watch, path, mask)
			
		if mask_trans == 'IN_CLOSE_WRITE':
			self.OnCloseWrite(watch, path, mask)
			
		if mask_trans == 'IN_CLOSE_NOWRITE':
			self.OnCloseNoWrite(watch, path, mask)
		
		if mask_trans == 'IN_OPEN':
			self.OnOpen(watch, path, mask)
			
		if mask_trans == 'IN_MOVED_FROM':
			self.OnMovedFrom(watch, path, mask)
		
		if mask_trans == 'IN_MOVED_TO':
			self.OnMovedTo(watch, path, mask)
		
		if mask_trans == 'IN_CREATE':
			self.OnCreate(watch, path, mask)
			
		
		
		
			
	def AllInotifyCalls(self, watch, path, mask):
		print "call"
		
		info = process_inotify_parameters(watch, path, mask)
		info_tuple = make_info_tuple(info)
		self.inotify_list.append(info_tuple)
		#print self.inotify_list
		
		
	def OnAccess(self, watch, path, mask):
		print "access"
		
	def OnModify(self, watch, path, mask):
		print "modify"
		
	def OnAttrib(self, watch, path, mask):
		print "attribute"
		'''
		info = process_inotify_parameters(watch, path, mask)
		attrib_list.append(info)
		
		
		if info['inode'] in create_list:
			in_create_list = True
		else:
			in_create_list = False
		
		if in_create_list:
			#self.Change_Name(watch, path, mask)
			pass
		'''	
		
	def OnCloseWrite(watch, path, mask):
		print "closed write"
	
	def OnCloseNoWrite(watch, path, mask):
		print "closed no-write"
		
	def OnOpen(watch, path, mask):
		print "open"
		
	def onMovedFrom(self, watch, path, mask):
		print 'moved from'
		
	def OnMovedTo(self, watch, path, mask):
		print "moved to"
		'''
		info = process_inotify_parameters(watch, path, mask)
		moved_to_list.append(info['inode'])
		'''
		
	def OnCreate(self, watch, path, mask):
		print 'create'
		
		'''
		info = process_inotify_parameters(watch, path, mask)
		inode = info['inode']
		date_time = info['date_time']
		create_list.append(inode)
		created_times[inode] = date_time
		'''	
	

'''
	def Change_Name(self, watch, path, mask):
		info = process_inotify_parameters(watch, path, mask)
		if info['inode'] not in name_changed_list:
			old_basename = info['basename']
			new_basename = created_times[info['inode']] + '---' + old_basename
			old_name = os.path.join(info['dirname'], old_basename)
			new_name = os.path.join(info['dirname'], new_basename)
			shutil.move(old_name,new_name)
			name_changed_list.append(info['inode'])
		
'''



	

def main():
	if len(sys.argv) > 1:
		dir_watch = str(sys.argv[1])
	else:
		dir_watch = '/home/me/Downloads/'
	fs = FileSystemWatcher(dir_watch)
	fs.Start()
	reactor.run()
	return 0

if __name__ == '__main__':
	main()

			
'''
	
'''			
