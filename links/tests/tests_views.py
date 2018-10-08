from django.test import TestCase
from django.shortcuts import reverse
# Models
from links.models import Link
from profiles.models import Profile
from users.models import User
# Serializers
from links.serializers import LinkSerializer

import json


class LinkViewSetTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='johndoe@gmail.com',
            password='password1',
        )
        self.profile = Profile.objects.create(
            user=self.user,
            first_name='John',
            last_name='Doe',
            display_name='John Doe',
        )
        self.link_1 = Link.objects.create(
            profile=self.profile,
            url='https://www.google.com',
            title='Google',
        )
        self.link_2 = Link.objects.create(
            profile=self.profile,
            url='https://www.youtube.com',
            title='Youtube',
        )
        self.client.login(email='johndoe@gmail.com', password='password1')

        # Payloads
        self.valid_payload = {
            'url': 'https://www.yahoo.com',
            'name': 'Yahoo'
        }

    def test_get_links(self):
        # Get data from request
        resp = self.client.get(reverse('link-list'))

        # Get data from model
        links = Link.objects.filter(profile=self.profile)
        serializer = LinkSerializer(links, many=True)

        self.assertEqual(resp.data, serializer.data)

    def test_post_valid_link(self):
        # Test valid link
        data = {
            'url': 'https://www.facebook.com',
            'title': 'Facebook',
            'tags_str': 'facebook, social media',
        }
        resp = self.client.post(reverse('link-list'), data=data, user=self.user)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['url'], data['url'])
        self.assertEqual(resp.data['title'], data['title'])
        self.assertEqual('facebook', resp.data['tags'][0]['name'])
        self.assertEqual('social media', resp.data['tags'][1]['name'])

    def test_update_link(self):
        data = {
            'url': 'https://www.yahoo.com',
            'title': 'Yahoo',
        }
        # Update link_1
        resp = self.client.patch(reverse(
            'link-detail',
            kwargs={'pk': self.link_1.id}),
            data=json.dumps(data),
            content_type='application/json',
        )

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['url'], data['url'])
        self.assertEqual(resp.data['title'], data['title'])

    def test_delete_link(self):
        # Delete object
        resp = self.client.delete(reverse(
            'link-detail',
            kwargs={'pk': self.link_2.id}
        ))
        self.assertEqual(resp.status_code, 204)

        # Try and get deleted object, should return 404
        resp = self.client.get(reverse(
            'link-detail',
            kwargs={'pk': self.link_2.id}
        ))
        self.assertEqual(resp.status_code, 404)

