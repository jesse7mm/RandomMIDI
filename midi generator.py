from midiutil.MidiFile import MIDIFile
import random

# Create a MIDIFile object
midi_file = MIDIFile(1)  # One track

# Add track name and tempo
track = 0
time = 0
midi_file.addTrackName(track, time, "Sample Track")
midi_file.addTempo(track, time, 120)  # Tempo in BPM

# Generate random notes and add them to the MIDI file
for i in range(0, 100):  # Change the range to generate desired number of notes
    pitch = random.randint(40, 90)  # Random MIDI note (adjust range as needed)
    duration = random.uniform(0.1, 2.0)  # Random duration in seconds

    # Add note to MIDI file (track, channel, pitch, time, duration, volume)
    midi_file.addNote(
        track,
        0,  # MIDI channel (0-15)
        pitch,
        time,
        duration,
        random.randint(50, 100)  # Random velocity
    )

    # Increment time for the next note
    time += duration  # Use duration for incremental time

# Save the generated MIDI data to a file
with open("random_notes.mid", "wb") as output_file:
    midi_file.writeFile(output_file)
