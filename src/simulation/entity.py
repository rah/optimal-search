class Entity(object):
    '''
    An entity has:
      - energy
      - position(x,y)
      - size(length, width)
    An entity may have a parent entity
    An entity may have child entities
    '''

    def __init__(
            self,
            p,
            parent=None,
            children=None):
        self.p = p
        self.energy = p.getfloat("ENTITY", "energy")
        self.x_pos = p.getfloat("ENTITY", "x_pos")
        self.y_pos = p.getfloat("ENTITY", "y_pos")
        self.length = p.getint("ENTITY", "length")
        self.width = p.getint("ENTITY", "width")
        self.parent = parent
        if children is None:
            self.children = []
        else:
            self.children = children

    def add_child(self, entity):
        """
        Adds a child entity to the current entity.

        Parameters:
            entity (Any): The child entity to be added.

        Returns:
            None
        """
        self.children.append(entity)

    def remove_child(self, entity):
        """
        Remove a child entity from the list of children.

        Args:
            entity: The entity to be removed.

        Returns:
            None
        """
        self.children.remove(entity)

    def remove_self(self):
        """
        Removes the current object from its parent's list of children.

        This method is used to remove the current object from its parent's list of children. 
        It checks if the current object has a parent. 
        If it does, it removes itself from the parent's list of children.

        Parameters:
            None

        Returns:
            None
        """
        if self.parent is not None:
            self.parent.children.remove(self)

    def number_children(self):
        """
        Returns the number of children for the current object.

        Parameters:
            self (object): The current object.

        Returns:
            int: The number of children for the current object.
        """
        if self.children:
            return len(self.children)
        else:
            return 0

    def total_energy(self):
        """
        Calculate and return the total energy of the object and its children.

        Returns:
            int: The total energy of the object and its children.
        """
        total_energy = self.energy
        for child in self.children:
            total_energy += child.energy

        return total_energy

    def set_bounds(self, x, y):
        """
        Set the bounds of the object based on the given x and y coordinates.

        Parameters:
            x (float): The x-coordinate of the object.
            y (float): The y-coordinate of the object.

        Returns:
            tuple: A tuple containing the updated x and y coordinates.
        """
        if x < 0.0:
            x = self.length
        if x > self.length:
            x = 0.0

        if y < 0.0:
            y = self.width
        if y > self.width:
            y = 0.0

        return x, y
