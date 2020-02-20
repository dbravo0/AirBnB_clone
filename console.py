#!/usr/bin/python3
"""Console AirBnB"""
import cmd
from models import storage
from models.base_model import BaseModel
from datetime import datetime
from models.amenity import Amenity
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from shlex import split


class HBNBCommand(cmd.Cmd):
    """entry point for the airbnb interpreter"""

    prompt = "(hbnb) "

    a_classes = {"BaseModel", "User", "State", "City",
                 "Amenity", "Place", "Review"}

    def emptyline(self):
        """no spaces"""
        pass

    def do_quit(self, line):
        """Exit the program"""
        return True

    def do_EOF(self, line):
        """exit the program at the end of the file or EOF"""
        return True

    def do_create(self, line):
        """
        Create a new instance and save it
        """
        try:
            if not line:
                raise SyntaxError()
            lists = line.split(" ")
            obj = eval("{}()".format(lists[0]))
            obj.save()
            print("{}".format(obj.id))
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """
        Deletes the instance with the class name and id
        """
        try:
            if not line:
                raise SyntaxError()
            lists = line.split(" ")
            if lists[0] not in self.a_classes:
                raise NameError()
            if len(lists) < 2:
                raise IndexError()
            obj = storage.all()
            key = lists[0] + '.' + lists[1]
            if key in obj:
                del obj[key]
                storage.save()
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """
        Shows all instances with the string
        """
        obj = storage.all()
        lists = []
        if not line:
            for key in obj:
                lists.append(obj[key])
            print(lists)
            return
        try:
            args = line.split(" ")
            if args[0] not in self.a_classes:
                raise NameError()
            for key in obj:
                name = key.split('.')
                if name[0] == args[0]:
                    lists.append(obj[key])
            print(lists)
        except NameError:
            print("** class doesn't exist **")

    def count(self, line):
        """
        Count the number of instances of a class
        """
        counter = 0
        try:
            lists = split(line, " ")
            if lists[0] not in self.a_classes:
                raise NameError()
            obj = storage.all()
            for key in obj:
                name = key.split('.')
                if name[0] == lists[0]:
                    counter += 1
            print(counter)
        except NameError:
            print("** class doesn't exist **")

    def strip_clean(self, args):
        """
        Deletes the argument and return a command string
        """
        new_list = []
        new_list.append(args[0])
        try:
            my_dict = eval(
                args[1][args[1].find('{'):args[1].find('}')+1])
        except Exception:
            my_dict = None
        if isinstance(my_dict, dict):
            new_str = args[1][args[1].find('(')+1:args[1].find(')')]
            new_list.append(((new_str.split(", "))[0]).strip('"'))
            new_list.append(my_dict)
            return new_list
        new_str = args[1][args[1].find('(')+1:args[1].find(')')]
        new_list.append(" ".join(new_str.split(", ")))
        return " ".join(i for i in new_list)

    def do_show(self, line):
        """
        String representation in instance
        """
        try:
            if not line:
                raise SyntaxError()
            lists = line.split(" ")
            if lists[0] not in self.a_classes:
                raise NameError()
            if len(lists) < 2:
                raise IndexError()
            obj = storage.all()
            key = lists[0] + '.' + lists[1]
            if key in obj:
                print(obj[key])
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_update(self, line):
        """
        Update an instance by adding or updating the attribute
        """
        try:
            if not line:
                raise SyntaxError()
            lists = split(line, " ")
            if lists[0] not in self.a_classes:
                raise NameError()
            if len(lists) < 2:
                raise IndexError()
            obj = storage.all()
            key = lists[0] + '.' + lists[1]
            if key not in obj:
                raise KeyError()
            if len(lists) < 3:
                raise AttributeError()
            if len(lists) < 4:
                raise ValueError()
            v = obj[key]
            try:
                v.__dict__[lists[2]] = eval(lists[3])
            except Exception:
                v.__dict__[lists[2]] = lists[3]
                v.save()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")

    def default(self, line):
        """
        Retrieve all instances of a class
        """
        lists = line.split('.')
        if len(lists) >= 2:
            if lists[1] == "all()":
                self.do_all(lists[0])
            elif lists[1] == "count()":
                self.count(lists[0])
            elif lists[1][:4] == "show":
                self.do_show(self.strip_clean(lists))
            elif lists[1][:7] == "destroy":
                self.do_destroy(self.strip_clean(lists))
            elif lists[1][:6] == "update":
                args = self.strip_clean(lists)
                if isinstance(args, list):
                    obj = storage.all()
                    key = args[0] + ' ' + args[1]
                    for k, v in args[2].items():
                        self.do_update(key + ' "{}" "{}"'.format(k, v))
                else:
                    self.do_update(args)
        else:
            cmd.Cmd.default(self, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
