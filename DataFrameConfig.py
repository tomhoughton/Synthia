
class DataFrameConfig:
    def __init__(self) -> None:
        self.signalChain = [
            "LFOSpeed",
            'LFOFadeIn',
            'OscillatorWaveShape',
            'OscillatorOct',
            'OscillatorSemi',
            'OscillatorDetune',
            'FilterCutoffFrequency',
            'FilterLFOCutoffMod',
            'FilterEnvCutoffMod'
        ]
        
        self.envelopes = [
            'AttackTime',
            'DecayTime',
            'SustainLevel',
            'SustainTime',
            'ReleaseTime'
        ]
        
        self.globals = [
            'VibratoSpeed',
            'VibratoAmount',
            'KeyboardUnisonToggle',
            'KeyboardUnison'
        ]
        
        