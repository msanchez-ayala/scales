from typing import List
from typing import Union

from src import intervals
from src.notes import Note
from src.scales import ChromaticScale


NUM_NOTES = 12
AUGMENTED_CHORDS = (intervals.Triad.Augmented,)


class ChordBuilder:

    def __init__(self, root: Note):
        """
        Instantiate the object with a root and a chromatic scale. The chromatic
        scale is used to derive all chord notes.
        """
        self._root = None
        self._chromatic_scale = None
        self.root = root

    @property
    def root(self) -> Note:
        return self._root

    @root.setter
    def root(self, root: Note):
        """
        Change the builder's root note and update the chromatic scale.

        :param root: The root note to use for this scale.
        """
        self._root = root
        self._update_chromatic_scale()

    def set_root(self, root: Note):

        super().set_root(root)

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
        """
        Return the notes in the major scale associated with this builder.
        """
        scale_notes = [self._root]
        degree = 0
        chromatic_notes = self._chromatic_scale.scale()
        for interval in intervals.MAJOR_SCALE_INTS:
            degree = (degree + interval) % NUM_NOTES
            scale_notes.append(chromatic_notes[degree])
        return scale_notes

    def build_chord(self,
                    chord_quality: Union[
                        intervals.Triad, intervals.SeventhChord]
                    ) -> List[Note]:
        """
        Return the notes in a chord of `chord_quality` built on the root of
        this builder.

        :param chord_quality: The quality of chord to build.
        """
        chord_notes = [self._root]
        reset_sharps = False
        if chord_quality in AUGMENTED_CHORDS and self.root == Note.C:
            self._chromatic_scale.use_sharps()
            reset_sharps = True
        chromatic_notes = self._chromatic_scale.scale()
        for interval in intervals.ALL_CHORD_INTS[chord_quality]:
            chord_notes.append(chromatic_notes[interval])
        if reset_sharps:
            self._update_chromatic_scale()
        return chord_notes
