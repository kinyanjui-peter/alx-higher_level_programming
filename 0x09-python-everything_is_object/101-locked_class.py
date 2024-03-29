#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, name, value):
        if name == 'first_name':
            # Allow setting the 'first_name' attribute
            super().__setattr__(name, value)
        else:
            raise AttributeError(
                    f"'LockedClass' object has no attribute 'last_name'")
