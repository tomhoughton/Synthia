
class DataFrameConfig:
    def __init__(self) -> None:
        self.signalChain = [
            'LFOSpeed',
            'LFOPhase',
            'LFOFadeIn',
            'LFODelay',
            'OscillatorWaveShape',
            'OscillatorOct',
            'OscillatorSemi',
            'OscillatorDetune',
            'FilterCutoffFrequency',
            'FilterLFOCutoffMod',
            'FilterEnvCutoffMod'
        ]
        
        self.globals = [
            'VibratoSpeed',
            'VibratoFadeIn',
            'VibratoAmount',
            'KeyboardUnison',
            'KeyboardUnisonDelay'
        ]
        
        self.parents = [
            'SignalChain1',
            'globals',
            'Envelope.0'
        ]