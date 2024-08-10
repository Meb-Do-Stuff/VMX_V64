# Combination Mode offsets
# ------------------------

TRACK_OFFSET = -1  # offset from the left of linked session origin; set to -1 for auto-joining of multiple instances
SCENE_OFFSET = 0  # offset from the top of linked session origin (no auto-join)

# Buttons / Pads
# -------------
# Valid Note/CC assignments are 0 to 127, or -1 for NONE
# Duplicate assignments are permitted

BUTTONCHANNEL = 0  # Channel assignment for all mapped buttons/pads; valid range is 0 to 15 ; 0=1, 1=2 etc.
MESSAGETYPE = 1  # Message type for buttons/pads; set to 0 for MIDI Notes, 1 for CCs.
# When using CCs for buttons/pads, set BUTTONCHANNEL and SLIDERCHANNEL to different values.


# Track selection box (aka that coloured box for scene/track launching)
TSB_X = 16  # Controls the vertical value for the track selection box. Default value is 8
TSB_Y = 4  # Controls the horizontal value for the track selection box. Default value is 8

# General
PLAY = 80  # Global play
STOP = 79  # Global stop
REC = 77  # Global record
DELETE = 69  # Delete selected clip
TAPTEMPO = -1  # Tap tempo
NUDGEUP = -1  # Tempo Nudge Up
NUDGEDOWN = -1  # Tempo Nudge Down
UNDO = -1  # Undo
REDO = -1  # Redo
LOOP = -1  # Loop on/off
PUNCHIN = -1  # Punch in
PUNCHOUT = -1  # Punch out
OVERDUB = -1  # Overdub on/off
METRONOME = -1  # Metronome on/off
RECQUANT = -1  # Record quantization on/off
DETAILVIEW = -1  # Detail view switch
CLIPTRACKVIEW = -1  # Clip/Track view switch

# Device Control
DEVICELOCK = -1  # Device Lock (lock "blue hand")
DEVICEONOFF = -1  # Device on/off
DEVICENAVLEFT = -1  # Device nav left
DEVICENAVRIGHT = -1  # Device nav right
DEVICEBANKNAVLEFT = -1  # Device bank nav left
DEVICEBANKNAVRIGHT = -1  # Device bank nav right
DEVICEBANK = tuple([-1] * 8)  # Device bank buttons

# Arrangement View Controls
SEEKFWD = -1  # Seek forward
SEEKRWD = -1  # Seek rewind

# Session Navigation
SESSIONLEFT = 67  # Session left
SESSIONRIGHT = 68  # Session right
SESSIONUP = 65  # Session up
SESSIONDOWN = 66  # Session down
ZOOMUP = -1  # Session Zoom up
ZOOMDOWN = -1  # Session Zoom down
ZOOMLEFT = -1  # Session Zoom left
ZOOMRIGHT = -1  # Session Zoom right

# Scene Launch
SELSCENELAUNCH = -1  # Selected scene launch
SCENELAUNCH = tuple([-1] * 4)  # Scene launch buttons

# Clip Launch / Stop
SELCLIPLAUNCH = 80  # Selected clip launch
STOPALLCLIPS = 78  # Stop all clips

# 8x8 Matrix note assignments
# Track no.:    1  2  3  4  5   6   7   8   9   10  11  12  13  14  15  16
CLIPNOTEMAP = ((1, 2, 3, 4, 17, 18, 19, 20, 33, 34, 35, 36, 49, 50, 51, 52),  # Row 1
               (5, 6, 7, 8, 21, 22, 23, 24, 37, 38, 39, 40, 53, 54, 55, 56),  # Row 2
               (9, 10, 11, 12, 25, 26, 27, 28, 41, 42, 43, 44, 57, 58, 59, 60),  # Row 3
               (13, 14, 15, 16, 29, 30, 31, 32, 45, 46, 47, 48, 61, 62, 63, 64),  # Row 4
               )

# Track Control
MASTERSEL = -1  # Master track select
SELTRACKREC = -1  # Arm Selected Track
SELTRACKSOLO = -1  # Solo Selected Track
SELTRACKMUTE = -1  # Mute Selected Track

TRACKSTOP = tuple([-1] * 16)  # Track stop buttons
TRACKSEL = tuple([-1] * 16)  # Track select buttons
TRACKMUTE = tuple([-1] * 16)  # Track mute buttons
TRACKSOLO = tuple([-1] * 16)  # Track solo buttons
TRACKREC = tuple([-1] * 16)  # Track record arm buttons

# Pad Translations for Drum Rack
PADCHANNEL = 0  # MIDI channel for Drum Rack notes
DRUM_PADS = (-1, -1, -1, -1,  # MIDI note numbers for 4 x 4 Drum Rack
             -1, -1, -1, -1,  # Mapping will be disabled if any notes are set to -1
             -1, -1, -1, -1,  # Notes will be "swallowed" if already mapped elsewhere
             -1, -1, -1, -1,
             )

# Sliders / Knobs
# ---------------
# Valid CC assignments are 0 to 127, or -1 for NONE
# Duplicate assignments will be ignored
SLIDERCHANNEL = 2  # Channel assignment for all mapped CCs; valid range is 0 to 15
TEMPO_TOP = 180.0  # Upper limit of tempo control in BPM (max is 999)
TEMPO_BOTTOM = 100.0  # Lower limit of tempo control in BPM (min is 0)

TEMPOCONTROL = -1  # Tempo control CC assignment; control range is set above
MASTERVOLUME = -1  # Master track volume
CUELEVEL = 117  # Cue level control
CROSSFADER1 = 122  # Crossfader control

TRACKVOL = (118,  # Track 1 Volume
            119,  # Track 2
            120,  # Track 3
            121,  # Track 4
            113,  # Track 5
            114,  # Track 6
            115,  # Track 7
            116,  # Track 8
            )

TRACKPAN = tuple([-1] * 16)  # Track pan controls

TRACKSENDA = (81,  # Track 1 Send A
              83,  # Track 2
              85,  # Track 3
              87,  # Track 4
              89,  # Track 5
              91,  # Track 6
              93,  # Track 7
              95,  # Track 8
              97,  # Track 9
              99,  # Track 10
              101,  # Track 11
              103,  # Track 12
              105,  # Track 13
              107,  # Track 14
              109,  # Track 15
              111,  # Track 16
              )

TRACKSENDB = (82,  # Track 1 Send B
              84,  # Track 2
              86,  # Track 3
              88,  # Track 4
              90,  # Track 5
              92,  # Track 6
              94,  # Track 7
              96,  # Track 8
              98,  # Track 9
              100,  # Track 10
              102,  # Track 11
              104,  # Track 12
              106,  # Track 13
              108,  # Track 14
              110,  # Track 15
              112,  # Track 16
              )

TRACKSENDC = tuple([-1] * 16)  # Track send C controls

PARAMCONTROL = tuple([-1] * 16)  # Device control

# Custom Menu
# ----------
MENUBUTTONS = [
    65, 66, 73, 74,
    67, 68, 75, 76,
    69, 70, 77, 78,
    71, 72, 79, 80
]
