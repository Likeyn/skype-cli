#!/usr/bin/env python2.7
# Skype CLI client
# Requires a running instance of Skype
#
# @author Likeyn
# @dependency Skype4Py
# @link https://github.com/awahlig/skype4py

import Skype4Py

# Show bookmarked chats
def showBookmarked():
	i = 1
	print "Bookmarked chats:"
	for bc in s.BookmarkedChats:
		print "   %d. %s (%s)" % (i, bc.FriendlyName, bc.Name)
		i = i + 1
	
	print "   q. Quit"
	num = raw_input('Choose a chat > ')
	try:
		num = int(num) - 1
	
	except ValueError:
		if num == 'q':
			print "Exiting."
			exit(0)
		else:
			print "Please pick a chat number."
			showBookmarked()
	
	showChat(s.BookmarkedChats[num])
	showBookmarked()

# Show chat
def showChat(chat):
	if chat.Bookmarked: b = "Bookmarked";
	else: b = "Not bookmarked";
	print """
%s
-------------------
%s - %s
%s - %s
-------------------
""" % (chat.FriendlyName, chat.Name, b, chat.Timestamp, chat.Members)
	for m in chat.RecentMessages:
		dt = m.Datetime
		print "[%d:%d:%d] %s: %s" % (dt.hour, dt.minute, dt.second, m.FromDisplayName, m.Body)
	
	print """
-------------------
	s: send a message	o: open chat window
	m: messages		q: quit
"""
	cmd = raw_input("> ")
	if cmd == 's':
		m = raw_input('Message > ')
		chat.SendMessage(m)
	elif cmd == 'o': chat.OpenWindow();
	elif cmd == 'm': showMessages(chat);
	elif cmd == 'q': return;
	else: print "Huh?";
	showChat(chat)

# Show missed message
def showMissedMessage(message, status):
	dt = message.Datetime
	print "--- On %s ---" % message.Chat.FriendlyName
	print "[%d:%d:%d] %s: %s" % (dt.hour, dt.minute, dt.second, message.FromDisplayName, message.Body)

# Show messages
def showMessages(chat):
	print "Unsupported"
	showChat(chat)


# Create a Skype instance
s = Skype4Py.Skype()
s.Attach()
s.OnMessageStatus = showMissedMessage

showBookmarked()
