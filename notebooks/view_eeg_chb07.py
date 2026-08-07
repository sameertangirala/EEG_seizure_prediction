import matplotlib
matplotlib.use('Qt5Agg')
import mne

raw = mne.io.read_raw_edf('../data/chb01/chb01_07.edf', 
                           preload=True, verbose=False)

raw.plot(
    duration=30,
    n_channels=23,
    scalings=dict(eeg=100e-6),
    title='chb01_73.edf eeg file (no seizures)',
    show_scrollbars=True,
    block=True
)
