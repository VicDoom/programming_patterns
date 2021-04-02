from abc import ABC, abstractmethod
class AbstractFactory:

    @abstractmethod
    def create_engineer(self):
        pass

    @abstractmethod
    def create_scout(self):
        pass

    @abstractmethod
    def create_infantry(self):
        pass

class AlliedFactory(AbstractFactory):

    def create_engineer(self):
        return AlliedEngineer()

    def create_scout(self):
        return AlliedScout()

    def create_infantry(self):
        return AlliedInfantry()

class SovietFactory(AbstractFactory):

    def create_engineer(self):
        return SovietEngineer()

    def create_scout(self):
        return SovietScout()

    def create_infantry(self):
        return SovietInfantry()

class ImperialFactory(AbstractFactory):

    def create_engineer(self):
        return ImperialEngineer()

    def create_scout(self):
        return ImperialScout()

    def create_infantry(self):
        return ImperialInfantry()

# creating all engineers
class AbstractEngineer(ABC):

    @abstractmethod
    def intro_line(self):
        pass

    @abstractmethod
    def fix_line(self):
        pass

class AlliedEngineer(AbstractEngineer):

    def intro_line(self):
        return "On time, as always!"

    def fix_line(self):
        return "I can fix it!"

class SovietEngineer(AbstractEngineer):

    def intro_line(self):
        return "You need engineer?"

    def fix_line(self):
        return "I've seen worse, you know!"

class ImperialEngineer(AbstractEngineer):

    def intro_line(self):
        return "You called, your Eminence?"

    def fix_line(self):
        return "I will fix it with your blessing!"

# creating all Scouts
class AbstractScout(ABC):

    @abstractmethod
    def intro_line(self):
        pass

class AlliedScout(AbstractScout):

    def intro_line(self):
        return "Woof!"

class SovietScout(AbstractScout):

    def intro_line(self):
        return "Grrrrrr!..."

class ImperialScout(AbstractScout):

    def intro_line(self):
        return "Vzhuh!"

# create all infantries
class AbstractInfantry(ABC):

    @abstractmethod
    def intro_line(self):
        pass

    @abstractmethod
    def fight_line(self, collaborator):
        pass

class AlliedInfantry(AbstractInfantry):

    def intro_line(self):
        return "Ready sir, where's the trouble?"

    def fight_line(self, collaborator):
        if isinstance(collaborator, AlliedScout) \
                or isinstance(collaborator, AlliedEngineer) \
                or isinstance(collaborator, AlliedInfantry):
            return f"Ready for the contact, {collaborator}!"
        else:
            return f"Thats {collaborator}! Take 'em down!"

class SovietInfantry(AbstractInfantry):

    def intro_line(self):
        return "Ready to fight for Union!"

    def fight_line(self, collaborator):
        if isinstance(collaborator, SovietInfantry) or isinstance(collaborator, SovietEngineer):
            return "Thats my comrade!"
        elif isinstance(collaborator, SovietScout):
            return "You know, you are awfully moody for bear"
        else:
            return f"For Mother Russia!"

class ImperialInfantry(AbstractInfantry):

    def intro_line(self):
        return "I serve the Emperor!"

    def fight_line(self, collaborator):
        if isinstance(collaborator, ImperialEngineer) \
            or isinstance(collaborator, ImperialInfantry) \
            or isinstance(collaborator, ImperialScout):
            return "It belongs to us!"
        else:
            return f"The Emperor has spoken! Bow before us, {collaborator}!"


def client_code(factory: AbstractFactory):
    scout = factory.create_scout()
    print(f"Scout was created: {scout.intro_line()}\n")

    engineer = factory.create_engineer()
    print(f"Engineer was created: {engineer.intro_line()}")
    print(f"Infantry fix line: {engineer.fix_line()}\n")

    infantry = factory.create_infantry()
    print(f"Infantry was created: {infantry.intro_line()}")
    print(f"Infantry fight line: {infantry.fight_line(scout)}\n")
    some_other_character = AlliedFactory().create_infantry()
    print(f"Infantry fight line: {infantry.fight_line(some_other_character)}\n")


if __name__ == "__main__":
    print("Comrades! Let's create the perfect army for our motherland\n")
    client_code(SovietFactory())