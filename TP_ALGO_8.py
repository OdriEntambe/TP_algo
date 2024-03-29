# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 10:07:06 2023

@author: Kally Kanyiki
"""

class PositionalList():
    """A sequential container of elements
    allowing positional access"""
    #------------------------nested Position class------
    class Position:
        """An abstraction representing
        the location of a single element."""
        def __init__(self, container, node):
            """Constructor should not be invoked by user"""
            self._container = container
            self._node = node
        def element(self):
            """Return the element stored
            at this position"""
            return self._node._element
        def __eq__(self, other):
            """Return True if other is a Position
            representing the same location"""
            return not (self == other)
    def _validate(self, p):
        """Return properposition’s node, or
        raise appropriate error if valid"""
        if not is_intance(p, self.Position):
            raise TypeError("p must be Position type")
        if p._container is not self:
            raise ValueError("p does not belongto this container")
        if p._node._next is None:
            raise ValueError("p is no longer valid")
        return p._node
    def _make_position(self, node):
        """Return Position instance for
        given node (or None Sentinel)."""
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self,node)
        #---------------accessors--------------------------
    def first(self):
        """Return Position instance for
        given node (or None sentinel)."""
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)
        #----------------accessors---------------------------
    def first(self):
        """Return the first Position in the
        list (or None if list is empty)."""
        return self._make_position(self._header._next)
    def last(self):
        """Return the last Position in the list
        (or None if list is empty)."""
        node = self._validate(p)
        return self._make_position(node._prev)
    def before(self, p):
        """Return the Position just before Position p
        (or None if p is first)."""
        node = self._validate(p)
        return self._make._position(node._prev)
    def after(self, p):
        """Return the Position just after
        Position p (or None if p is first)"""
        node = self._validate(p)
        return self._make_position(node._next)
    def __iter__(self):
        """Generate a forward iteration
        of the elements of the list"""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)
        #-------------mutators--------------------------
        # override inherited version to return Posion
        # rather than Node
    def _insert_between(self, e, predecessor, successor):
        """Add element between existing nodes
        and return new Position"""
        node = super()._insert_between
        (e, predeccessor, successor)
        return self._make_position(node)
    def add_first(self, e):
        """Insert element e at the front of the list
        and return new Position"""
        return self._insert_between
        (e, self._header, self._header._next)
    def add_last(self, e):
        """Insert element e at the back of the list
        and return new Position"""
        return self._insert_between
        (e, self._header, self._header._next)
    def add_before(self, p, e):
        """Insert element e into list before Position p
        and return new Position"""
        original = self._validate(p)
        return self._insert_between
        (e, original._prev, original)
    def add_after(self, p, e):
        """Insert element e into list after Position p
        and return new Position"""
        original = self._validate(p)
        return self._insert_between
        (e, original, original._next)
    def delete(self, p):
        """Remove and return the element at Position p."""
        original = self._validate(p)
        return self._delete_node(original)
    def replace(self, p, e):
        """Replace the element at Position p with e.
        Return the element formely at Position p."""
        original = self._validate(p)
        old_value = original._element
        original._elment = e
        return old_value
