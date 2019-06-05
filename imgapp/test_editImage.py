#!/usr/bin/python
# -*- coding: utf-8 -*-
from .editImage import setLabelCvtType, readImg, setOutputPath, decideOutputPath

class TestClass(object):

    def test_setLabelCvtType1(self):
        cvtType = setLabelCvtType("gray")
        assert cvtType == "グレースケール画像"

    def test_setLabelCvtType2(self):
        cvtType = setLabelCvtType("monochrome")
        assert cvtType == "モノクロ画像"

    def test_setLabelCvtType3(self):
        cvtType = setLabelCvtType("mosaic")
        assert cvtType == "顔モザイク画像"

    def test_setLabelCvtType4(self):
        cvtType = setLabelCvtType("convolute")
        assert cvtType == "ぼかし画像"

    def test_setOutputPath1(self):
        output = setOutputPath("test1","gray")
        assert output == "edittedImg/test1_gray.jpg"

    def test_setOutputPath2(self):
        output = setOutputPath("test2","monochrome")
        assert output == "edittedImg/test2_monochrome.jpg"

    def test_setOutputPath3(self):
        output = setOutputPath("test3","mosaic")
        assert output == "edittedImg/test3_mosaic.jpg"

    def test_setOutputPath4(self):
        output = setOutputPath("test4","convolute")
        assert output == "edittedImg/test4_convolute.jpg"

    def test_setOutputPath5(self):
        output = setOutputPath("+>?*<`{~|}`","gray")
        assert output == "edittedImg/+>?*<`{~|}`_gray.jpg"

    def test_setOutputPath6(self):
        output = setOutputPath("+>?*<`{~|}`","monochrome")
        assert output == "edittedImg/+>?*<`{~|}`_monochrome.jpg"

    def test_setOutputPath7(self):
        output = setOutputPath("+>?*<`{~|}`","mosaic")
        assert output == "edittedImg/+>?*<`{~|}`_mosaic.jpg"

    def test_setOutputPath8(self):
        output = setOutputPath("+>?*<`{~|}`","convolute")
        assert output == "edittedImg/+>?*<`{~|}`_convolute.jpg"

    def test_setOutputPath9(self):
        output = setOutputPath("テスト（全角）","gray")
        assert output == "edittedImg/テスト（全角）_gray.jpg"

    def test_setOutputPath10(self):
        output = setOutputPath("テスト（全角）","monochrome")
        assert output == "edittedImg/テスト（全角）_monochrome.jpg"

    def test_setOutputPath11(self):
        output = setOutputPath("テスト（全角）","mosaic")
        assert output == "edittedImg/テスト（全角）_mosaic.jpg"

    def test_setOutputPath12(self):
        output = setOutputPath("テスト（全角）","convolute")
        assert output == "edittedImg/テスト（全角）_convolute.jpg"
