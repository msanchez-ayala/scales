import pytest
from unittest import mock

from src import notes
from src.notes import Note
from src.scales import ChromaticScale
from src.scales import MajorScale


class TestChromaticScale:

    def setup(self):
        self.c_scale = ChromaticScale(root=Note.C)
        self.flat_scale = ChromaticScale(root=Note.F)
        self.sharp_scale = ChromaticScale(root=Note.G)

    def test_init(self):
        # C uses sharps by default
        assert self.c_scale.sharps is False

        # Flats by default with a flat key root
        assert self.flat_scale.sharps is False

        # Sharps by default with a sharp key root
        assert self.sharp_scale.sharps is True

    def test_udpate_sharps(self):
        """
        Make sure update_sharps() assigns the attribute correctly based on the
        current root note.
        """
        scale = self.c_scale

        # Sharp root will always have sharps
        scale._root = Note.FSharp
        scale.update_sharps()
        assert scale.sharps is True

        # Flat root will never have sharps
        scale._root = Note.BFlat
        scale.update_sharps()
        assert scale.sharps is False

        # C root is sharp by default
        scale._root = Note.C
        scale.update_sharps()
        assert scale.sharps is False

    def test_use_sharps_flats(self):
        """
        Make sure calling use_sharps() or use_flats() does nothing except for
        when the root note is C.
        """
        scale = self.c_scale
        scale.use_sharps()
        assert scale.sharps
        scale.use_flats()
        assert not scale.sharps

        for root in notes.USED_KEYS:
            if root == Note.C:
                continue
            scale.root = root
            sharps = scale.sharps
            scale.use_sharps()
            assert scale.sharps == sharps
            scale.use_flats()
            assert scale.sharps == sharps

    def test__get_scale_with_sharps(self):
        """
        Make sure _get_scale_with_sharps produces the appropriate sequence of
        notes.
        """
        assert self.c_scale._get_scale_with_sharps() == \
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
        assert self.c_scale._get_scale_with_flats() == \
               notes.CHROMATIC_NOTES_FLATS
        assert self.flat_scale._get_scale_with_flats() == \
               notes.CHROMATIC_NOTES_FLATS[5:] + notes.CHROMATIC_NOTES_FLATS[:5]
        with pytest.raises(RuntimeError):
            self.sharp_scale._get_scale_with_flats()

    @mock.patch('src.scales.ChromaticScale._get_scale_with_sharps')
    @mock.patch('src.scales.ChromaticScale._get_scale_with_flats')
    def test_scale(self, _get_scale_with_flats, _get_scale_with_sharps):
        """
        Make sure scale() calls the appropriate method given the root note.
        """
        self.c_scale.scale()
        assert _get_scale_with_sharps.call_count == 0
        assert _get_scale_with_flats.call_count == 1

        _get_scale_with_flats.reset_mock()
        self.flat_scale.scale()
        assert _get_scale_with_sharps.call_count == 0
        assert _get_scale_with_flats.call_count == 1

        _get_scale_with_flats.reset_mock()
        self.sharp_scale.scale()
        assert _get_scale_with_sharps.call_count == 1
        assert _get_scale_with_flats.call_count == 0


class TestMajorScale:

    def setup(self):
        self.c_scale = MajorScale()
        self.flat_scale = MajorScale(Note.F)
        self.sharp_scale = MajorScale(Note.G)

    def test_init(self):
        assert self.c_scale.root is Note.C
        assert self.flat_scale.root is Note.F
        assert self.sharp_scale.root is Note.G

    def test__update_scale(self):
        scale = self.c_scale
        scale._root = Note.A
        scale._update_scale()
        assert scale._chromatic_scale.root is Note.A
        assert scale.scale() == [
        Note.A, Note.B, Note.CSharp, Note.D, Note.E, Note.FSharp, Note.GSharp
        ]
