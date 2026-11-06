import unittest

from app.main import demo_reply


class DemoReplyTests(unittest.TestCase):
    def test_reply_includes_user_topic(self):
        reply = demo_reply("A video about learning English")
        self.assertIn("A video about learning English", reply)
        self.assertIn("PRODUCTION PLAN", reply)
        self.assertIn("not connected", reply)

    def test_reply_handles_blank_topic(self):
        reply = demo_reply("   ")
        self.assertIn("your idea", reply)


if __name__ == "__main__":
    unittest.main()
