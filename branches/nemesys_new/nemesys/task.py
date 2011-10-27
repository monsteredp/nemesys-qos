# task.py
# -*- coding: utf8 -*-

# Copyright (c) 2010 Fondazione Ugo Bordoni.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from server import Server

class Task:

  def __init__(self, id, start, server, ftpdownpath, ftpuppath, upload=100,
               download=100, multiplier=5, ping=100, nicmp=4, delay=1, now=False, message=None):
    self._id = id
    self._start = start
    self._server = server
    self._ftpdownpath = ftpdownpath
    self._ftpuppath = ftpuppath
    self._upload = upload
    self._download = download
    self._multiplier = multiplier
    self._ping = ping
    self._nicmp = nicmp
    self._delay = delay
    self._now = now
    self._message = message
  	
  def setPathD(self, bandaDown):	
    self._profilesD=[256,384,512,640,768,1000,1200,1280,1500,1600,2000,2048,3000,4000,4096,6000,6122,7000,7168,8000,8192,10000,12000,16000,20000,20480,24000,30000,34000]

  
    for i in range(1,len(self._profilesD)):
      if (bandaDown>self._profilesD[i-1] and bandaDown<self._profilesD[i]):
        bandaDown=self._profilesD[i]
    
    if (bandaDown>self._profilesD[i]):
        bandaDown=self._profilesD[i]

    ind=self._ftpdownpath.rfind('/')
    self._ftpdownpath=self._ftpdownpath[0:ind+1]+str(bandaDown)+'.rnd'



  @property
  def id(self):
    return self._id

  @property
  def start(self):
    return self._start

  @property
  def server(self):
    return self._server

  @property
  def ftpdownpath(self):
    return self._ftpdownpath

  @property
  def ftpuppath(self):
    return self._ftpuppath

  @property
  def download(self):
    return self._download

  @property
  def multiplier(self):
    return self._multiplier

  @property
  def upload(self):
    return self._upload

  @property
  def ping(self):
    return self._ping

  @property
  def nicmp(self):
    return self._nicmp

  @property
  def delay(self):
    return self._delay

  @property
  def now(self):
    return self._now

  @property
  def message(self):
    return self._message

  def __str__(self):
    return 'id: %s; start: %s; serverip: %s; ftpdownpath: %s; ftpuppath: %s; upload: %d; download: %d; multiplier %d; ping %d; ncimp: %d; delay: %d; now %d; message: %s' % \
      (self.id, self.start, self.server.ip, self.ftpdownpath, self.ftpuppath, self.upload, self.download, self.multiplier, self.ping, self.nicmp, self.delay, self.now, self.message)

if __name__ == '__main__':
  s = Server('s1', '127.0.0.1')
  p = Task(0, '2010-01-01 10:01:00', s, 'r.raw', 'upload/r.raw')
  print p
