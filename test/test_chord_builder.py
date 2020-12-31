from src import chord_builder
from src.intervals import Triad
from src.intervals import SeventhChord
from src.notes import Note


class TestChordBuilder:

    def test_major_scale(self):
        """
        Make sure correct accidentals are returned for the major scale
        based on the root note.
        """
        builder = chord_builder.ChordBuilder(Note.A)
        assert builder.major_scale() == [
            Note.A,
            Note.B,
            Note.CSharp,
            Note.D,
            Note.E,
            Note.FSharp,
            Note.GSharp]

        builder.set_root(Note.C)
        assert builder.major_scale() == [
            Note.C,
            Note.D,
            Note.E,
            Note.F,
            Note.G,
            Note.A,
            Note.B
        ]

        builder.set_root(Note.EFlat)
        assert builder.major_scale() == [
            Note.EFlat,
            Note.F,
            Note.G,
            Note.AFlat,
            Note.BFlat,
            Note.C,
            Note.D
        ]

    def test_build_chord(self):
        """
        Make sure chords are constructed with appropriate accidentals based on
        root note and chord quality.
        """
        builder = chord_builder.ChordBuilder(Note.C)
        c_maj_triad = builder.build_chord(Triad.Major)
        assert c_maj_triad == [Note.C, Note.E, Note.G]

        c_min_triad = builder.build_chord(Triad.Minor)
        assert c_min_triad == [Note.C, Note.EFlat, Note.G]

        c_dim_triad = builder.build_chord(Triad.Diminished)
        assert c_dim_triad == [Note.C, Note.EFlat, Note.GFlat]

        c_aug_triad = builder.build_chord(Triad.Augmented)
        assert c_aug_triad == [Note.C, Note.ESharp, Note.GSharp]