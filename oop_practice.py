# Creating an empty class
class Competitor:
    pass


conor = Competitor()
conor.name = "Conor McGregor"
conor.age = 29
conor.weight = 155

print(conor.__dict__)

nate = Competitor()
nate.name = "Nate Diaz"
nate.age = 30
nate.weight = 170

print(nate.__dict__)


def print_competitor_age(object):
    print(f"{object.name} is {object.age} years old.")


print_competitor_age(conor)
print_competitor_age(nate)


# Using Inheritance
class UFC:
    def weight_class(self, weight):
        classes = {
            155: "Lightweight",
            170: "Welterweight"
        }
        return classes[weight]


class Competitor(UFC):
    pass


conor = Competitor()
conor.name = "Conor McGregor"
conor.age = 29
conor.weight = 155

print(conor.__dict__)

nate = Competitor()
nate.name = "Nate Diaz"
nate.age = 30
nate.weight = 170

print(nate.__dict__)

print(f"{conor.name} is in the {conor.weight_class(conor.weight)} weight class.")
print(f"{nate.name} is in the {nate.weight_class(nate.weight)} weight class.")


# Using Multiple Inheritance
class MMA:
    def org(self, org_name):
        orgs = {"UFC": "Ultimate Fighting Championship",
                "Bellator": "MMA promotion in Santa Monica, California."}
        return orgs[org_name]


class CompetitorAll(UFC, MMA):
    pass


gsp = CompetitorAll()
gsp.name = "Georges St-Pierre"
gsp.age = 27
gsp.weight = 170

print(f"{gsp.name} is in the {gsp.weight_class(gsp.weight)} weight class and fights in the {gsp.org('UFC')}. {gsp.name} is the G.O.A.T.")


# Special Class Method: __len__
class JonJones:
    def __len__(self):
        return 84


jon_jones = JonJones()
print(len(jon_jones))


# @property (read-only attribute)
class JonJonesProperty:

    @property
    def reach(self):
        return 84


jon_jones = JonJonesProperty()
print(jon_jones.reach)
jon_jones.length = 85
print(jon_jones.length)


# @staticmethod (no self needed)
class JonJonesStatic:
    @staticmethod
    def reach():
        return 84


jon_jones = JonJonesStatic()
print(jon_jones.reach())


# Immutability with @property
class Foo:
    @property
    def unbreakable(self):
        return "David"


foo = Foo()
print(foo.unbreakable)

foo.not_unbreakable = "Elijah2"
print(foo.__dict__)
