# -*- coding: utf-8 -*-
from vumi.transports.smpp.icodecs import ISmppCodec
from vumi.transports.smpp.codecs import SmppCodec, SmppCodecException

from twisted.trial.unittest import TestCase


class TestSmppCodec(TestCase):

    def setUp(self):
        self.codec = SmppCodec()

    def test_implements(self):
        self.assertTrue(ISmppCodec.implementedBy(SmppCodec))
        self.assertTrue(ISmppCodec.providedBy(self.codec))

    def test_unicode_encode_guard(self):
        self.assertRaises(
            SmppCodecException, self.codec.encode, "byte string")

    def test_bytestring_decode_guard(self):
        self.assertRaises(
            SmppCodecException, self.codec.decode, u"unicode")

    def test_default_encoding(self):
        self.assertEqual(self.codec.encode(u"a"), "a")
        self.assertRaises(
            UnicodeEncodeError, self.codec.encode, u"ë")

    def test_default_decoding(self):
        self.assertEqual(self.codec.decode("a"), u"a")
        self.assertRaises(
            UnicodeDecodeError, self.codec.decode, '\xc3\xab')  # e-umlaut

    def test_utf8(self):
        self.assertEqual(self.codec.encode(u"Zoë", "utf-8"), 'Zo\xc3\xab')