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
        self._members = members

    
    def add_member(self, member):
        self._members.append(member)

    @members.deleter
    def delete_member(self, member_pos):
        del self._members[member_pos]
    
    @property
    def travel_pace(self):
        speeds = []

        for member in self.members:
            member_speed = convert_fpt_to_mph(member.get_speed())
            speeds.append(member_speed)
    
        return min(speeds)


class Adventurer:
    def __init__(self, name="", strength=0, size=0, speed=0, 
                carryingCapacity = 0, mount=None, passivePerception=0, 
                metavision=(0, 0), encumberment=1, exhaustionLevel=0):
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
        self.name = name
    
    def delete_name(self):
        self.name = ""

    def get_strength(self):
        return self.strength

    def set_strength(self, strength):
        self.strength = strength

    def delete_strength(self):
        self.strength = 0

    def get_size(self):
        return self.size

    @property
    def carryingCapacity(self):
        return self.strength*self.size*15

    def delete_size(self):
        self.size = 0

    def get_speed(self):
        if self.mount is None:
            return self.speed
        else:
            return self.mount.speed

    def set_speed(self, speed):
        self.speed = speed

    def delete_speed(self):
        self.speed = 0 

    def get_mount(self):
        return self.mount

    def set_mount(self, mount):
        self.mount = mount

    def delete_mount(self):
        self.mount = None
    
    def get_passive_perception(self):
        return self.passivePerception

    def set_passive_perception(self, passivePerception):
        self.passivePerception = passivePerception

    def delete_passive_perception(self):
        self.passivePerception = 0

    def get_metavision(self):
        return self.metavision

    def set_metavision(self, metavisionTuple):
        self.metavision = metavisionTuple

    def delete_metavision(self):
        self.metavision = (0, 0)

    def get_encumberment(self):
        return self.encumberment

    def set_encumberment(self, encumbermentValue):
        self.encumberment = encumbermentValue

    def delete_encumberment(self):
        self.encumberment = 0

class Mount:
    def __init__(self, name="", strength=0, size=0, speed=0):
        self.name = name
        self.strength = strength
        self.size = size
        self.speed = speed

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def delete_name(self):
        self.name = None

    def get_strength(self):
        return self.strength

    def set_strength(self, strength):
        self.strength = strength

    def delete_strength(self):
        self.strength = 0

    @property
    def carryingCapacity(self):
        return self.strength*self.size*15

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size

    def delete_size(self):
        self.size = 0

    def get_speed(self):
        return self.speed()
    
    def set_speed(self, speed):
        self.speed = speed

    def delete_speed(self):
        self.speed = 0

def convert_fpt_to_mph(fptSpeed):
    return fptSpeed/10