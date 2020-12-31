from enum import Enum
from typing import List

from src import intervals
from src.notes import Note
from src.scales import NoteCollection
from src.scales import ChromaticScale


NUM_NOTES = 12


class ChordBuilder(NoteCollection):

    def __init__(self, root: Note):
        """
        Instantiate the object with a root and a chromatic scale. The chromatic
        scale is used to derive all chord notes.
        """
        super().__init__(root)
        self._chromatic_scale = None
        self._update_chromatic_scale()

    def set_root(self, root: Note):
        """
        Extends NoteCollection's set_root() to update the chromatic scale any time
        the root is changed.

        :param root: The root note to use for this scale.
        """
        super().set_root(root)
        self._update_chromatic_scale()

    @property
    def chromatic_scale(self) -> ChromaticScale:
        return self._chromatic_scale

    def _update_chromatic_scale(self):
        """
        Update self._chromatic_scale with the current root. Called any time
        the root is changed.
        """
        self._chromatic_scale = ChromaticScale(root=self._root)

    def major_scale(self) -> List[Note]:
        scale_notes = [self._root]
        degree = 0
        chromatic_notes = self._chromatic_scale.scale()
        for interval in intervals.MAJOR_SCALE_INTS:
            degree = (degree + interval) % NUM_NOTES
            scale_notes.append(chromatic_notes[degree])
        return scale_notes

    def build_chord(self, chord_quality: Enum) -> List[Note]:
        chord_notes = [self._root]
        degree = 0
        chromatic_notes = self._chromatic_scale.scale()
        for interval in intervals.ALL_CHORD_INTS[chord_quality]:
            degree += interval
            chord_notes.append(chromatic_notes[degree])
        return chord_notes
