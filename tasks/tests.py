from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Task
from django.utils.timezone import now, timedelta


class TasksViewsTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.admin_user = User.objects.create_superuser(username='admin', password='adminpass', email='admin@example.com')
        self.task = Task.objects.create(name=self.user, taskContent="Test Task", complete=False)

    def test_tasks_home_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('Tasks-home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")

    def test_add_task(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('add_task'), {
            'username': 'testuser',
            'taskContent': 'New Task',
            'complete': 'on'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Task.objects.filter(taskContent='New Task').exists())

    def test_edit_task(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('edit_task', args=[self.task.id]), {
            'username': 'testuser',
            'taskContent': 'Updated Task',
            'complete': 'on'
        })
        self.assertRedirects(response, reverse('Tasks-home'))
        self.task.refresh_from_db()
        self.assertEqual(self.task.taskContent, 'Updated Task')
        self.assertTrue(self.task.complete)

    def test_delete_task(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('delete_task', args=[self.task.id]))
        self.assertRedirects(response, reverse('Tasks-home'))
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())

    def test_external_tasks_home_superuser(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.get(reverse('External-tasks-home'), {'username': 'testuser'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")

    def test_external_tasks_home_permission_denied(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('External-tasks-home'))
        self.assertRedirects(response, reverse('chat-home'))

    def test_filter_completed_tasks(self):
        self.client.login(username='testuser', password='testpass')
        Task.objects.create(name=self.user, taskContent="Completed Task", complete=True)
        response = self.client.get(reverse('Tasks-home') + '?filter=completed')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Completed Task")
        self.assertNotContains(response, "Test Task")  # Test Task is incomplete

    def test_filter_incomplete_tasks(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('Tasks-home') + '?filter=incomplete')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")

    def test_filter_last_week_tasks(self):
        self.client.login(username='testuser', password='testpass')
        old_task = Task.objects.create(name=self.user, taskContent="Old Task", complete=False)
        old_task.date_added = now() - timedelta(days=10)
        old_task.save()

        recent_task = Task.objects.create(name=self.user, taskContent="Recent Task", complete=False)
        recent_task.date_added = now() - timedelta(days=2)
        recent_task.save()

        response = self.client.get(reverse('Tasks-home') + '?filter=week')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Recent Task")
        self.assertNotContains(response, "Old Task")

    def test_filter_last_month_tasks(self):
        self.client.login(username='testuser', password='testpass')
        very_old_task = Task.objects.create(name=self.user, taskContent="Very Old Task", complete=False)
        very_old_task.date_added = now() - timedelta(days=40)
        very_old_task.save()

        this_month_task = Task.objects.create(name=self.user, taskContent="This Month Task", complete=False)
        this_month_task.date_added = now() - timedelta(days=20)
        this_month_task.save()

        response = self.client.get(reverse('Tasks-home') + '?filter=month')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This Month Task")
        self.assertNotContains(response, "Very Old Task")