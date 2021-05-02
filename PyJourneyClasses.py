"""
PyJourneyClasses.py
Sets the classses included into the PyJourney code
"""

"""
If variable insertion is closed, 
so only reduced to the get-set-del,
data input check should go on the get
"""

class Group:
    def __init__(self, members=[]):
        self.members = members

    @property
    def members(self):
        return self._members

    @members.setter
    def set_members(self, members):
        # Check if array of Adventurer object
        self._members = members

    def add_member(self, member):
        self._members.append(member)

    @members.deleter
    def delete_member(self, member_pos):
        del self._members[member_pos]

    def del_all_members(self):
        self._members = None

    @property
    def travel_pace(self):
        speeds = []

        for member in self.members:
            member_speed = convert_fpt_to_mph(member.get_speed())
            speeds.append(member_speed)
    
        return min(speeds)


class Adventurer:
    def __init__(self, name="", strength=0, size=0, speed=-1, 
                carryingCapacity=-1, mount=0, passivePerception=0, 
                metavision=(-1, -1), encumberment=-1,
                exhaustionLevel=-1):
        self.name = name
        self.strength = strength
        self.size = size
        self.speed = speed
        self.mount = mount
        self.passivePerception = passivePerception
        self.metavision = metavision
        self.encumberment = encumberment
        self.exhaustionLevel = exhaustionLevel

    def get_name(self):
        return self.name

    def set_name(self, name):
        # Check if string
        try:
            if isinstance(name, str):
                if name != "":
                    self.name = name
                else:
                    raise ValueError("Mount name is empty")
            else:
                raise TypeError("Mount name should be a string, "\
                    "recieved a", name)
        except TypeError as e:
            print(e)
    
    def delete_name(self):
        self.name = None

    def get_strength(self):
        return self.strength

    def set_strength(self, strength):
        try:
            if isinstance(strength, int):
                if (strength >= 1 and strength <= 20 
                and self.strength != strength):
                    self.strength = strength
                    
                elif self.strength == strength:
                    raise ValueError("Input value and current strenth "\
                        "value are the same :", strength, ". No change"\
                        " needed")
                else:
                    raise ValueError("Strength sould be comprised " \
                    "between 1 and 20, recieved", strength)
            else:
                raise TypeError("Strength value should be an integer, "\
                    "recieved", strength)
        except (TypeError, ValueError) as e:
            print(e)

    def delete_strength(self):
        self.strength = None

    def get_size(self):
        return self.size

    @property
    def carryingCapacity(self):
        return self.strength*self.size*15

    def delete_size(self):
        self.size = None

    def get_speed(self):
        if self.mount is None:
            return self.speed
        else:
            return (self.speed, self.mount.speed)

    def set_speed(self, speed):
        # Check if positive integer
            # -1 default value
            # None deleted value 
        try:
            if isinstance(speed, int):
                if speed >= 0:
                    self.speed = speed
                elif self.speed == speed:
                    raise ValueError ("Input value and current speed "\
                        "value are the same :", speed, \
                        ". No change needed")
                else:
                    raise ValueError("Speed input value should be "\
                        "a positive integer, recieved ", speed)
            else:
                raise TypeError("Speed should be an integer, "\
                    "recieved a", type(speed))
        except (TypeError, ValueError) as e:
            print(e)

    def delete_speed(self):
        self.speed = None

    def get_mount(self):
        return self.mount

    def set_mount(self, mount):
        # Check if mount object
        self.mount = mount

    def delete_mount(self):
        self.mount = None
    
    def get_passive_perception(self):
        return self.passivePerception

    def set_passive_perception(self, passivePerception):
        # Check if positive integer between 1 and 20
        try:
            if isinstance(passivePerception, int):
                if (passivePerception >= 1 and passivePerception <= 20 
                and self.passivePerception != passivePerception):
                    self.passivePerception = passivePerception
                elif self.passivePerception == passivePerception:
                    raise ValueError("Input value and current passive "\ 
                        "perception value are the same :", 
                        passivePerception, ". No change needed")
                else:
                    raise ValueError("Passive perception sould be "\ 
                    "comprised between 1 and 20, recieved", strength)
            else:
                raise TypeError("Passive perception value should be "\ 
                    "an integer, recieved", passivePerception)
        except (TypeError, ValueError) as e:
            print(e)

    def delete_passive_perception(self):
        self.passivePerception = 0

    def get_metavision(self):
        return self.metavision

    def set_metavision(self, metavisionTuple):
        try:
            if isinstance(metavisionTuple, tuple):
                if (isinstance(metavisionTuple[0], int) 
                and metavisionTuple[0] in [1, 2, 3]):
                    if (isinstance(metavisionTuple[1], int)
                    and metavisionTuple[1] > 0):
                        self.metavision = metavisionTuple

                    elif isinstance(metavisionTuple[1], int) == False:
                        raise ValueError("MetavisionTuple second "\
                        "parameter should be an integer, recieved",
                        metavisionTuple[1])

                    else:
                        raise ValueError("MetavisionTuple second "\
                        "parameter should be a positive integer, "\
                        "recieved", metavisionTuple[1])

                elif isinstance(metavisionTuple[0], int) == False:
                    raise ValueError("MetavisionTuple first "\
                    "parameter should be an integer, recieved", 
                    metavisionTuple[0])

                else:
                    raise ValueError("MetavisionTuple first "\
                    "parameter should be comprised between 1 and 3, "\
                    "recieved", metavisionTuple[0])

            else:
                raise TypeError("metavisionTuple should be a tuple, "\
                    "recieved a", type(metavisionTuple))

        except (TypeError, ValueError) as e:
            print(e)

    def delete_metavision(self):
        self.metavision = None

    def get_encumberment(self):
        return self.encumberment

    def set_encumberment(self, encumbermentValue):
        # Boolean 
        self.encumberment = encumbermentValue

    def delete_encumberment(self):
        self.encumberment = None

    def get_exhaustionLevel(self):
        return self.exhaustionLevel

    def set_exhaustionLevel(self, exhaustionLevel):
        # Check if integer between 0 and 6
            # -1 default value
            # None deleted
        try:
            if isinstance(exhaustionLevel, int):
                if (exhaustionLevel >= 0 and exhaustionLevel <= 6
                and self.exhaustionLevel != exhaustionLevel):
                    self.exhaustionLevel = exhaustionLevel
                elif self.exhaustionLevel == exhaustionLevel:
                    raise ValueError("Input value and current "\ 
                        "exhaustion level value are the same :", 
                        exhaustionLevel, ". No change needed")
                else:
                    raise ValueError("Exhaustion level sould be "\ 
                    "comprised between 0 and 6, recieved", 
                    exhaustionLevel)
            else:
                raise TypeError("Exhaustion level value should be "\ 
                    "an integer, recieved", exhaustionLevel)
        except (TypeError, ValueError) as e:
            print(e)

    def del_exhaustionLevel(self):
        self.exhaustionLevel = None

class Mount:
    def __init__(self, name="", strength=0, size=0, speed=0):
        self.name = name
        self.strength = strength
        self.size = size
        self.speed = speed

    def get_name(self):
        return self.name

    def set_name(self, name):
        try:
            if isinstance(name, str):
                if name != "":
                    self.name = name
                else:
                    raise ValueError("Mount name is empty")
            else:
                raise TypeError("Mount name should be a string.")
        except TypeError as e:
            print(e)

    def delete_name(self):
        self.name = None

    def get_strength(self):
        return self.strength

    def set_strength(self, strength):
        try:
            if isinstance(strength, int):
                if (strength >= 1 and strength <= 20 
                and self.strength != strength):
                    self.strength = strength
                elif self.strength == strength:
                    raise ValueError("Input value and current strenth "\
                        "value are the same :", strength, ". No change"\
                        " needed")
                else:
                    raise ValueError("Strength sould be comprised " \
                    "between 1 and 20, recieved", strength)
            else:
                raise TypeError("Strength value should be an integer, "\
                    "recieved", strength)
        except (TypeError, ValueError) as e:
            print(e)

    def delete_strength(self):
        self.strength = None

    @property
    def carryingCapacity(self):
        return self.strength*self.size*15

    def get_size(self):
        return self.size

    def set_size(self, size):
        try:
            if isinstance(size, int) or isinstance(size, float):
                if (size in [0.25, 0.5, 1, 2, 4, 6] 
                and size != self.size):
                    self.size = size
                elif self.size == size:
                    raise ValueError("Input value and current size "\
                        "value are the same :", size, \
                        ". No change needed")
                else:
                    raise ValueError("Size sould be one of these "\
                        "values : 0.25, 0.5, 1, 2, 4, 6; recieved", 
                        size)
            else:
                raise TypeError("Ize value should be an integer "\
                    "or a float, recieved", size)
        except (TypeError, ValueError) as e:
            print(e)

    def delete_size(self):
        self.size = None


    def get_speed(self):
        return self.speed()


    def set_speed(self, speed):
        try:
            if isinstance(speed, int):
                if speed >= 0:
                    self.speed = speed
                elif self.speed == speed:
                    raise ValueError ("Input value and current speed "\
                        "value are the same :", speed, \
                        ". No change needed")
                else:
                    raise ValueError("Speed input value should be "\
                        "a positive integer, recieved ", speed)
            else:
                raise TypeError("Speed should be an integer, "\
                    "recieved a", type(speed))
        except (TypeError, ValueError) as e:
            print(e)

    def delete_speed(self):
        self.speed = None

def convert_fpt_to_mph(fptSpeed):
    return fptSpeed/10