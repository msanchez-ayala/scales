from enum import Enum


# ==============================================================================
# Intervals
# ==============================================================================


class Interval(Enum):
    Unison = 'Unison'
    m2 = 'Minor Second'
    M2 = 'Major Second'
    m3 = 'Minor Third'
    M3 = 'Major Third'
    P4 = 'Perfect Fourth'
    d5 = 'Diminished Fifth'
    P5 = 'Perfect Fifth'
    m6 = 'Minor Sixth'
    M6 = 'Major Sixth'
    m7 = 'Minor Seventh'
    M7 = 'Major Seventh'


INTERVALS = {
    Interval.Unison: 0,
    Interval.m2: 1,
    Interval.M2: 2,
    Interval.m3: 3,
    Interval.M3: 4,
    Interval.P4: 5,
    Interval.d5: 6,
    Interval.P5: 7,
    Interval.m6: 8,
    Interval.M6: 9,
    Interval.m7: 10,
    Interval.M7: 11
}


# ==============================================================================
# Triads
# ==============================================================================


class Triad(Enum):
    Major = 'Major Triad'
    Minor = 'Minor Triad'
    Diminished = 'Diminished Triad'
    Augmented = 'Augmented Triad'


TRIADS = {
    Triad.Major: (INTERVALS[Interval.M3], INTERVALS[Interval.P5]),
    Triad.Minor: (INTERVALS[Interval.m3], INTERVALS[Interval.P5]),
    Triad.Diminished: (INTERVALS[Interval.m3], INTERVALS[Interval.d5]),
    Triad.Augmented: (INTERVALS[Interval.M3], INTERVALS[Interval.m6])
}


# ==============================================================================
# 7 Chords (No extensions)
# ==============================================================================


class SeventhChord(Enum):
    Major = 'Major 7'
    Dominant = 'Dominant 7'
    Minor = 'Minor 7'
    MinorMajor = 'Minor Major 7'
    HalfDiminished = 'Half Diminished 7'
    Diminished = 'Diminished 7'


SEVENTH_CHORDS = {
    SeventhChord.Major: (*TRIADS[Triad.Major], INTERVALS[Interval.M7]),
    SeventhChord.Dominant: (*TRIADS[Triad.Major], INTERVALS[Interval.m7]),
    SeventhChord.Minor: (*TRIADS[Triad.Minor], INTERVALS[Interval.m7]),
    SeventhChord.MinorMajor: (*TRIADS[Triad.Minor], INTERVALS[Interval.M7]),
    SeventhChord.HalfDiminished: (*TRIADS[Triad.Diminished], INTERVALS[Interval.m7]),
    SeventhChord.Diminished: (*TRIADS[Triad.Diminished], INTERVALS[Interval.M6])
}

ALL_CHORD_INTS = {**TRIADS, **SEVENTH_CHORDS}

MAJOR_SCALE_INTS = (INTERVALS[Interval.M2],
                    INTERVALS[Interval.M2],
                    INTERVALS[Interval.m2],
                    INTERVALS[Interval.M2],
                    INTERVALS[Interval.M2],
                    INTERVALS[Interval.M2])
