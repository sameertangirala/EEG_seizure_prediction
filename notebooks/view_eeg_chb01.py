import matplotlib
matplotlib.use('Qt5Agg')
import mne

raw = mne.io.read_raw_edf('../data/chb01/chb01_03.edf', 
                           preload=True, verbose=False)

sz_start = 2996
sz_end = 3036
preictal_start = sz_start - 1200 # 20 mins before seizure
raw.set_annotations(mne.Annotations(
    onset=[preictal_start, sz_start, sz_end],
    duration=[1200, sz_end - sz_start, 1800], # 1800 = 30 mins of postictal data
    description=['Preictal (20 mins)', 'Seizure', 'Postictal (30 mins)']
))

raw.plot(
    duration=30,
    n_channels=23,
    scalings=dict(eeg=100e-6),
    title='chb01_03.edf eeg file (seizure 1 at 2996s)',
    show_scrollbars=True,
    block=True
)
