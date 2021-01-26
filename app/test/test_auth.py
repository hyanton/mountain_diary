import unittest
import json
from app.test.base import BaseTestCase


def register_user(self):
    return self.client.post(
        '/user/',
        data=json.dumps({
            'username': 'test',
            'email': 'example@gmail.com',
            'password': '123456'
        }),
        content_type='application/json'
    )


def login_user(self):
    return self.client.post(
        '/auth/login',
        data=json.dumps({
            'email': 'example@gmail.com',
            'password': '123456'
        }),
        content_type='application/json'
    )


class TestAuth(BaseTestCase):
    def test_registred_user_login(self):
        """
        Test for login of registred user login
        :return:
        """
        with self.client:
            # user registration
            user_response = register_user(self)
            response_data = json.loads(user_response.data)
            self.assertTrue(response_data['Authorization'])
            self.assertEqual(user_response.status_code, 201)

            # registred user login
            login_response = login_user(self)
            data = json.loads(login_response.data)
            self.assertTrue(data['Authorization'])
            self.assertEqual(login_response.status_code, 200)

    def test_valid_logout(self):
        """
        Test for logout before token expires
        :return:
        """

        with self.client:
            # user registration
            user_response = register_user(self)
            response_data = json.loads(user_response.data)
            self.assertTrue(response_data['Authorization'])
            self.assertEqual(user_response.status_code, 201)

            # registred user login
            login_response = login_user(self)
            data = json.loads(login_response.data)
            self.assertTrue(data['Authorization'])
            self.assertEqual(login_response.status_code, 200)

            # valid token logout
            response = self.client.post(
                '/auth/logout',
                headers={
                    'Authorization': 'Bearer ' + str(json.loads(login_response.data)['Authorization'])
                }
            )

            data = json.loads(response.data)
            self.assertTrue(data['status'] == 'success')
            self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()