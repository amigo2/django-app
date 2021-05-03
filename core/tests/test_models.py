from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_model(self):
        ''' test creating user model with email '''
        email = 'mimigo@gmail.com'
        password = '12345678P'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalize(self):
        ''' test email is normalize '''
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(email, '12346578P')

        self.assertEqual(user.email, email.lower())


    def test_new_user_invalid_email(self):
        ''' testing invalid email '''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '12346578P')


    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            'fimmigo@carbon.com', 
            '12345678P'
            )

        # is part of permission mixing 
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)





