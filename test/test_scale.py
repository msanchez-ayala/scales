import pytest
from unittest import mock

from src import scale
from src import notes
from src.notes import Note
from src.scale import ChromaticScale


# class TestMajorScale:
#
#     def test_A_major(self):
#         a_maj = scale.MajorScale(Note.A)
#         assert a_maj.scale() == [
#             Note.A,
#             Note.B,
#             Note.CSharp,
#             Note.D,
#             Note.E,
#             Note.FSharp,
#             Note.GSharp]


class TestChromaticScale:

    def setup(self):
        self.natural_scale = ChromaticScale()
        self.flat_scale = ChromaticScale(root=Note.F, sharps=False)
        self.sharp_scale = ChromaticScale(root=Note.G)

    def test_init(self):
        # Correct defaults
        assert self.natural_scale.root == Note.C
        assert self.natural_scale.sharps is True

        # Flats by default with a flat key root
        assert self.flat_scale.sharps is False

        # Sharps by default with a sharp key root
        assert self.sharp_scale.sharps is True

    def test_udpate_sharps(self):
        """
        Make sure update_sharps() assigns the attribute correctly based on the
        current root note.
        """
        # Natural root can have sharps or flats
        scale = ChromaticScale(root=Note.A)
        scale.update_sharps(True)
        assert scale.sharps is True
        scale.update_sharps(False)
        assert scale.sharps is False
        # Default for natural note is True
        scale.update_sharps()
        assert scale.sharps is True

        # Sharp root will always have sharps
        scale._root = Note.FSharp
        scale.update_sharps()
        assert scale.sharps is True
        scale.update_sharps(False)
        assert scale.sharps is True

        # Flat root will never have sharps
        scale._root = Note.BFlat
        scale.update_sharps()
        assert scale.sharps is False
        scale.update_sharps(True)
        assert scale.sharps is False

    def test_use_sharps_flats(self):
        """
        Make sure use_sharps() and use_flats() always set sharps correctly.
        """
        # Natural keys can be assigned either flats or sharps
        self.natural_scale.use_flats()
        assert self.natural_scale.sharps is False
        self.natural_scale.use_sharps()
        assert self.natural_scale.sharps is True

        # When root is a flat use_sharps() does nothing
        scale = ChromaticScale(root=Note.BFlat)
        scale.use_sharps()
        assert self.flat_scale.sharps is False

        # When root is a sharp use_flats() does nothing
        scale.set_root(Note.FSharp)
        self.sharp_scale.use_flats()
        assert self.sharp_scale.sharps is False

    def test__get_scale_with_sharps(self):
        """
        Make sure _get_scale_with_sharps produces the appropriate sequence of
        notes.
        """
        assert self.natural_scale._get_scale_with_sharps() == \
               notes.CHROMATIC_NOTES_SHARPS
        assert self.sharp_scale._get_scale_with_sharps() == \
               notes.CHROMATIC_NOTES_SHARPS[7:] + notes.CHROMATIC_NOTES_SHARPS[:7]
        with pytest.raises(RuntimeError):
            self.flat_scale._get_scale_with_sharps()

    def test__get_scale_with_flats(self):
        """
        Make sure _get_scale_with_flats produces the appropriate sequence of
        notes.
        """
        assert self.natural_scale._get_scale_with_flats() == \
               notes.CHROMATIC_NOTES_FLATS
        assert self.flat_scale._get_scale_with_flats() == \
               notes.CHROMATIC_NOTES_FLATS[5:] + notes.CHROMATIC_NOTES_FLATS[:5]
        with pytest.raises(RuntimeError):
            self.sharp_scale._get_scale_with_flats()

    @mock.patch('src.scale.ChromaticScale._get_scale_with_sharps')
    @mock.patch('src.scale.ChromaticScale._get_scale_with_flats')
    def test_scale(self, _get_scale_with_flats, _get_scale_with_sharps):
        """
        Make sure scale() calls the appropriate method given the root note.
        """
        self.natural_scale.scale()
        assert _get_scale_with_sharps.call_count == 1
        assert _get_scale_with_flats.call_count == 0

        _get_scale_with_sharps.reset_mock()
        self.flat_scale.scale()
        assert _get_scale_with_sharps.call_count == 0
        assert _get_scale_with_flats.call_count == 1

        _get_scale_with_flats.reset_mock()
        self.natural_scale.scale()
        assert _get_scale_with_sharps.call_count == 1
        assert _get_scale_with_flats.call_count == 0