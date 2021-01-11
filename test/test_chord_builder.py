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

        builder.root = Note.C
        assert builder.major_scale() == [
            Note.C,
            Note.D,
            Note.E,
            Note.F,
            Note.G,
            Note.A,
            Note.B
        ]

        builder.root = Note.EFlat
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
        assert c_aug_triad == [Note.C, Note.E, Note.GSharp]

        c_maj_7 = builder.build_chord(SeventhChord.Major)
        assert c_maj_7 == [Note.C, Note.E, Note.G, Note.B]

        c_dom_7 = builder.build_chord(SeventhChord.Dominant)
        assert c_dom_7 == [Note.C, Note.E, Note.G, Note.BFlat]

        c_min_7 = builder.build_chord(SeventhChord.Minor)
        assert c_min_7 == [Note.C, Note.EFlat, Note.G, Note.BFlat]

        c_half_dim_7 = builder.build_chord(SeventhChord.HalfDiminished)
        assert c_half_dim_7 == [Note.C, Note.EFlat, Note.GFlat, Note.BFlat]

        c_dim_7 = builder.build_chord(SeventhChord.Diminished)
        assert c_dim_7 == [Note.C, Note.EFlat, Note.GFlat, Note.A]