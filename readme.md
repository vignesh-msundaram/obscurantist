# The Obscurantist
> Obscurantism: Deliberate obscurity or vagueness.

The Obscurantist is a Python class that makes its attributes... obscure. It hides private information and transform the public information in such a way that the person using it might be mistaken into thinking it actually works as expected (but it does not).

It's characteristics are:

* Hides private attributes as if they did not exist
* Divide by 2 all of its numeric attributes
* Randomly removes elements from its attributes when they are iterable
* Has a `reveal` method to know the true, non modified value of an argument by name
* Randomly inserts `don't` before the verbs `know`/ `have`/`see` when attributes are string
* Randomly select a date between 2 and 4 days before when attributes are dates or datetimes
* Randomly returns the opposite when an attribute is `True`/ `False`
* To hide its track, regular ways to get the attributes through `dir`or `__dict__` should also follow that behaviour, and act otherwise completely normally
* Consistency: calling several times the same method should return the same value. The obscurantist does not always return the right value but it does not change its mind.
* It should be inheritable, which means that methods should work as expected (well, apart from the fact that the attributes used in them will have wrong values)

Demonstration of what is expected:

    >>> mystery = Obscurantist()
    >>> mystery._gold = 10000
    AttributeError: 'Obscurantist' has no attribute '_gold'

    >>> mystery.shoes = 2
    >>> mystery.shoes
    1
    >>> mystery.reveal('shoes)
    2

    >>> dir(mystery)
    ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', 
    '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', 
    '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
    'shoes']
    >>> mystery.__dict__
    {'shoes': 1}

    >>> mystery.friends = ['Tony', 'Johnny', 'Billy']
    >>> mystery.friends
    ['Tony']

    >>> mystery.last_time_saw_that_knife = datetime.date(year=2017, month=3, day=4)
    >>> mystery.last_time_saw_that_knife
    datetime.date(2017, 3, 4)

    >>> mystery.last_words = 'I have a very good friend in Rome'
    >>> mystery.last_words
    "I don't have a very good friend in Rome"

    >>> mystery.is_trustful = False
    >>> mystery.is_trustful
    True


## Source code

* This project is written using Python 3.5 leveraging the concepts of meta-programming.
* The source code for the Obscurantist class can be found in src/code.py.
* Unit tests to meet the requirements specified above can be found in src/tests.py
