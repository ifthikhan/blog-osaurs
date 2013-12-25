"""Module containing all the tests"""

import unittest

from main import sub_youtube_link


class TestReplaceYoutubeLinksWithEmbeds(unittest.TestCase):

    def test_empty_input(self):
        self.assertEqual(sub_youtube_link(""), "")

    def test_non_string_input(self):
        with self.assertRaises(ValueError):
            sub_youtube_link(5)

    def test_replace_normal_url(self):
        video_id = "5MgBikgcWnY"
        yt = "http://www.youtube.com/watch?v={}".format(video_id)
        sub = """<iframe width="560" height="315"
        src="//www.youtube.com/embed/{}" frameborder="0"
        allowfullscreen></iframe>"""
        subf = sub.format(video_id)
        cont = "This is {} blah blah"
        self.assertTrue(
                sub_youtube_link(cont.format(yt), sub=sub) == cont.format(subf))

    def test_replace_short_url(self):
        video_id = "5MgBikgcWnY"
        yt = "http://youtu.be/{}".format(video_id)
        sub = """<iframe width="560" height="315"
        src="//www.youtube.com/embed/{}" frameborder="0"
        allowfullscreen></iframe>"""
        subf = sub.format(video_id)
        cont = "This is {} blah blah"
        self.assertTrue(
                sub_youtube_link(cont.format(yt), sub=sub) == cont.format(subf))

    def test_replace_normal_url_without_http_or_www(self):
        assert False

    def test_replace_short_url_without_http(self):
        assert False


if __name__ == '__main__':
    unittest.main()

