from contextlib import contextmanager

from tests.case import HTMLTestCase


class FrameTestCase(HTMLTestCase):
    __matcher__ = "frame"


class TestFrame(FrameTestCase):
    __fixture__ = "frames.html"

    def test_finds_frames_by_id(self):
        self.assertEqual(self.get("frame1"), "Frame One")
        self.assertEqual(self.get("frame2"), "Frame Two")
        self.assertEqual(self.get("frame3"), "Frame Three")
        self.assertEqual(self.get("frame4"), "Frame Four")

    def test_finds_frames_by_name(self):
        self.assertEqual(self.get("frame_one"), "Frame One")
        self.assertEqual(self.get("frame_two"), "Frame Two")
        self.assertEqual(self.get("frame_three"), "Frame Three")
        self.assertEqual(self.get("frame_four"), "Frame Four")


class TestIFrame(FrameTestCase):
    __fixture__ = "iframes.html"

    def test_finds_iframes_by_id(self):
        self.assertEqual(self.get("frame1"), "Frame One")
        self.assertEqual(self.get("frame2"), "Frame Two")
        self.assertEqual(self.get("frame3"), "Frame Three")
        self.assertEqual(self.get("frame4"), "Frame Four")

    def test_finds_iframes_by_name(self):
        self.assertEqual(self.get("frame_one"), "Frame One")
        self.assertEqual(self.get("frame_two"), "Frame Two")
        self.assertEqual(self.get("frame_three"), "Frame Three")
        self.assertEqual(self.get("frame_four"), "Frame Four")
