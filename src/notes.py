import enum


class Note(enum.Enum):
    C = 'C'
    CSharp = 'C♯'
    DFlat = 'D♭'
    D = 'D'
    DSharp = 'D♯'
    EFlat = 'E♭'
    E = 'E'
    ESharp = 'E♭'
    FFlat = 'F♭'
    F = 'F'
    FSharp = 'F♯'
    GFlat = 'G♭'
    G = 'G'
    GSharp = 'G♯'
    AFlat = 'A♭'
    A = 'A'
    ASharp = 'A♯'
    BFlat = 'B♭'
    B = 'B'
    BSharp = 'B♯'
    CFlat = 'C♭'


CHROMATIC_NOTES_SHARPS = (
    Note.C,
    Note.CSharp,
    Note.D,
    Note.DSharp,
    Note.E,
    Note.F,
    Note.FSharp,
    Note.G,
    Note.GSharp,
    Note.A,
    Note.ASharp,
    Note.B
)
CHROMATIC_NOTES_FLATS = (
    Note.C,
    Note.DFlat,
    Note.D,
    Note.EFlat,
    Note.E,
    Note.F,
    Note.GFlat,
    Note.G,
    Note.AFlat,
    Note.A,
    Note.BFlat,
    Note.B
)
SHARP_KEYS = set((
    Note.G,
    Note.D,
    Note.A,
    Note.E,
    Note.B,
    Note.FSharp,
    Note.CSharp
))
FLAT_KEYS = set((
    Note.F,
    Note.BFlat,
    Note.EFlat,
    Note.AFlat,
    Note.DFlat,
    Note.GFlat,
    Note.CFlat
))
NATURAL_NOTES = set((
    Note.A,
    Note.B,
    Note.C,
    Note.D,
    Note.E,
    Note.F,
    Note.G
))