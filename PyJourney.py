class Group:
    def __init__(self, members=[]):
        self.members = members

    def get_members(self):
        return self.members

    def set_members(self, members):
        self.members = members

    def add_member(self, member):
        self.members.append(member)
    
    @property
    def travelPace(self):
        speeds = []

        for member in self.members:
            memberSpeed = convert_fpt_to_mph(member.get_speed())
            speeds.append(memberSpeed)
    
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

    def get_strength(self):
        return self.strength

    def set_strength(self, strength):
        self.strength = strength

    def get_size(self):
        if self.size == 1:
            return(self.size, "Normal")

        elif self.size == 0.5:
            return(self.size, "Small")

        elif self.size == 0.25:
            return(self.size, "Tiny")

        elif self.size == 2:
            return(self.size, "Large")

        elif self.size == 4:
            return(self.size, "Huge")

        elif self.size == 6:
            return(self.size, "Gargantuan")

        else:
            raise Exception("Incorrect values for size.\
                            Accepted values are :\
                            0.25, 0.5, 1\
                            2, 4, 6")


    def get_speed(self):
        if self.mount is None:
            return self.speed
        else:
            return self.mount.speed

    def set_speed(self, speed):
        self.speed = speed

    @property
    def carryingCapacity(self):
        return self.strength*self.size*15

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

    def get_metavision(self):
        if self.metavision[0] == 0:
            return("No metavision")

        elif self.metavision[0] == 1:
            return("Darkvision", self.metavision[1], "ft")

    def set_metavision(self, metavisionTuple):
        self.metavision = metavisionTuple

    def get_encumberment(self):
        return self.encumberment

    def set_encumberment(self, encumbermentValue):
        self.encumberment = encumbermentValue

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

    def get_strength(self):
        return self.strength

    def set_strength(self, strength):
        self.strength = strength

    @property
    def carryingCapacity(self):
        return self.strength*self.size*15

    def get_size(self):
        if self.size == 1:
            return(self.size, "Normal")

        elif self.size == 0.5:
            return(self.size, "Small")

        elif self.size == 0.25:
            return(self.size, "Tiny")

        elif self.size == 2:
            return(self.size, "Large")

        elif self.size == 4:
            return(self.size, "Huge")

        elif self.size == 6:
            return(self.size, "Gargantuan")

        else:
            raise Exception("Incorrect values for size.\
                            Accepted values are :\
                            0.25, 0.5, 1\
                            2, 4, 6")

    def get_speed(self):
        return self.speed()
    
    def set_speed(self, speed):
        self.speed = speed


def convert_fpt_to_mph(fptSpeed):
    return fptSpeed/10
