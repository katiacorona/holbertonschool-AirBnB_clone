#!/usr/bin/python3
"""
Console, entry point of the command interpreter
"""

import cmd
import models
from models.base_model import BaseModel
from models import storage
from models import allclasses
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter using the
    cmd module
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Typing quit will exit the console
        """
        quit()

    def do_EOF(self, arg):
        """
        Typing EOF will exit the console
        important - console its case-sensitive
        """
        quit()

    def emptyline(line):
        """
        An empty line + ENTER = pass
        Nothing happens
        """
        pass

    def do_create(self, arg):
        """
        Typing create creates a new instance of an object,
        saves it and prints its id.
        If class name is missing an error will be shown.
        If class name doesn´t exists an error will be shown.
        """
        if not arg:
            print("** class name missing **")
        else:
            arg_split = arg.split(" ")
            if arg_split[0] not in allclasses:
                print("** class doesn't exist **")
            else:
                """
                create new obj
                """
                my_obj = eval(arg_split[0])()
                my_obj.save()
                print(my_obj.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based
        on the class name and id.
        """
        if not arg:
            print("** class name missing **")
        else:
            arg_split = arg.split(" ")
            if arg_split[0] not in allclasses:
                print("** class doesn't exist **")
            else:
                """
                Check if id exists and is not missing
                """
                if len(arg_split) < 2:
                    print("** instance id missing **")
                else:
                    obj_name = arg_split[0]
                    obj_id = arg_split[1]
                    key = str(obj_name) + "." + str(obj_id)
                    if key not in models.storage.all():
                        print("** no instance found **")
                    else:
                        print(models.storage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and
        id (save the change into the JSON file).
        """
        if not arg:
            print("** class name missing **")
        else:
            arg_split = arg.split(" ")
            if arg_split[0] not in allclasses:
                print("** class doesn't exist **")
            else:
                """
                Check if id exists and is not missing
                """
                if len(arg_split) < 2:
                    print("** instance id missing **")
                else:
                    obj_name = arg_split[0]
                    obj_id = arg_split[1]
                    key = str(obj_name) + "." + str(obj_id)
                    if key not in models.storage.all():
                        print("** no instance found **")
                    else:
                        del(models.storage.all()[key])
                        models.storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        if not arg:
            """
            Prints all the storage dictionary
            Because we didnt specify the Class
            """
            my_dict = models.storage.all()
            for key, val in my_dict.items():
                print(val)
        else:
            arg_split = arg.split(" ")
            if arg_splt[0] not in allclasses:
                print("** class doesn't exist **")
            else:
                my_dict = models.storage.all()
                for key, val in my_dict.items():
                    if val.__class__.__name__ == arg_split[0]:
                        print(val)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and
        id by adding or updating attribute (save the change
        into the JSON file)
        """


if __name__ == '__main__':
    HBNBCommand().cmdloop()
