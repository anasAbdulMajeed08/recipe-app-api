from django.test import TestCase, Client # Client is test module enabe test requests in our application
from django.contrib.auth import get_user_model
from django.urls import reverse # Uses to create a url for admin page

class AdminSiteTests(TestCase):
    """ Function that runs before test runs """
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@anas.com',
            password='password123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@anas.com',
            password='password123',
            name='Test user full name' 
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page workds"""
        # usually urls looks like: /admin/core/user/[id]
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that create usr page wroks"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
