from django.test import TestCase
from . models import Blog,Comment,Venue,Sport,Lesson,Facility,Bookings
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
    self.test_venue.save()
    self.blog = Blog(title = 'sample1',description = 'sample1 description',venue = self.test_venue,user = self.test_user)
    self.blog2 = Blog(title = 'sample2',description = 'sample12 description',venue = self.test_venue,user = self.test_user)
    self.comments = Comment(user = self.test_user,comment_id=self.blog,status='new comment')

  def test_instance(self):
    self.assertTrue(isinstance(self.blog,Blog))


  def test_save_blog(self):
    self.blog.save_blog()
    blogs = Blog.objects.all()
    self.assertTrue(len(blogs)>0)


  def test_delete_blog(self):
    self.blog2.save_blog()
    self.blog.save_blog()
    self.blog.delete_blog()
    blogs = Blog.objects.all()
    self.assertEqual(len(blogs),1)


  def test_display_blog(self):
    self.blog.save_blog()
    self.blog2.save_blog()
    dt = Blog.display_blogs()
    self.assertEqual(len(dt),2)





class TestSport(TestCase):
  '''
  class that will test the sports model
  '''
  def setUp(self):
    self.sportName = Sport(sportName = 'Kasarani' )

  def test_instance(self):
    self.assertTrue(isinstance(self.sportName,Sport))

  def test_sport_save(self):
    self.sportName.save_sport()
    all_sports = Sport.objects.all()
    self.assertTrue(len(all_sports)>0)

  def test_delete_sport(self):
    self.sportName.save_sport()
    self.sportName.delete_sport()
    all_sports = Sport.objects.all()
    self.assertEqual(len(all_sports),0)


class TestBokings(TestCase):
  '''
  class that will test the Booking model
  '''
  def setUp(self):
    self.test_user = User(username = 'code')
    self.test_user.save()
    self.lessonSport = Sport(sportName = 'Kasarani' )
    self.lessonSport.save()
    self.lessonVenue = Venue(venueName='Nyayo',venueLocation='Nairobi',venueCapacity=100)
    self.lessonVenue.save()
    self.lessonFacility = Facility(facilityName = 'dont know', facilityLocation = self.lessonVenue, facilityRoom = 21)
    self.lessonFacility.save()
    self.test_lesson = Lesson(lessonName = 'Swimming', lessonDescription = 'just swimming', lessonSport=self.lessonSport, lessonVenue = self.lessonVenue, lessonFacility = self.lessonFacility)
    self.test_lesson.save()
    self.test_booking = Bookings(lessonBooked = self.test_lesson, user = self.test_user)


  def test_instance(self):
    self.assertTrue(isinstance(self.test_booking,Bookings))
