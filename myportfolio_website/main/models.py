from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class About(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=1000)
    description = models.TextField()
    birthday = models.DateField()
    website = models.URLField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    age = models.IntegerField()
    degree = models.CharField(max_length=100)
    email = models.EmailField()
    freelance = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/assets/img/about/')

    def __str__(self):
        return self.title

class Count(models.Model):
    ICON_CHOICES = [
        ('bi bi-award', 'Award'),
        ('bi bi-cup', 'Cup'),
        ('bi bi-people', 'People'),
        ('bi bi-clock', 'Clock'),
        ('bi bi-star', 'Star'),
        ('bi bi-gear', 'Gear'),
        ('bi bi-briefcase', 'Briefcase'),
        ('bi bi-calendar', 'Calendar'),
        ('bi bi-trophy', 'Trophy'),
        ('bi bi-heart', 'Heart'),
        ('bi bi-globe', 'Globe'),
        # Add more icons as needed
    ]

    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, choices=ICON_CHOICES)
    value = models.IntegerField()

    def __str__(self):
        return self.title

class Skill(models.Model):
        
    COLOR_CHOICES = [
        ('#18d26e','Default'),
        ('#e361ff', 'HTML'),
        ('#5578ff', 'CSS'),
        ('#e74c3c', 'JavaScript'),
        ('#4233ff', 'Python'),
        ('#f39c12', 'Django'),
        ('#3498db', 'WordPress/CMS'),
        ('#e74c3c', 'Bootstrap'),
        ('#2ecc71', 'Vue.js'),
        ('#ffbb2c', 'React.js'),
        ('#3498db', 'Canva'),
    ]
    
    name = models.CharField(max_length=100)
    value = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])  # Ensuring percentage between 1% and 100%
    color = models.CharField(max_length=7, choices=COLOR_CHOICES, default='#18d26e')
    
    def __str__(self):
        return self.name

class Interest(models.Model):
    ICON_CHOICES = [
        ('ri-anchor-line', 'Marine Engineering'),
        ('ri-computer-line', 'Web Development'),
        ('ri-paint-brush-line', 'Graphic Design'),
        ('ri-bar-chart-box-line', 'Data Analytics'),
        ('ri-lightbulb-line', 'AI'),
        ('ri-database-2-line', 'Blockchain Technology'),
        ('ri-rocket-line', 'Space Exploration'),
        ('ri-store-line', 'Entrepreneurship'),
        ('ri-football-line', 'Rugby'),
        ('ri-history-line', 'History'),
        ('ri-flask-line', 'Science'),
        ('ri-newspaper-line', 'Current Affairs'),
    ]
    
    COLOR_CHOICES = [
        ('#18d26e','Default'),
        ('#ffbb2c', 'Marine Engineering'),
        ('#e80368', 'Web Development'),
        ('#e361ff', 'Graphic Design'),
        ('#5578ff', 'Data Analytics'),
        ('#ffa76e', 'AI'),
        ('#47aeff', 'Blockchain Technology'),
        ('#e74c3c', 'Space Exploration'),
        ('#4233ff', 'Entrepreneurship'),
        ('#f39c12', 'Rugby'),
        ('#3498db', 'History'),
        ('#e74c3c', 'Science'),
        ('#2ecc71', 'Current Affairs'),
    ]
    
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, choices=ICON_CHOICES, default='ri-anchor-line')
    color = models.CharField(max_length=7, choices=COLOR_CHOICES, default='#18d26e')

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    quote = models.TextField()
    image = models.ImageField(upload_to='media/testimonials/')

    def __str__(self):
        return f"{self.name} - {self.position}"

class Summary(models.Model):
    profile = models.TextField()
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return "Summary"

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    start_year = models.IntegerField()
    end_year = models.IntegerField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.degree

    def year_range(self):
        return f"{self.start_year} - {self.end_year if self.end_year else 'Present'}"

class VoluntaryExperience(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    responsibilities = models.TextField()

    def __str__(self):
        return self.title

    def date_range(self):
        return f"{self.start_date.year} - {self.end_date.year if self.end_date else 'Present'}"

class ProfessionalExperience(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    responsibilities = models.TextField()

    def __str__(self):
        return self.title

    def date_range(self):
        return f"{self.start_date.year} - {self.end_date.year if self.end_date else 'Present'}"

from django.db import models

class Service(models.Model):
    ICON_CHOICES = [
        ('bx bx-laptop', 'Laptop'),
        ('bx bx-chalkboard', 'Chalkboard'),
        ('bx bx-file', 'File'),
        ('bx bx-paint', 'Paint'),
        ('bx bxl-css3', 'CSS3'),
        ('bx bx-line-chart', 'Line Chart'),
        ('bx bx-cube', 'Cube'),
        ('bx bx-folder', 'Folder'),
        ('bx bxl-wordpress', 'WordPress'),
    ]

    COLOR_CHOICES = [
        ('#007bff', 'Blue'),
        ('#28a745', 'Green'),
        ('#ffc107', 'Yellow'),
        ('#dc3545', 'Red'),
        ('#17a2b8', 'Teal'),
        ('#fd7e14', 'Orange'),
        ('#6f42c1', 'Purple'),
        ('#20c997', 'Cyan'),
        ('#0073aa', 'Dark Blue'),
    ]

    title = models.CharField(max_length=200)
    icon = models.CharField(max_length=50, choices=ICON_CHOICES, default='bx bx-laptop')
    color = models.CharField(max_length=7, choices=COLOR_CHOICES, default='#17a2b8')
    description = models.TextField()

    def __str__(self):
        return self.title

from django.db import models

class Portfolio(models.Model):
    CATEGORY_CHOICES = [
        ('app', 'App'),
        ('card', 'Card'),
        ('web', 'Web'),
    ]

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/portfolio/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    service_type = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    client = models.CharField(max_length=200, blank=True, null=True)
    project_date = models.DateField(blank=True, null=True)
    project_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class PortfolioBanner(models.Model):
    portfolio = models.ForeignKey(Portfolio, related_name='banners', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/portfolio/', default='media/portfolio/default-details-1.jpg')

    def __str__(self):
        return f"Banner for {self.portfolio.title}"
