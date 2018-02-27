import ch
import random
import sys
import os
import time

class botgrandover(ch.RoomManager):
  def onInit(self):
      print("Osu!")
      self.setNameColor("000000")
      self.setFontColor("000000")
      self.setFontFace("Ariel")
      self.setFontSize(11)

  def onConnect(self,room):
      print("[INFO] Connected to : "+room.name)
      self.setNameColor("000000")
      self.setFontColor("000000")
      self.setFontFace("Ariel")
      self.setFontSize(11)
      room.message("You have summoned me, Master?")

  def onConnectFail(self, room):
      print("Failed to connect to "+room.name+ ", trying to reconnect..")
      room.reconnect()

  def onReconnect(self,room):
      print("[INFO] Connected to : "+room.name)
      self.setNameColor("000000")
      self.setFontColor("000000")
      self.setFontFace("Ariel")
      self.setFontSize(11)
      room.message("Back!（＾◇＾)")
	
  def onDisconnect(self,room):
      print("[INFO] Disconnected from : "+room.name)
      self.setNameColor("000000")
      self.setFontColor("000000")
      self.setFontFace("Ariel")
      self.setFontSize(11)
      room.message("Farewell.")

  def onFloodWarning(self,room):
      print("[INFO] FloodWarning in : "+room.name)
      room.reconnect()

  def onJoin(self, room, user):
      print(user.name + " joined the chat!")
 
  def onLeave(self, room, user):
      print(user.name + " left the chat!")

  def onMessage(self,room,user,message):
      print(user.name+" : "+message.body)

      msgdata = message.body.split(" ",1)  
      if len(msgdata) > 1:
          cmd, args = msgdata[0], msgdata[1]
      else:
          cmd, args = msgdata[0], ""
      cmd=cmd.lower()
      
      elif cmd == ".pat":
      room.message(":3")
      
      elif cmd == ".say":
      if args:
        room.message(args)
      else:
        room.message("Nothing to say")

rooms = ["fategrandorder"]

if __name__ == "__main__":
    botgrandover.easy_start(rooms, "botgrandover", "Pokemon")
