import random
from datetime import datetime, date, timedelta


class ObscureBaseMeta(type):
    """ Meta class that abstracts away certain attributes, and adds new attributes to the class instances.
        Attributes manipulated by this meta class include:
            '_excluded_dir_fields' : A list containing the fields that would be excluded when calling the __dir__() on
                an instance.
            '_private_attributes' : A dictionary containing the attributes with their original values. The original
                values are shown via the reveal() method defined in the class that inherits this meta class.
    """

    _excluded_dir_fields = ['__getattr__', '__dir__',
                            '__eq__', '__ge__', '__gt__', '__le__', '__lt__', '__ne__',
                            '_excluded_methods', '_excluded_dir_fields', '_private_attributes']

    def __new__(mcs, name, bases, clsdict):
        """ Create a new instance of the meta class. Propagate the '_excluded_dir_fields' attribute to this new instance
            and all the class that would inherit the instance. Also, declare and initialize '_private_attributes' to be
            an empty dictionary
        """
        clsobj = super().__new__(mcs, name, bases, clsdict)
        setattr(clsobj, '_excluded_dir_fields', mcs._excluded_dir_fields)
        setattr(clsobj, '_private_attributes', {})
        return clsobj


class ObscureBase(metaclass=ObscureBaseMeta):
    """ A base class that extends the meta class ObscureBaseMeta. The purpose of this base class is to specify how the
        following methods should behave::
        1. __dir__() : This method would be subsequently called by this class and any class that inherits this base
            class. The __dir__() function should mask all the fields and methods that have been marked to be
            excluded.
        2. reveal : This method specifies how the private attributes should be revealed.
        3. set_private : This method adds an attribute and its original, aka private value as a key-value pair in the
            '_private_attributes' dictionary attribute.
        4. set_public : This method adds the attribute and its public value into the '__dict__' attribute of the
            instance.
    """
    _excluded_methods = ['reveal', 'set_private', 'set_public']

    def __dir__(self):
        """ Exclude specified attributes from the parent's __dir__ attributes."""
        return [field for field in super().__dir__() if field not in
                getattr(self, '_excluded_dir_fields', []) + self.__class__._excluded_methods]

    def reveal(self, attribute):
        """ Retrieve the original / private value of the attribute from the '_private_attributes' dictionary
            attribute."""
        return getattr(self, '_private_attributes', {}).get('_{0}'.format(attribute), None)

    def set_private(self, attribute, private_value):
        """ Add the original /private value of the attribute into the '_private_attributes' dictionary
            attribute."""
        getattr(self, '_private_attributes', {})['_{0}'.format(attribute)] = private_value

    def set_public(self, attribute, public_value):
        """ Add the public value of the attribute into the '__dict__' attribute."""
        self.__dict__[attribute] = public_value


class Obscurantist(ObscureBase):
    """ A class that obscures attribute values based on their types. An instance of this class stores both the
        original and obscured copies of its attributes. The original values are stored to be later revealed whenever
        the 'reveal' method is called. The obscured values are stored for data integrity and consistency.
    """

    def __setattr__(self, key, value):
        """ Set obscured values based on the attribute types:
            String : If the attribute contains "have", "know", or "see" in its value, prefix them with "don't".
                The attribute can have multiple occurrences of "have", "know", and "see" in its value. Therefore,
                the prefix should work for all those occurrences.
            Numeric : Can be int, float, decimal, etc. The obscured version is half the original version.
            List : The obscured version is a randomly chosen version from this list.
            Date / Datetime : The obscured value has the day offset of 2-4 (randomly chosen) days prior to the that of
                the original value.
            Boolean : The obscured value is a negation of the original value.
        """
        if key.startswith('_'):
            raise AttributeError("""'{0}' has no attribute '{1}'""".format(self.__class__, key))
        private, public = value, value
        if isinstance(value, bool):
            public = not value
        elif isinstance(value, (int, float)):
            public = value / 2
        elif isinstance(value, str):
            if "have" in value:
                public = value.replace("have", "don't have")
            if "know" in value:
                public = value.replace("know", "don't know")
            if "see" in value:
                public = value.replace("see", "don't see")
        elif isinstance(value, list):
            public = random.choice(value)
        elif isinstance(value, (datetime, date)):
            public = value - timedelta(days=random.randint(2, 4))
        self.set_private(key, private)
        self.set_public(key, public)
