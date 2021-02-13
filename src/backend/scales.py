from typing import Optional
from typing import Tuple
from typing import List
from typing import Any

from . import intervals
from .notes import Note
from .notes import CHROMATIC_NOTES_FLATS
from .notes import CHROMATIC_NOTES_SHARPS
from .notes import ROOT_ACCIDENTALS_MAP
from .notes import FLAT_KEYS
from .notes import SHARP_KEYS


def replace_list_item(input_list: List, item_1: Any, item_2: Any):
    """
    Replace `item_1` with `item_2` in `input_list` in-place.

    :raise ValueError: if item_1 doesn't exist in the list.
    """
    idx = input_list.index(item_1)
    input_list[idx] = item_2


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

    @property
    def notes(self) -> Tuple[Note]:
        if self.sharps:
            return self._get_scale_notes_sharps()
        return self._get_scale_notes_flats()

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

    def _get_scale_notes_sharps(self) -> Tuple[Note]:
        """
        Return the notes of a chromatic scale of only sharp variations of notes
        starting with self._root.
        """
        if self._root in FLAT_KEYS:
            msg = f'The scale root must belong to a sharp key in order to' \
                  f' produce a scale with sharp notes, not {self._root}.'
            raise RuntimeError(msg)
        chr_notes = list(CHROMATIC_NOTES_SHARPS)
        num_sharps = ROOT_ACCIDENTALS_MAP[self._root]
        if num_sharps > 5:
            replace_list_item(chr_notes, Note.F, Note.ESharp)
        if num_sharps == 7:
            replace_list_item(chr_notes, Note.C, Note.BSharp)
        root_idx = chr_notes.index(self._root)
        return tuple(chr_notes[root_idx:] + chr_notes[:root_idx])

    def _get_scale_notes_flats(self) -> Tuple[Note]:
        """
        Return the notes of a chromatic scale of only flat variations of notes
        starting with self._root.
        """
        if self._root in SHARP_KEYS:
            msg = f'The scale root must belong to a flat key in order to' \
                  f' produce a scale with flat notes, not {self._root}.'
            raise RuntimeError(msg)
        chr_notes = list(CHROMATIC_NOTES_FLATS)
        num_flats = ROOT_ACCIDENTALS_MAP[self._root]
        if num_flats > 5:
            replace_list_item(chr_notes, Note.B, Note.CFlat)
        if num_flats == 7:
            replace_list_item(chr_notes, Note.E, Note.FFlat)
        root_idx = chr_notes.index(self._root)
        return tuple(chr_notes[root_idx:] + chr_notes[:root_idx])


class MajorScale:

    def __init__(self, root: Optional[Note] = Note.C):
        self._root = None
        self._chromatic_scale = None
        self._notes = None
        self.root = root

    @property
    def root(self) -> Note:
        return self._root

    @root.setter
    def root(self, root: Note):
        self._root = root
        self._update_scale()

    @property
    def notes(self) -> Optional[Tuple[Note]]:
        """
        Return a list of notes in the currect major scale. None if no root is
        set.
        """
        return self._notes

    def _update_scale(self):
        """
        Update the chromatic and major scale based on the current root note.
        """
        if not self.root:
            self._chromatic_scale = None
            self._notes = None
            return
        self._chromatic_scale = ChromaticScale(self.root)
        scale_notes = [self._root]
        chromatic_notes = self._chromatic_scale.notes
        current_int = 0
        for interval in intervals.MAJOR_SCALE_INTS:
            current_int += interval
            scale_notes.append(chromatic_notes[current_int])
        self._notes = tuple(scale_notes)

