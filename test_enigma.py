import unittest
import pycipher
import enigma as en


class EnsureCypher(unittest.TestCase):
    def test_cypher(self):
        enigma = pycipher.Enigma(
            settings=("A", "A", "A"),
            rotors=(1, 2, 3),
            reflector="B",
            ringstellung=("A", "A", "A"),
            steckers=[],
        )
        mach1 = en.Enigma(
            settings=("A", "A", "A"),
            rotors=(1, 2, 3),
            reflector="B",
            ringstellung=("B", "B", "B"),
            steckers=[],
        )
        self.assertEqual(
            enigma.encipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
            mach1.encipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
        )
        pass
