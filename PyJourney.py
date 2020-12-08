class Group:
    def __init__(self, members=[], travelPace=0):
        self.members = members
        self.travelPace = travelPace

    def get_members(self):
        return self.members

    def set_members(self, members):
        self.members = members

    def add_member(self, member):
        self.members.append(member)
    
    def get_group_speed(self):
        speeds = []

        for member in self.members:
            memberSpeed = convert_fpt_to_mph(member.speed)
            speeds.append(memberSpeed)
    
        return min(speeds)


class Adventurer:
    def __init__(self, name="", strength=0, size=0, speed=0, mount=None,
            passivePerception=0, hasMetavision=False, encumberment=0,
            exhaustionLevel=0):
        self.name = name
        self.strength = strength
        self.size = size
        self.speed = speed
        self.mount = mount
        self.passivePerception = passivePerception
        self.hasMetavision = hasMetavision
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
        size = ""

        if self.size == 1:
            size = "Normal"

        elif self.size == 0.5:
            size = "Small"

        elif self.size == 0.25:
            size = "Tiny"

        elif self.size == 2:
            size = "Large"

        elif self.size == 4:
            size = "Huge"

        elif self.size == 6:
            size = "Gargantuan"

        else:
            raise Exception("Incorrect values for size.\
                            Accepted values are :\
                            0.25, 0.5, 1\
                            2, 4, 6")

        return size

    def get_speed(self):
        if self.mount is None:
            return self.speed
        else:
            return self.mount.speed

    def set_speed(self, speed):
        self.speed = speed

    def get_mount(self):
        return self.mount

    def set_mount(self, mount):
        self.mount = mount
    
    def get_passive_perception(self):
        return self.passivePerception

    def set_passive_perception(self, passivePerception):
        self.passivePerception = passivePerception

    def get_has_metavision(self):
        return self.hasMetavision

    def set_has_metavision(self, metavisionValue):
        self.hasMetavision = metavisionValue

    def get_encumberment(self):
        return self.encumberment

    def set_encumberment(self, encumbermentValue):
        self.encumberment = encumbermentValue

class Mount:
    def __init__(self):
        self.name = ""
        self.strength = 0
        self.size = 0
        self.speed = 0

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_strength(self):
        return self.strength

    def set_strength(self, strength):
        self.strength = strength

    def get_size(self):
        size = ""
        if self.size == 0.25:
            size = "Tiny"

        elif self.size == 0.5:
            size = "Small"

        elif self.size == 1:
            size = "Normal"

        elif self.size == 2:
            size = "Large"

        elif self.size == 4:
            size = "Huge"

        elif self.size == 6:
            size = "Gargantuan"

        else:
            raise Exception("Incorrect values for size.\
                            Accepted values are :\
                            0.25, 0.5, 1\
                            2, 4, 6")

        return size

    def get_speed(self):
        return self.speed()
    
    def set_speed(self, speed):
        self.speed = speed


def convert_fpt_to_mph(fptSpeed):
    return fptSpeed/10


def main():
    Benelios = Adventurer(name="Benelios", size = 1)
    print(Benelios.get_speed())

if __name__ == '__main__':
    main()
