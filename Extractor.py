from typing import List
import re, json

class Extractor:
    def __init__(self, filePath: str):
        with open(filePath) as f:
            self._patterns = json.load(f)

    @property
    def input(self):
        if 'input' in self._patterns:
            return re.compile(self._patterns['input'])
        else: raise ValueError('No input key in pattern file')

    @property
    def resource(self):
        if 'resource' in self._patterns:
            return re.compile(self._patterns['resource'])
        else: raise ValueError('No resource key in pattern file')
