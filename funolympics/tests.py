from django.test import TestCase
from . models import Blog,Comment,Venue
from django.contrib.auth.models import User

# Create your tests here.

class TestBlogs(TestCase):
  '''
  Class where we write our Blog models tests
  '''
  def setUp(self):
    '''
    function that runs before others
    '''
    self.test_user = User(username = 'code')
    self.test_user.save()
    self.test_venue = Venue(venueName='Nyayo',venueLocation='Nairobi',venueCapacity=100)
    self.blog = Blog(title = 'sample1',description = 'sample1 description',venue = self.test_venue,user = self.test_user)
    self.comments = Comment(user = self.test_user,comment_id=self.blog,status='new comment')

  def test_instance(self):
    self.assertTrue(isinstance(self.comments,Blog))


  def test_save_blog(self):
    self.blog.save_blog()
    blogs = Blog.objects.all()
    self.assertTrue(len(blogs)>0)


  def test_delete_blog(self):
    self.blog2 = Blog(title = 'sample2',description = 'sample12 description',venue = 'Nairobi',user = self.test_user)
    self.blog2.save_blog()
    self.blog.save_blog()
    self.blog.delete_blog()
    blogs = Blog.objects.all()
    self.assertEqual(len(blogs),1)


  def test_display_images(self):
    self.blog.save_blog()
    self.blog2= Blog(title = 'sample2',description = 'sample12 description',venue = 'Nairobi',user = self.test_user)
    self.blog2.save_image()
    dt = Blog.display_blogs()
    self.assertEqual(len(dt),2)





# class TestComments(TestCase):
#   '''
#   class that will test the profile model
#   '''
#   def setUp(self):
#     self.test_user = User(username = 'denis')
#     self.test_user.save()
#     self.image = Image(image = 'denis.jpeg',name = 'denis',caption = 'denis',user = self.test_user)
#     self.comments = Comment(comment = 'awesome',image = self.image,user = self.test_user)

