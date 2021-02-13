import pytest

from src import main
from src.backend.notes import Note


class TestManager:

    def setup(self):
        self.manager = main.Manager()

    def test_can_init(self):
        """
        Make sure the class can initialize without errors.
        """
        assert True


class TestRootNotes:

    def setup(self):
        self.model = main.RootNotes()

    def test_init_defaults(self):
        """
        Make sure this model initializes with the correct defaults.
        """
        # C + 7 sharp keys + 7 flat keys
        assert self.model.rowCount() == 15

        first_item = self.model.item(0)
        first_note = first_item.data(main.NOTE_ROLE)
        first_note_name = first_item.data(main.NOTE_NAME_ROLE)
        assert first_note == Note.A
        assert first_note_name == 'A'


class TestKeySignatures:

    def setup(self):
        self.model = main.KeySignatures()

    def test_init_defaults(self):
        """
        Make sure this model initializes with the correct defaults.
        """
        # C + 7 sharp keys + 7 flat keys
        assert self.model.rowCount() == 15

        first_signature = self.model.item(0)
        first_note = first_signature.data(main.NOTE_ROLE)
        first_signature_name = first_signature.data(main.SIGNATUTE_NAME_ROLE)
        assert first_note == Note.C
        assert first_signature_name == '0 Flats/Sharps'
