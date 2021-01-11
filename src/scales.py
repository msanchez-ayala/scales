from typing import Optional
from typing import Tuple

from .notes import Note
from .notes import CHROMATIC_NOTES_FLATS
from .notes import CHROMATIC_NOTES_SHARPS
from .notes import FLAT_KEYS
from .notes import NATURAL_NOTES
from .notes import SHARP_KEYS


class ChromaticScale:
    """
    An ascending chromatic scale starting with any natural, single sharp, or
    single flat note. No double sharps or flats are accounted for.
    """

    def __init__(self, root: Optional[Note] = Note.C):
        """
        :param root: The root note to use for this scale.
        """
        self._root = None
        self._sharps = None
        self.root = root

    @property
    def root(self) -> Note:
        return self._root

    @root.setter
    def root(self, root: Note):
        """
        Set the root note and update sharps/flats accordingly.

        :param root: The root note to use for this scale.
        """
        self._root = root
        self.update_sharps()

    @property
    def sharps(self) -> bool:
        return self._sharps

    def update_sharps(self):
        """
        Set self._sharps based on the root note of the scale.
        Roots from sharp or flat keys can only have sharps or flats,
        respectively. C defaults to flats but can be changed by use_sharps()
        or use_flats().
        """
        if self._root in SHARP_KEYS:
            sharps = True
        elif self._root in FLAT_KEYS:
            sharps = False
        elif self._root == Note.C:
            sharps = False
        else:
            msg = f'{self._root} is either not a Note enum or is an' \
                  f' unconventional root note.'
            raise RuntimeError(msg)
        self._sharps = sharps

    def scale(self) -> Tuple[Note]:
        if self.sharps:
            return self._get_scale_with_sharps()
        return self._get_scale_with_flats()

    def use_sharps(self):
        """
        Use sharp notes only if the root is C.
        """
        if self._root != Note.C:
            return
        self._sharps = True

    def use_flats(self):
        """
        Use flat notes only if the root is C.
        """
        if self._root != Note.C:
            return
        self._sharps = False

    def _get_scale_with_sharps(self) -> Tuple[Note]:
        """
        Return a chromatic scale of only sharp variations of notes starting with
        self._root.
        """
        if self._root in FLAT_KEYS:
            msg = f'The scale root must belong to a sharp key in order to' \
                  f' produce a scale with sharp notes, not {self._root}.'
            raise RuntimeError(msg)
        notes = CHROMATIC_NOTES_SHARPS
        root_idx = notes.index(self._root)
        return notes[root_idx:] + notes[:root_idx]

    def _get_scale_with_flats(self) -> Tuple[Note]:
        """
        Return a chromatic scale of only flat variations of notes starting with
        self._root.
        """
        if self._root in SHARP_KEYS:
            msg = f'The scale root must belong to a flat key in order to' \
                  f' produce a scale with flat notes, not {self._root}.'
            raise RuntimeError(msg)
        notes = CHROMATIC_NOTES_FLATS
        root_idx = notes.index(self._root)
        return notes[root_idx:] + notes[:root_idx]
