#!/usr/bin/python3
'''
greating console very simple.
'''

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
        elif len(h) >= 1 and h[0] not in HBNBCommand._class:
            print("** class doesn't exist **")
        else:
            new_obj = eval("{}()".format(h[0]))
            storage.new(new_obj)
            storage.save()
            print(new_obj.id)

    def do_show(self, arg):
        """Prints the string representation"""
        h = arg.split()
        a = storage.all()
        p = None
        if len(h) == 2 and h[0] in HBNBCommand._class:
            for key in a:
                if a[key].id == h[1] and a[key].__class__.__name__ == h[0]:
                    p = a[key]
                    break
        if len(h) == 0:
            print("** class name missing **")
        elif len(h) >= 1 and h[0] not in HBNBCommand._class:
            print("** class doesn't exist **")
        elif len(h) == 1 and h[0] in HBNBCommand._class:
            print("** instance id missing **")
        elif len(h) >= 2 and p is None:
            print("** no instance found **")
        else:
            print(p)

    def do_all(self, arg):
        """Prints the string representation"""
        h = arg.split()
        a = storage.all()
        h_list = []
        if len(h) == 1 and h[0] in HBNBCommand._class:
            for key in a:
                if a[key].__class__.__name__ == h[0]:
                    h_list.append(a[key].__str__())
        elif len(h) == 0:
            for key in a:
                h_list.append(a[key].__str__())
        if len(h) == 1 and h[0] not in HBNBCommand._class:
            print("** class doesn't exist **")
        else:
            print(h_list)

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id"""
        h = arg.split()
        a = storage.all()
        f = False
        if len(h) == 2 and h[0] in HBNBCommand._class:
            for key in a:
                if a[key].id == h[1] and a[key].__class__.__name__ == h[0]:
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
        a = storage.all()
        obj_key = None
        if len(h) >= 2 and h[0] in HBNBCommand._class:
            for key in a:
                if a[key].id == h[1]:
                    obj_key = key
                    break
        if len(h) == 0:
            print("** class name missing **")
        elif len(h) == 1 and h[0] in HBNBCommand._class:
            print("** instance id missing **")
        elif h[0] not in HBNBCommand._class:
            print("** class doesn't exist **")
        elif len(h) == 2 and obj_key is not None:
            print("** attribute name missing **")
        elif obj_key is None:
            print("** no instance found **")
        elif len(h) == 3:
            print("** value missing **")
        else:
            setattr(a[key], h[2], h[3])
            storage.save()

    def do_quit(self, line):
        """command quit"""
        return True

    def do_EOF(self, arg):
        """command EOF"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
