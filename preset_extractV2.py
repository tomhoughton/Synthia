"""
This file is what manages all of the data involved with this program.
It's roles include:
- Detecting new training data.
- Adding the new presets into the existing training data.
- CSV dataset creation (NOT IMPLETMENTED YET).
- Source and return all of the training data into json.
"""

"""
IMPORTS
"""
import gzip
import os
from xml.etree.ElementTree import tostring
import xml.etree.cElementTree as ET
import numpy as np
import xmltodict
import json
from xml.dom import minidom


class PresetManager_V2:
    def __init__(self):
        self.training_json_folder = os.path.join('TrainingData', 'TrainingPresets')
        self.NewPresets_folder = os.path.join('NewPresets')
        self.NewPresetsJson_folder = os.path.join('NewPresetsJson')
        self.new_presets = os.path.join('NewPresets')
        self.xml_export_path = os.path.join('NewPresetsXML')
        self.json_export_path = os.path.join('New{resetsJson')

    def get_new_data_v2(self):
        
        """
        This function checks the new presets folder to see if there are any new ones.
        Then return an array of PresetV2 objects for the program to use.

        Improvements:
        - Get it to delete the xml presets as they are not needed.
        - Get rid of the enumerate function as it is not needed.
        """

        # New presets path:
        new_presets = os.path.join('NewPresets')

        # New presets array:
        presets = os.listdir(new_presets)

        # XML export path:
        xml_export_path = os.path.join('NewPresetsXML')

        # Json export path:
        json_export_path = os.path.join('NewPresetsJson')


        # Store the new preset object:
        new_preset_obj = []

        # Loop through:
        for index, preset in enumerate(presets):

            # Export and save the xml files:
            adv_file = os.path.join(new_presets, preset)
            xml_file_name = preset[:-3] + 'xml'
            self.to_xml(adv_file, xml_export_path, xml_file_name)

            json_file_name = preset[:-3] + 'json'
            xml_file = os.path.join(xml_export_path, xml_file_name)
            self.to_json(xml_file, json_export_path, json_file_name)
            print('should be done')

        # Read through the completed json files:
        json_files = os.listdir(json_export_path)
        print('json folder length: ', len(json_files))

        for preset in json_files:
            print('iterate')
            values = []
            name = ""

            with open(os.path.join(json_export_path, preset)) as json_file:
                data = json.load(json_file)
                print('---------------------------')
                print(os.path.join(json_export_path, preset))

                # Name:
                if len(data["Ableton"]["UltraAnalog"]["UserName"]["@Value"]) > 0:
                    name = data["Ableton"]["UltraAnalog"]["UserName"]["@Value"]
                else:
                    name = preset[:-5]

            """
            Values not related to signal chains:
            """

            # One value [0]:
            values.append(data["Ableton"]["UltraAnalog"]["Volume"]["Manual"]["@Value"])

            # Polyphony:

            # Octave:

            # Transpose:

            # Keyboard unison Toggle [1]:
            values.append(data["Ableton"]["UltraAnalog"]["KeyboardUnisonToggle"]["Manual"]["@Value"])

            # Keyboard unison [2]:
            values.append(data["Ableton"]["UltraAnalog"]["KeyboardUnison"]["Manual"]["@Value"])

            # Keyboard detune [3]:
            values.append(data["Ableton"]["UltraAnalog"]["KeyboardDetune"]["Manual"]["@Value"])
            
            # Keyboard unison delay [4]:
            values.append(data["Ableton"]["UltraAnalog"]["KeyboardUnisonDelay"]["Manual"]["@Value"])
            
            # Keyboard Priority [5]:
            values.append(data["Ableton"]["UltraAnalog"]["KeyboardPriority"]["Manual"]["@Value"])
            
            # Vibrato Toggle [6]:
            values.append(data["Ableton"]["UltraAnalog"]["VibratoToggle"]["Manual"]["@Value"])
            
            # Vibrato Speed [7]:
            values.append(data["Ableton"]["UltraAnalog"]["VibratoSpeed"]["Manual"]["@Value"])
            
            # Vibrato fade in [8]:
            values.append(data["Ableton"]["UltraAnalog"]["VibratoFadeIn"]["Manual"]["@Value"])
            
            # Vibrato Amount [9]:
            values.append(data["Ableton"]["UltraAnalog"]["VibratoAmount"]["Manual"]["@Value"])
            
            # Vibrato Error [10]:
            values.append(data["Ableton"]["UltraAnalog"]["VibratoError"]["Manual"]["@Value"])
            
            # Vibrato Delay [11]:
            values.append(data["Ableton"]["UltraAnalog"]["VibratoDelay"]["Manual"]["@Value"])
            
            # Portamento Toggle [12]:
            values.append(data["Ableton"]["UltraAnalog"]["PortamentoToggle"]["Manual"]["@Value"])
            
            # Portamento Time [13]:
            values.append(data["Ableton"]["UltraAnalog"]["PortamentoTime"]["Manual"]["@Value"])
            
            # Portamento Mode [14]:
            values.append(data["Ableton"]["UltraAnalog"]["PortamentoMode"]["Manual"]["@Value"])
            
            # Portamento Legato [15]:
            values.append(data["Ableton"]["UltraAnalog"]["PortamentoLegato"]["Manual"]["@Value"])
            
            # Noise Toggle [16]:
            values.append(data["Ableton"]["UltraAnalog"]["NoiseToggle"]["Manual"]["@Value"])
            
            # Noise Color [17]: 
            values.append(data["Ableton"]["UltraAnalog"]["NoiseColor"]["Manual"]["@Value"])
            
            # Noise Balance [18]:
            values.append(data["Ableton"]["UltraAnalog"]["NoiseColor"]["Manual"]["@Value"])
            
            # Noise Level [19]:
            values.append(data["Ableton"]["UltraAnalog"]["NoiseLevel"]["Manual"]["@Value"])
            
            """
            Signal Chain 01
            """
            # Oscillator Toggle [20]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["OscillatorToggle"]["Manual"]["@Value"])

            # Oscillator Waveshape [21]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["OscillatorWaveShape"]["Manual"]["@Value"])

            # Oscillator Octave [22]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["OscillatorOct"]["Manual"]["@Value"])

            # Oscillator Semitone [23]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["OscillatorSemi"]["Manual"]["@Value"])

            # Oscillator ENV Time [24]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["OscillatorEnvTime"]["Manual"]["@Value"])

            # Values that we need to get:
            # Oscillator Detune [25]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["OscillatorDetune"]["Manual"]["@Value"])

            # Oscillator Modulation1 [26]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["OscillatorModulation1"]["Manual"]["@Value"])

            # Oscillator Pulse Width [27]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["OscillatorPulseWidth"]["Manual"]["@Value"])

            # Oscillator Sub amount [28]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["OscillatorSubAmount"]["Manual"]["@Value"])

            # Oscillatr Balance [29]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["OscillatorBalance"]["Manual"]["@Value"])

            # Oscillator Env Amount [30]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["OscillatorEnvAmount"]["Manual"]["@Value"])

            # Oscillator LFO Mod Pitch [31]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["OscillatorLFOModPitch"]["Manual"]["@Value"])
            
            # Oscillator LFO Mod PW [32]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["OscillatorLFOModPW"]["Manual"]["@Value"])

            # Oscillator Level [33]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["OscillatorLevel"]["Manual"]["@Value"])

            # Filter Toggle [34]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["FilterToggle"]["Manual"]["@Value"])

            # Filter Type [35]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["FilterType"]["Manual"]["@Value"])

            # Filter Drive [36]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["FilterDrive"]["Manual"]["@Value"])

            # FilterCutoffMod [37]
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["FilterKbdCutoffMod"]["Manual"]["@Value"])

            # Filter Cutoff Frequency [38]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["FilterCutoffFrequency"]["Manual"]["@Value"])

            # FilterKbdQMod [39]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["FilterKbdQMod"]["Manual"]["@Value"])

            # FilterQFactor [40]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["FilterQFactor"]["Manual"]["@Value"])

            # Filter LFO Cutoff Mod [41]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["FilterLFOCutoffMod"]["Manual"]["@Value"])
            
            # Filter ENV Cutoff Mod [42]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["FilterEnvCutoffMod"]["Manual"]["@Value"])
            
            # Filter LFO Q MOD ?
            # Filter ENV Q MOD ?

            # Amplifier Toggle [43]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["AmplifierToggle"]["Manual"]["@Value"])

            # AmplifierKbdAmpMod [44]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["AmplifierKbdAmpMod"]["Manual"]["@Value"])

            # AmplifierLevel [45]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["AmplifierLevel"]["Manual"]["@Value"])

            # Amplifier Kbd Pan Mod [46]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["AmplifierKbdPanMod"]["Manual"]["@Value"])
            
            # Amplifier Pan [47]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["AmplifierPan"]["Manual"]["@Value"])
            
            # Amplifier LFO Amp Mod [48]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["AmplifierLFOAmpMod"]["Manual"]["@Value"])
            
            # Amplifier LFO Pan Mod [49]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["AmplifierLFOPanMod"]["Manual"]["@Value"])
            
            # Amplifier ENV Pan Mod [50]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["AmplifierEnvPanMod"]["Manual"]["@Value"])
            
            # LFO Toggle [51]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["LFOToggle"]["Manual"]["@Value"])
            
            # LFO Waveshape [52]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["LFOWaveShape"]["Manual"]["@Value"])
            
            # LFO Sync [53]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["LFOSync"]["Manual"]["@Value"])
            
            # LFO Sync Toggle [54]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["LFOSyncToggle"]["Manual"]["@Value"])
            
            # LFO Gate Reset [55]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["LFOGateReset"]["Manual"]["@Value"])
            
            # LFO Pulse Width [56]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["LFOPulseWidth"]["Manual"]["@Value"])
            
            # LFO Speed [57]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["LFOSpeed"]["Manual"]["@Value"])
            
            # LFO Phase [58]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["LFOPhase"]["Manual"]["@Value"])
            
            # LFO Delay [59]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["LFODelay"]["Manual"]["@Value"])
            
            # LFO FadeIn [60]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["LFOFadeIn"]["Manual"]["@Value"])
            
            """ ENVELOPES"""

            # Envelope 0
            # Exponential Slope [61]
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.0"]["ExponentialSlope"]["Manual"]["@Value"])
            
            # Loop [62]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.0"]["Loop"]["Manual"]["@Value"])
            
            # Free Run [63]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.0"]["FreeRun"]["Manual"]["@Value"])
            
            # Legato [64]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.0"]["Legato"]["Manual"]["@Value"])
            
            # Attack Mod [65]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.0"]["AttackMod"]["Manual"]["@Value"])
            
            # Attack Time [66]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.0"]["AttackTime"]["Manual"]["@Value"])
            
            # Decay Time [67]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.0"]["DecayTime"]["Manual"]["@Value"])
            
            # Amp Mod [68]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.0"]["AmpMod"]["Manual"]["@Value"])
            
            # Sustain Level [69]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.0"]["SustainLevel"]["Manual"]["@Value"])
            
            # SustainTime [70]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.0"]["SustainTime"]["Manual"]["@Value"])
            
            # Release Time [71]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.0"]["ReleaseTime"]["Manual"]["@Value"])
            
            # Envelope 1
            # Exponential Slope [72]
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.1"]["ExponentialSlope"]["Manual"]["@Value"])
            
            # Loop [73]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.1"]["Loop"]["Manual"]["@Value"])
            
            # Free Run [74]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.1"]["FreeRun"]["Manual"]["@Value"])
            
            # Legato [75]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.1"]["Legato"]["Manual"]["@Value"])
            
            # Attack Mod [76]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.1"]["AttackMod"]["Manual"]["@Value"])
            
            # Attack Time [77]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.1"]["AttackTime"]["Manual"]["@Value"])
            
            # Decay Time [78]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.1"]["DecayTime"]["Manual"]["@Value"])
            
            # Amp Mod [79]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.1"]["AmpMod"]["Manual"]["@Value"])
            
            # Sustain Level [80]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.1"]["SustainLevel"]["Manual"]["@Value"])
            
            # SustainTime [81]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.1"]["SustainTime"]["Manual"]["@Value"])
            
            # Release Time [82]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain1"]["Envelope.1"]["ReleaseTime"]["Manual"]["@Value"])
            

            """
            Signal Chain 02
            """

            # Oscillator Toggle [83]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["OscillatorToggle"]["Manual"]["@Value"])

            # Oscillator Waveshape [84]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["OscillatorWaveShape"]["Manual"]["@Value"])

            # Oscillator Osctave [85]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["OscillatorOct"]["Manual"]["@Value"])

            # Oscillator Semitone [86]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["OscillatorSemi"]["Manual"]["@Value"])

            # Psco;;atpr ENV Time [87]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["OscillatorEnvTime"]["Manual"]["@Value"])

            # Values that we need to get:
            # Oscillator Detune [88]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["OscillatorDetune"]["Manual"]["@Value"])

            # Oscillator Modulation1 [89]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["OscillatorModulation1"]["Manual"]["@Value"])

            # Oscillator Pulse Width [90]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["OscillatorPulseWidth"]["Manual"]["@Value"])

            # Oscillator Sub amount [91]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["OscillatorSubAmount"]["Manual"]["@Value"])

            # Oscillatr Balance [92]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["OscillatorBalance"]["Manual"]["@Value"])

            # Oscillator Env Amount [93]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["OscillatorEnvAmount"]["Manual"]["@Value"])

            # Oscillator LFO Mod Pitch [94]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["OscillatorLFOModPitch"]["Manual"]["@Value"])
            
            # Oscillator LFO Mod PW [95]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["OscillatorLFOModPW"]["Manual"]["@Value"])

            # Oscillator Level [96]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["OscillatorLevel"]["Manual"]["@Value"])

            # Filter Toggle [97]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["FilterToggle"]["Manual"]["@Value"])

            # Filter Type [98]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["FilterType"]["Manual"]["@Value"])

            # Filter Drive [99]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["FilterDrive"]["Manual"]["@Value"])

            # FilterCutoffMod [100]
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["FilterKbdCutoffMod"]["Manual"]["@Value"])

            # Filter Cutoff Frequency [101]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["FilterCutoffFrequency"]["Manual"]["@Value"])

            # FilterKbdQMod [102]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["FilterKbdQMod"]["Manual"]["@Value"])

            # FilterQFactor [103]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["FilterQFactor"]["Manual"]["@Value"])

            # Filter LFO Cutoff Mod [104]:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["FilterLFOCutoffMod"]["Manual"]["@Value"])
            
            # Filter ENV Cutoff Mod 105:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["FilterEnvCutoffMod"]["Manual"]["@Value"])
            
            # Filter LFO Q MOD ?
            # Filter ENV Q MOD ?

            # Amplifier Toggle 106:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["AmplifierToggle"]["Manual"]["@Value"])

            # AmplifierKbdAmpMod 107:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["AmplifierKbdAmpMod"]["Manual"]["@Value"])

            # AmplifierLevel 108:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["AmplifierLevel"]["Manual"]["@Value"])

            # Amplifier Kbd Pan Mod 109:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["AmplifierKbdPanMod"]["Manual"]["@Value"])
            
            # Amplifier Pan 110:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["AmplifierPan"]["Manual"]["@Value"])
            
            # Amplifier LFO Amp Mod 111:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["AmplifierLFOAmpMod"]["Manual"]["@Value"])
            
            # Amplifier LFO Pan Mod 112:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["AmplifierLFOPanMod"]["Manual"]["@Value"])
            
            # Amplifier ENV Pan Mod 113:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["AmplifierEnvPanMod"]["Manual"]["@Value"])
            
            # LFO Toggle 114: 
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["LFOToggle"]["Manual"]["@Value"])
            
            # LFO Waveshape 115:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["LFOWaveShape"]["Manual"]["@Value"])
            
            # LFO Sync 116:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["LFOSync"]["Manual"]["@Value"])
            
            # LFO Sync Toggle 117:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["LFOSyncToggle"]["Manual"]["@Value"])
            
            # LFO Gate Reset 118:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["LFOGateReset"]["Manual"]["@Value"])
            
            # LFO Pulse Width 119:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["LFOPulseWidth"]["Manual"]["@Value"])
            
            # LFO Speed 120:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["LFOSpeed"]["Manual"]["@Value"])
            
            # LFO Phase 121:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["LFOPhase"]["Manual"]["@Value"])
            
            # LFO Delay 122:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["LFODelay"]["Manual"]["@Value"])
            
            # LFO FadeIn 123:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["LFOFadeIn"]["Manual"]["@Value"])
            
            """ ENVELOPES"""
            # Envelope 0
            # Exponential Slope 124
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["Envelope.0"]["ExponentialSlope"]["Manual"]["@Value"])
            
            # Loop 125:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["Envelope.0"]["Loop"]["Manual"]["@Value"])
            
            # Free Run 126:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["Envelope.0"]["FreeRun"]["Manual"]["@Value"])
            
            # Legato 127:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["Envelope.0"]["Legato"]["Manual"]["@Value"])
            
            # Attack Mod 128:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["Envelope.0"]["AttackMod"]["Manual"]["@Value"])
            
            # Attack Time 129:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["Envelope.0"]["AttackTime"]["Manual"]["@Value"])
            
            # Decay Time 130:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["Envelope.0"]["DecayTime"]["Manual"]["@Value"])
            
            # Amp Mod 130:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["Envelope.0"]["AmpMod"]["Manual"]["@Value"])
            
            # Sustain Level 131:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["Envelope.0"]["SustainLevel"]["Manual"]["@Value"])
            
            # SustainTime 132:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["Envelope.0"]["SustainTime"]["Manual"]["@Value"])
            
            # Release Time 133:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["Envelope.0"]["ReleaseTime"]["Manual"]["@Value"])
            
            # Envelope 1
            # Exponential Slope 134
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["Envelope.1"]["ExponentialSlope"]["Manual"]["@Value"])
            
            # Loop 135:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["Envelope.1"]["Loop"]["Manual"]["@Value"])
            
            # Free Run 136:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["Envelope.1"]["FreeRun"]["Manual"]["@Value"])
            
            # Legato 137:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["Envelope.1"]["Legato"]["Manual"]["@Value"])
            
            # Attack Mod 138:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["Envelope.1"]["AttackMod"]["Manual"]["@Value"])
            
            # Attack Time 139:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["Envelope.1"]["AttackTime"]["Manual"]["@Value"])
            
            # Decay Time 140:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["Envelope.1"]["DecayTime"]["Manual"]["@Value"])
            
            # Amp Mod 141:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["Envelope.1"]["AmpMod"]["Manual"]["@Value"])
            
            # Sustain Level 142:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["Envelope.1"]["SustainLevel"]["Manual"]["@Value"])
            
            # SustainTime 143:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["Envelope.1"]["SustainTime"]["Manual"]["@Value"])
            
            # Release Time 144:
            values.append(data["Ableton"]["UltraAnalog"]["SignalChain2"]["Envelope.1"]["ReleaseTime"]["Manual"]["@Value"])
            
            # Append new preset and values to array.
            new_preset = PresetV2(name, values, 0, 0, 0, 0)
            new_preset_obj.append(new_preset)
        return new_preset_obj

    def get_preset_dataV2(self):

        presets = []

        # Need to get the path to the training data:
        training_json_folder = os.path.join('TrainingData', 'TrainingPresets')

        training_presets = os.listdir(training_json_folder)

        for preset in training_presets:
            values = []

            with open(os.path.join(training_json_folder, preset)) as json_file:

                data = json.load(json_file)
                
                name = data["name"] 

                # Volume:
                values.append(data["volume"])

                # OscToggle01:
                values.append(data["OscToggle01"])

                # OscWaveShape01:
                values.append(data["OscWaveshape01"])

                # OscOctave01
                values.append(data["OscOctave01"])

                # OscSemi01:
                values.append(data["OscSemi01"])

                # OscEnvT01:
                values.append(data["OsvEnvT01"])

                # OscToggle 02:
                values.append(data["OscToggle02"])

                # Osc WaveShape 02:
                values.append(data["OscWaveshape02"])

                # Osc Octave02:
                values.append(data["OscOctave02"])

                # Osc Semi 02:
                values.append(data["OscSemi02"])

                # Osc Env02
                values.append(data["OscEnvT02"])

                """
                Descriptors:
                """
                brightness = data["descriptors"]["brightness"] 
                consistency = data["descriptors"]["consistency"] 
                dynamics = data["descriptors"]["dynamics"] 
                evolution = data["descriptors"]["evolution"] 

                new_preset = PresetV2(name, values, consistency, brightness, dynamics, evolution)
                presets.append(new_preset)

                
        return presets


    def to_xml(self, path, export_path, file_name):
        with gzip.open(path, 'r') as f:
            raw_xml = f.read()

            xml = ET.fromstring(raw_xml)
            tree = ET.ElementTree(xml)
            tree.write(os.path.join(export_path, file_name), encoding="utf-8")



    def to_json(self, path, export_path, file_name):
        xml_tree = ET.parse(path)

        root = xml_tree.getroot()
        to_string = ET.tostring(root, encoding='utf-8', method='xml')
        xml_to_dict = xmltodict.parse(to_string)
        
        with open(os.path.join(export_path, file_name), 'w') as json_file:
            json.dump(xml_to_dict, json_file, indent=2)

    def get_json_tree(self, presets):
        json_presets = []

        for preset in presets:
            json_presets.append(
                preset.format_to_json()
            )

        return { 'presets': json_presets }


    def save_training_data(self, presets):
        """
        This saves the new presets as json files.
        And then deletes the old 'new' presets.
        """

        # Need to get the path to export the json files:
        training_json_export = os.path.join('TrainingData', 'TrainingPresets')

        for preset in presets:
            preset_name = preset["name"] + '.json'
            self.write_json(training_json_export, preset_name, preset)


    def write_json(self, export_path, file_name, data):
        with open(os.path.join(export_path, file_name), 'w') as json_file:
            json.dump(data, json_file)


    def clear_NewPresets_folder(self, usedPresets):

        # Path to NewPresets:
        NewPresets_folder = os.path.join('NewPresets')
        NewPresetsJson_folder = os.path.join('NewPresetsJson')
        adv_to_remove = self.create_file_extensions(usedPresets, '.adv')
        json_to_remove = self.create_file_extensions(usedPresets, '.json')

        for index, adv in enumerate(adv_to_remove):
            # Generate the correct file paths:
            path_to_remove_adv = os.path.join(NewPresets_folder, adv)
            path_to_remove_json = os.path.join(NewPresetsJson_folder, json_to_remove[index])
            
            # Remove file:
            os.remove(path_to_remove_adv)
            os.remove(path_to_remove_json)

    def create_file_extensions(self, data, extension):
        temp = []
        for element in data:
            temp.append(element["name"] + extension)

        return temp       

    def refresh_stats(self):

        # This stores the low mid and high bands of the descriptors:
        descriptor_m = np.array([
            [0, 0, 0], # Consistency
            [0, 0, 0], # Brightness
            [0, 0, 0], # Dynamics
            [0, 0, 0] # Evolution
        ])

        total = 0 # Stores the total presets.

        presets = os.listdir(self.training_json_folder)

        for preset in presets:
            total += 1
            with open(os.path.join(self.training_json_folder, preset), 'r') as json_file:
                data = json.load(json_file)
                descriptors = [
                    data["descriptors"]["consistency"],
                    data["descriptors"]["brightness"],
                    data["descriptors"]["dynamics"],
                    data["descriptors"]["evolution"]
                ]

                for i, descrip in enumerate(descriptors):
                    if descrip > 66:
                        descriptor_m[i][2] = descriptor_m[i][2] + 1
                    elif descrip < 66 and descrip > 33:
                        descriptor_m[i][1] = descriptor_m[i][1] + 1
                    elif descrip < 33:
                        descriptor_m[i][0] = descriptor_m[i][0] + 1
        
        data = {
            'descriptorMatrix': descriptor_m,
            'totalPresets': total
        }

        return data





class PresetV2:
    def __init__ (self, name, values, consistency, brightness, dynamics, evolution):
        self.name = name
        self.volume = values[0]

        """
        Descriptors
        """
        self.consistency = consistency
        self.brightness = brightness
        self.dynamics = dynamics
        self.evolution = evolution

        """
        Independants:
        """
        self.UnisonToggle = values[1]
        self.keyboardUnison = values[2]
        self.keyboardDetune = values[3]
        self.keyboardUnisonDelay = values[4]
        
        self.keyboardPriority = values[5]

        self.vibratoToggle = values[6]
        self.vibratoSpeed = values[7]
        self.vibratoFadein = values[8]
        self.vibratoAmount = values[9]
        self.vibratoError = values[10]
        self.vibratoDelay = values[11]
        
        self.portamentoToggle = values[12]
        self.portamentoTime = values[13]
        self.PortamentoMode = values[14]
        self.PortamentoLegato = values[15]

        self.noiseToggle = values[16]
        self.noiseColor = values[17]
        self.noiseBalance = values[18]
        self.noiseLevel = values[19]


        """
        Signal Chain 01
        """
        self.OscToggle01 = values[20]
        self.OscWaveshape01 = values[21]
        self.OscOsctave01 = values[22]
        self.OscSemi01 = values[23]
        self.OscEnvT01 = values[24]

        # Need to get:
        self.OscDetune01 = values[25]
        self.OscModulation01 = values[26]
        self.OscPulseWidth01 = values[27]
        self.OscSubAmount01 = values[28]
        self.OscBalance01 = values[29]
        self.OscEnvAmount01 = values[30]
        self.OscLFOModPitch01 = values[31]
        self.OscLFOModPW01 = values[32]
        self.OscLevel01 = values[33]
        
        self.filterToggle01 = values[34]
        self.filterType01 = values[35]
        self.filterDrive01 = values[36]
        self.filterCutoffMod01 = values[37]
        self.filterCutoffFreq01 = values[38]
        self.filterKbdMod01 = values[39]
        self.filterQFactor01 = values[40]
        self.filterLFOCuttoffMod = values[41]
        self.filterENVCuttoffMod = values[42]
        
        self.ampToggle01 = values[43]
        self.ampKbdAmpMod01 = values[44]
        self.ampLevel01 = values[45]
        self.ampKbdPanMod01 = values[46]
        self.ampPan01 = values[47]
        self.ampLFOampMod01 = values[48]
        self.ampLFOPanMod01 = values[49]
        
        self.lfoToggle01 = values[51]
        self.lfoWaveshape01 = values[52]
        self.lfoSync01 = values[53]
        self.lfoSyncToggle = values[54]
        self.lfoGateReset01 = values[55]
        self.lfoPulseWidth01 = values[56]
        self.lfoSpeed01 = values[57]
        self.lfoPhase01 = values[58]
        self.lfoDelay01 = values[59]
        self.lfoFadeIn01 = values[60]

        self.envExpoSlope01 = values[61]
        self.envLoop01 = values[62]
        self.envFreeRun01 = values[63]
        self.envLegato01 = values[64]
        self.envAttackMod01 = values[65]
        self.envAttackTime01 = values[66]
        self.envDecayTime01 = values[67]
        self.envAmpMod01 = values[68]
        self.envSustainLevel01 = values[69]
        self.envSustainTime01 = values[70]
        self.envReleaseTime01 = values[71]
        
        """ENV 02"""
        self.env02ExpoSlope01 = values[72]
        self.env02Loop01 = values[73]
        self.env02FreeRun01 = values[74]
        self.env02Legato01 = values[75]
        self.env02AttackMod01 = values[76]
        self.env02AttackTime01 = values[77]
        self.env02DecayTime01 = values[78]
        self.env02AmpMod01 = values[79]
        self.env02SustainLevel01 = values[80]
        self.env02SustainTime01 = values[81]
        self.env02ReleaseTime01 = values[82]
        

        """
        Signal Chain 02
        """
        self.OscToggle02 = values[83]
        self.OscWaveshape02 = values[84]
        self.OscOsctave02 = values[85]
        self.OscSemi02 = values[86]
        self.OscEnvT02 = values[87]

        # Need to get:
        self.OscDetune02 = values[88]
        self.OscModulation02 = values[89]
        self.OscPulseWidth02 = values[90]
        self.OscSubAmount02 = values[91]
        self.OscBalance02 = values[92]
        self.OscEnvAmount02 = values[93]
        self.OscLFOModPitch02 = values[94]
        self.OscLFOModPW02 = values[95]
        self.OscLevel02 = values[96]
        
        self.filterToggle01 = values[97]
        self.filterType01 = values[98]
        self.filterDrive01 = values[99]
        self.filterCutoffMod01 = values[100]
        self.filterCutoffFreq01 = values[101]
        self.filterKbdMod01 = values[102]
        self.filterQFactor01 = values[103]
        self.filterLFOCuttoffMod = values[104]
        self.filterENVCuttoffMod = values[105]
        
        self.ampToggle02 = values[106]
        self.ampKbdAmpMod02 = values[107]
        self.ampLevel02 = values[108]
        self.ampKbdPanMod02 = values[109]
        self.ampPan02 = values[110]
        self.ampLFOampMod02 = values[111]
        self.ampLFOPanMod02 = values[112]
        
        self.lfoToggle02 = values[114]
        self.lfoWaveshape02 = values[115]
        self.lfoSync02 = values[116]
        self.lfoSyncToggle = values[117]
        self.lfoGateReset02 = values[118]
        self.lfoPulseWidth02 = values[119]
        self.lfoSpeed02 = values[120]
        self.lfoPhase02 = values[121]
        self.lfoDelay02 = values[122]
        self.lfoFadeIn02 = values[123]

        self.envExpoSlope02 = values[124]
        self.envLoop02 = values[125]
        self.envFreeRun02 = values[126]
        self.envLegato02 = values[127]
        self.envAttackMod02 = values[128]
        self.envAttackTime02 = values[129]
        self.envDecayTime02 = values[130]
        self.envAmpMod02 = values[130]
        self.envSustainLevel02 = values[131]
        self.envSustainTime02 = values[132]
        self.envReleaseTime02 = values[133]
        
        """ENV 02"""
        self.env02ExpoSlope02 = values[134]
        self.env02Loop02 = values[135]
        self.env02FreeRun02 = values[136]
        self.env02Legato02 = values[137]
        self.env02AttackMod02 = values[138]
        self.env02AttackTime02 = values[139]
        self.env02DecayTime02 = values[140]
        self.env02AmpMod02 = values[141]
        self.env02SustainLevel02 = values[142]
        self.env02SustainTime02 = values[143]
        self.env02ReleaseTime02 = values[144]

    def format_to_json(self):
        return {
            'name': self.name,
            'volume': self.volume,
            'OscToggle01': self.OscToggle01,
            'OscWaveshape01': self.OscWaveshape01,
            'OscOctave01': self.OscOsctave01,
            'OscSemi01': self.OscSemi01,
            'OsvEnvT01': self.OscEnvT01,
            'OscToggle02': self.OscToggle02,
            'OscWaveshape02': self.OscWaveshape02,
            'OscOctave02': self.OscOsctave02,
            'OscSemi02': self.OscSemi02,
            'OscEnvT02': self.OscEnvT02,
            'descriptors': {
                'consistency': self.consistency,
                'brightness': self.brightness,
                'dynamics': self.dynamics,
                'evolution': self.evolution
            }
        }