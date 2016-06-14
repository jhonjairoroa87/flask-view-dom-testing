import mock
import unittest

from app import flask_app
from bs4 import BeautifulSoup


class TestViews(unittest.TestCase):
    """
    Tests of the project endpoints
    """

    # An example of the values the /get_groups endpoint is supposed to return
    _get_all_groups_mock_return = [{
        "city": "Medellin",
        "country_code": "CO",
        "country_name": "Colombia",
        "members": 848,
        "name": "Medellin Python y Django Meetup"
    }, {
        "city": "Medellin",
        "country_code": "CO",
        "country_name": "Colombia",
        "members": 150,
        "name": "PyLadies Medellin "
    }]

    @classmethod
    def setUpClass(self):
        self.app = flask_app.test_client()

    @mock.patch('utils.meetup_utils.MeetupUtils.get_all_groups', return_value=_get_all_groups_mock_return)
    def groups_test(self, get_all_groups_mock):
        """
        Validate the values returned by the /groups view
        """
        response = self.app.get('/groups')

        # create soup object with the returned html file
        soup = BeautifulSoup(response.data, "html.parser")

        # look for all divs that it's class is 'flash'
        flask_divs = soup.find_all('div', {'class': "flash"})

        # verify the rendered divs number is the same number of the groups in memory
        self.assertEqual(len(flask_divs), len(self._get_all_groups_mock_return))

        # verify each div text is exactly the same of the the groups in memory
        for index, item in enumerate(self._get_all_groups_mock_return):
            text_div_element = flask_divs[index].text
            name_group_memory = self._get_all_groups_mock_return[index]['name']
            self.assertEqual(text_div_element, name_group_memory)
