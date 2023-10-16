#!/usr/bin/python3
'''
greating console very simple.
'''

import datetime
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    '''
Simple command processor example.
'''
	prompt = '(hbnb) '
	_class = {
		"BaseModel",
		"User",
		"Place",
		"Amenity",
		"Review",
		"State",
		"City"
		}

	def emptyline(self):
		"""command empty line"""
		pass

	def help_quit(self):
		"""command Help quit"""
		print('Quit command to exit the program')
		print()

	def do_create(self, arg):
		"""Creates a new instance"""
		h = arg.split()
		if len(h) == 0:
			print("** class name missing **")
		elif h[0] not in HBNBCommand._class:
			print("** class doesn't exist **")
		else:
			print(eval(h[0])().id)
			storage.save()

	def do_show(self, arg):
		"""Prints the string representation"""
		h = arg.split()
		a = storage.all()
		f = False
		p = ""
		if len(h) == 2 and h[0] in HBNBCommand._class:
			for key in a:
				if a[key]['id'] == h[1]:
					current_obj = eval("{}(a[key])".format(h[0]))
					current_obj.id = h[1]
					p = "{}".format(current_obj)
					f = True
					break
		if len(h) == 0:
			print("** class name missing **")
		elif h[0] not in HBNBCommand._class:
			print("** class doesn't exist **")
		elif len(h) == 1 and h[0] in HBNBCommand._class:
			print("** instance id missing **")
		elif len(h) == 2 and f is False:
			print("** no instance found **")
		else:
			print(p)

	def do_all(self, arg):
		"""Prints the string representation"""
		h = arg.split()
		if len(h) == 0:
			print("** class name missing **")
		elif h[0] not in HBNBCommand._class:
			print("** class doesn't exist **")
		else:
			print([eval(h[0])().__str__()])

	def do_destroy(self, arg):
		""" Deletes an instance based on the class name and id"""
		h = arg.split()
		a = storage.all()
		f = False
		if len(h) == 2 and h[0] in HBNBCommand._class:
			for key in a:
				if a[key]['id'] == h[1]:
					del a[key]
					f = True
					break
		if len(h) == 0:
			print("** class name missing **")
		elif h[0] not in HBNBCommand._class:
			print("** class doesn't exist **")
		elif len(h) == 1 and h[0] in HBNBCommand._class:
			print("** instance id missing **")
		elif len(h) == 2 and f is False:
			print("** no instance found **")
		else:
			storage.save()

	def do_update(self, arg):
		"""updates the string representation"""
		h = arg.split()
		print(len(h))
		s = ""
		a = storage.all()
		f = False
		if len(h) >= 2 and h[0] in HBNBCommand._class:
			for key in a:
				if a[key]['id'] == h[1]:
					current_obj = eval("{}(a[key])".format(h[0]))
					current_obj.id = h[1]
					if len(h) == 4:
						eval("setattr(current_obj, h[2],h[3])")
					s = "{}".format(current_obj)
					f = True
					break
		if len(h) == 0:
			print("** class name missing **")
		elif h[0] not in HBNBCommand._class:
			print("** class doesn't exist **")
		elif len(h) == 1 and h[0] in HBNBCommand._class:
			print("** instance id missing **")
		elif len(h) == 2 and f is False:
			print("** no instance found **")
		elif len(h) == 2 and h[0] in HBNBCommand._class and f is True:
			print("** attribute name missing **")
		elif len(h) == 3 and h[0] in HBNBCommand._class:
			print("** value missing **")
		else:
			print(s)

	def do_quit(self, line):
		"""command quit"""
		return True

	def do_EOF(self, arg):
		"""command EOF"""
		return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

