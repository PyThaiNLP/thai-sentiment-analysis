# -*- coding: utf-8 -*-
import unittest
import sys

from pythaisa import *


class TestUM(unittest.TestCase):
    """
    ระบบทดสอบการทำงานของโค้ดของ PyThaiNLP 1.7
    """
    def test_train(self):
        datatrain=[("ฉันรักคุณ","love"),("ผมก็รักคุณเหมือนกัน","love"),("เกลียดคุณ","neg"),("เกลียดเหมือนกัน","neg")]
        m=model(name="test",train_dataset=datatrain)
        m.train()
        self.assertIsNotNone(m.predict("ฉันรักคุณ"))
        self.assertIsNotNone(model(name="test"))
        

if __name__ == '__main__':
    unittest.main()