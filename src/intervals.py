from enum import Enum


# ==============================================================================
# Intervals
# ==============================================================================


class Interval(Enum):
    Unison = 'Unison'
    MinorSecond = 'Minor Second'
    MajorSecond = 'Major Second'
    MinorThird = 'Minor Third'
    MajorThird = 'Major Third'
    PerfectFourth = 'Perfect Fourth'
    DiminishedFifth = 'Diminished Fifth'
    PerfectFifth = 'Perfect Fifth'
    MinorSixth = 'Minor Sixth'
    MajorSixth = 'Major Sixth'
    MinorSeventh = 'Minor Seventh'
    MajorSeventh = 'Major Seventh'


INTERVALS = {
    Interval.Unison: 0,
    Interval.MinorSecond: 1,
    Interval.MajorSecond: 2,
    Interval.MinorThird: 3,
    Interval.MajorThird: 4,
    Interval.PerfectFourth: 5,
    Interval.DiminishedFifth: 6,
    Interval.PerfectFifth: 7,
    Interval.MinorSixth: 8,
    Interval.MajorSixth: 9,
    Interval.MinorSeventh: 10,
    Interval.MajorSeventh: 11
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
    Triad.Major: (INTERVALS[Interval.MajorThird], INTERVALS[Interval.MinorThird]),
    Triad.Minor: (INTERVALS[Interval.MinorThird], INTERVALS[Interval.MajorThird]),
    Triad.Diminished: (INTERVALS[Interval.MinorThird], INTERVALS[Interval.MinorThird]),
    Triad.Augmented: (INTERVALS[Interval.MajorThird], INTERVALS[Interval.MajorThird])
}


# ==============================================================================
# Seventh Chords (No extensions)
# ==============================================================================


class SeventhChord(Enum):
    Major = 'Major Seventh'
    Dominant = 'Dominant Seventh'
    Minor = 'Minor Seventh'
    MinorMajor = 'Minor Major Seventh'
    HalfDiminished = 'Half Diminished Seventh'
    Diminished = 'Diminished Seventh'


SEVENTH_CHORDS = {
    SeventhChord.Major: TRIADS[Triad.Major] + (INTERVALS[Interval.MajorThird],),
    SeventhChord.Dominant: TRIADS[Triad.Major] + (INTERVALS[Interval.MinorThird],),
    SeventhChord.Minor: TRIADS[Triad.Minor] + (INTERVALS[Interval.MinorThird],),
    SeventhChord.MinorMajor: TRIADS[Triad.Minor] + (INTERVALS[Interval.MajorThird],),
    SeventhChord.HalfDiminished: TRIADS[Triad.Diminished] + (INTERVALS[Interval.MajorThird],),
    SeventhChord.Diminished: TRIADS[Triad.Diminished] + (INTERVALS[Interval.MinorThird],)
}

ALL_CHORD_INTS = {**TRIADS, **SEVENTH_CHORDS}

MAJOR_SCALE_INTS = (INTERVALS[Interval.MajorSecond],
                    INTERVALS[Interval.MajorSecond],
                    INTERVALS[Interval.MinorSecond],
                    INTERVALS[Interval.MajorSecond],
                    INTERVALS[Interval.MajorSecond],
                    INTERVALS[Interval.MajorSecond])
