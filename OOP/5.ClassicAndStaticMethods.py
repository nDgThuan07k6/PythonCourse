class Robot:
    active_count = 0
    def __init__(self, name):
        self.name = name
        Robot.active_count += 1
        print(f'Robot {self.name} has been activated')

    def remove(self):
        """Deactivating robot"""
        if Robot.active_count > 0:
            Robot.active_count -= 1
            print(f'Robot {self.name} has been turned off')
        else:
            print(f'There is no robot to deactivate')

    # Call class methods and cls in order to print number activating
    @classmethod
    def number_active(cls):
        """Print activating robot"""
        if cls.active_count <= 1:
            print(f'There is {cls.active_count} robot activating')
        else:
            print(f'There are {cls.active_count} robots activating')

r1 = Robot("Alpha")
r2 = Robot("Beta")
Robot.number_active()
r1.remove()
Robot.number_active()