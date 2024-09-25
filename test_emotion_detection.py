from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        res1 = emotion_detector("I am glad this happened")
        res2 = emotion_detector("I am really mad about this")
        res3 = emotion_detector("I feel disgusted just hearing about this")
        res4 = emotion_detector("I am so sad about this")
        res5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(res1['dominant_emotion'], 'joy')
        self.assertEqual(res2['dominant_emotion'], 'anger')
        self.assertEqual(res3['dominant_emotion'], 'disgust')
        self.assertEqual(res4['dominant_emotion'], 'sadness')
        self.assertEqual(res5['dominant_emotion'], 'fear')

unittest.main()
