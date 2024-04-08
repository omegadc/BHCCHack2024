from flask import Flask, render_template

app = Flask(__name__)

# Dummy data

profile_student = [{
    "id":
    1,
    "name":
    "Adeolu Adeyemi",
    "major":
    "Computer Science",
    "role":
    "Student",
    "year":
    "Second Year",
    "image":
    "john.jpg",
    "description":
    "John is a computer science major who loves to code.",
    "interests": ["Python", "Machine Learning", "Web Development"],
    "points_earned":
    50,
    "events_attended": ["Hackathon", "Conference", "Workshop"],
    "events_scheduled": ["Python", "Machine Learning", "Web Development"],
    "study_groups": ["Python", "Machine Learning", "Web Development"],
    "title":
    "Scholar"
}]

profile_staff = [{
    "id":
    8,
    "name":
    "Michael Clarke Duncan",
    "major":
    "Theatre Arts",
    "year":
    "Third Year",
    "role":
    "Advisor",
    "image":
    "linda.jpg",
    "description":
    "Micheal is passionate about understanding the events and cultures of the past.",
    "interests":
    ["Ancient Civilizations", "European History", "Historical Methodology"],
    "points_earned":
    55,
    "events_attended": [
        "Historical Symposium", "Archaeological Excavation",
        "Documentary Screening"
    ],
    "events_scheduled":
    ["Ancient Civilizations", "European History", "Historical Methodology"],
    "study_groups":
    ["Ancient Civilizations", "European History", "Historical Methodology"],
    "title":
    "Staff"
}]

people = [{
    "id": 1,
    "name": "David Cerna",
    "major": "Computer Science",
    "role": "Student",
    "year": "Second Year",
    "image":
    "https://media.licdn.com/dms/image/D4E03AQHOGxP6OZBp6w/profile-displayphoto-shrink_800_800/0/1706128669350?e=1718236800&v=beta&t=cYYvjL6dyqAgyV4NOgqx4nU37X4hmc61U-1mo_mQL7A",
    "description": "John is a computer science major who loves to code.",
    "interests": ["Python", "Machine Learning", "Web Development"],
    "points_earned": 50,
    "events_attended": ["Hackathon", "Conference", "Workshop"],
    "events_scheduled": ["Python", "Machine Learning", "Web Development"],
    "study_groups": ["Python", "Machine Learning", "Web Development"],
    "title": "Scholar"
}, {
    "id":
    2,
    "name":
    "Jaylen Brown",
    "major":
    "Engineering-Undecided",
    "year":
    "Alum",
    "role":
    "Alum",
    "image":
    "https://cdn.nba.com/headshots/nba/latest/1040x760/1627759.png",
    "description":
    "Emily is passionate about electrical engineering and enjoys building circuits.",
    "interests": ["Circuit Design", "Signal Processing", "Embedded Systems"],
    "points_earned":
    65,
    "events_attended": ["Engineering Expo", "Seminar", "Tech Talk"],
    "events_scheduled":
    ["Circuit Design", "Signal Processing", "Embedded Systems"],
    "study_groups":
    ["Circuit Design", "Signal Processing", "Embedded Systems"],
    "title":
    "Alum"
}, {
    "id":
    3,
    "name":
    "Michael Jordan",
    "major":
    "N/A",
    "year":
    "Third Year",
    "role":
    "Staff",
    "title":
    "Hope Success Navigator",
    "image":
    "https://cdn.nba.com/headshots/nba/latest/1040x760/893.png",
    "description":
    "Michael is fascinated by the complexities of life and is pursuing a career in biological research.",
    "interests": ["Genetics", "Ecology", "Neuroscience"],
    "points_earned":
    40,
    "events_attended":
    ["Biological Symposium", "Research Conference", "Field Trip"],
    "events_scheduled": ["Genetics", "Ecology", "Neuroscience"],
    "study_groups": ["Genetics", "Ecology", "Neuroscience"],
}, {
    "id":
    4,
    "name":
    "Kayne West",
    "major":
    "Psychology",
    "year":
    "Fourth Year",
    "image":
    "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Kanye_West_at_the_2009_Tribeca_Film_Festival_%28crop_2%29.jpg/800px-Kanye_West_at_the_2009_Tribeca_Film_Festival_%28crop_2%29.jpg",
    "description":
    "Sophia is passionate about understanding the human mind and behavior and Jesus.",
    "interests": [
        "Cognitive Psychology", "Developmental Psychology",
        "Clinical Psychology"
    ],
    "points_earned":
    55,
    "events_attended":
    ["Psychology Conference", "Research Symposium", "Workshop"],
    "events_scheduled": [
        "Cognitive Psychology", "Developmental Psychology",
        "Clinical Psychology"
    ],
    "study_groups": [
        "Cognitive Psychology", "Developmental Psychology",
        "Clinical Psychology"
    ],
    "title":
    "Scholar"
}, {
    "id": 11,
    "name": "Cisco Amparo Ruiz",
    "major": "Computer Science",
    "role": "Student",
    "year": "Second Year",
    "image": "https://placehold.co/600x400/png",
    "description": "John is a computer science major who loves to code.",
    "interests": ["Python", "Machine Learning", "Web Development"],
    "points_earned": 50,
    "events_attended": ["Hackathon", "Conference", "Workshop"],
    "events_scheduled": ["Python", "Machine Learning", "Web Development"],
    "study_groups": ["Python", "Machine Learning", "Web Development"],
    "title": "Scholar"
}, {
    "id":
    9,
    "name":
    "Zahmir Jacobs",
    "major":
    "Electrical Engineering",
    "year":
    "Second Year",
    "image":
    "https://placehold.co/600x400/png",
    "description":
    "Daniel is fascinated by the fundamental laws governing the universe and aspires to contribute to the field of theoretical physics.",
    "interests": ["Quantum Mechanics", "Astrophysics", "Particle Physics"],
    "points_earned":
    30,
    "events_attended":
    ["Physics Colloquium", "Observatory Visit", "Quantum Computing Workshop"],
    "events_scheduled":
    ["Quantum Mechanics", "Astrophysics", "Particle Physics"],
    "study_groups": ["Quantum Mechanics", "Astrophysics", "Particle Physics"],
    "title":
    "Scholar"
}, {
    "id":
    8,
    "name":
    "Pedro Ruiz",
    "major":
    "History",
    "year":
    "Third Year",
    "image":
    "https://placehold.co/600x400/png",
    "description":
    "Linda is passionate about understanding the events and cultures of the past.",
    "interests":
    ["Ancient Civilizations", "European History", "Historical Methodology"],
    "points_earned":
    55,
    "events_attended": [
        "Historical Symposium", "Archaeological Excavation",
        "Documentary Screening"
    ],
    "events_scheduled":
    ["Ancient Civilizations", "European History", "Historical Methodology"],
    "study_groups":
    ["Ancient Civilizations", "European History", "Historical Methodology"],
    "title":
    "Scholar"
}, {
    "id":
    7,
    "name":
    "Adeolu Adeyemi",
    "major":
    "Chemical Engineering",
    "year":
    "Fourth Year",
    "image":
    "https://placehold.co/600x400/png",
    "description":
    "David is fascinated by chemical processes and their applications in various industries.",
    "interests": ["Process Control", "Polymer Chemistry", "Energy Conversion"],
    "points_earned":
    70,
    "events_attended": [
        "Chemical Engineering Symposium", "Process Optimization Workshop",
        "Industrial Visit"
    ],
    "events_scheduled":
    ["Process Control", "Polymer Chemistry", "Energy Conversion"],
    "study_groups":
    ["Process Control", "Polymer Chemistry", "Energy Conversion"],
    "title":
    "Scholar"
}, {
    "id":
    5,
    "name":
    "Kofi Addo",
    "major":
    "Civil Engineering",
    "year":
    "Third Year",
    "image":
    "https://placehold.co/600x400/png",
    "description":
    "Alex is passionate about designing infrastructure that improves people's lives.",
    "interests": [
        "Structural Engineering", "Transportation Engineering",
        "Environmental Engineering"
    ],
    "points_earned":
    60,
    "events_attended": [
        "Civil Engineering Conference", "Bridge Design Competition",
        "Sustainability Workshop"
    ],
    "events_scheduled": [
        "Structural Engineering", "Transportation Engineering",
        "Environmental Engineering"
    ],
    "study_groups": [
        "Structural Engineering", "Transportation Engineering",
        "Environmental Engineering"
    ],
    "title":
    "Scholar"
}, {
    "id": 8,
    "name": "Sarah",
    "age": 60,
    "title": "Ambassador"
}, {
    "id": 9,
    "name": "Chris",
    "age": 65,
    "title": "Ambassador"
}, {
    "id": 10,
    "name": "Emma",
    "age": 70,
    "title": "Ambassador"
}]

study_groups = [{
    "group_id":
    1,
    "group_name":
    "Python Programming",
    "meeting_times": ["Monday 3-5 PM", "Wednesday 3-5 PM", "Friday 3-5 PM"],
    "current_members":
    12,
    "associated_class":
    "Computer Science 101",
    "instructor":
    "Dr. Smith",
    "location":
    "Room 102",
    "description":
    "This group focuses on learning Python programming basics.",
    "image_link":
    "https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg"
}, {
    "group_id":
    12,
    "group_name":
    "HOPE Gateway",
    "meeting_times": ["Monday 3-5 PM", "Wednesday 3-5 PM", "Friday 3-5 PM"],
    "current_members":
    12,
    "associated_class":
    "Computer Science 101",
    "instructor":
    "Dr. Smith",
    "location":
    "Room 102",
    "description":
    "This group focuses on learning Python programming basics.",
    "image_link":
    "https://www.bhcc.edu/media/02-images/banners/HOPE_WebBanner-400x100.jpg"
}, {
    "group_id":
    3,
    "group_name":
    "Mathematics",
    "meeting_times": ["Monday 6-8 PM", "Wednesday 6-8 PM"],
    "current_members":
    10,
    "associated_class":
    "Calculus 101",
    "instructor":
    "Prof. Thompson",
    "location":
    "Room 301",
    "description":
    "Group focusing on solving mathematical problems and understanding concepts in calculus.",
    "image_link":
    "https://resilienteducator.com/wp-content/uploads/2012/11/AdobeStock_60467600_cup.jpg"
}, {
    "group_id":
    2,
    "group_name":
    "Anime/Manga",
    "meeting_times": ["Tuesday 4-6 PM", "Thursday 4-6 PM"],
    "current_members":
    8,
    "associated_class":
    "Data Analysis 202",
    "instructor":
    "Prof. Johnson",
    "location":
    "Room 205",
    "description":
    "Learn data analysis techniques and tools such as Pandas, NumPy, and Matplotlib.",
    "image_link":
    "https://assets-prd.ignimgs.com/2022/08/17/top25animecharacters-slideshow-1660779038818.jpg?crop=16%3A9&width=888"
}, {
    "group_id":
    4,
    "group_name":
    "Language Exchange:French",
    "meeting_times": ["Tuesday 5-7 PM", "Thursday 5-7 PM"],
    "current_members":
    15,
    "associated_class":
    "Language Studies 101",
    "instructor":
    None,
    "location":
    "Language Lab",
    "description":
    "Practice speaking and learning new languages in a friendly environment.",
    "image_link":
    "https://www.veritasedu.net/Content/images/french.jpg"
}, {
    "group_id":
    5,
    "group_name":
    "Study Skills",
    "meeting_times": ["Wednesday 2-4 PM", "Friday 2-4 PM"],
    "current_members":
    6,
    "associated_class":
    "Study Techniques 101",
    "instructor":
    "Ms. Rodriguez",
    "location":
    "Library Conference Room",
    "description":
    "Develop effective study habits and techniques to improve academic performance.",
    "image_link":
    "https://www.veritasedu.net/Content/images/french.jpg"
}, {
    "group_id":
    6,
    "group_name":
    "Art Appreciation",
    "meeting_times": ["Thursday 6-8 PM"],
    "current_members":
    7,
    "associated_class":
    "Art History 101",
    "instructor":
    "Prof. Martinez",
    "location":
    "Art Studio",
    "description":
    "Explore various art movements and artists while discussing and analyzing artworks.",
    "image_link":
    "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Vincent_van_Gogh_-_Road_with_Cypress_and_Star_-_c._12-15_May_1890.jpg/387px-Vincent_van_Gogh_-_Road_with_Cypress_and_Star_-_c._12-15_May_1890.jpg"
}]

campus_events = [{
    "event_id":
    1,
    "event_name":
    "Career Fair",
    "date":
    "2024-04-15",
    "time":
    "10:00 AM - 3:00 PM",
    "location":
    "Campus Gymnasium",
    "description":
    "An opportunity for students to meet with potential employers and explore job opportunities.",
    "image_link":
    "https://www.bhcc.edu/media/00-homepage/slideshowimages/CareerFair_Homepage.jpg"
}, {
    "event_id":
    3,
    "event_name":
    "Compelling Conversations: Kevin Kreider",
    "date":
    "2024-04-20",
    "time":
    "2:00 PM - 4:00 PM",
    "location":
    "Auditorium",
    "description":
    "Born in Seoul, South Korea and adopted at the age of three to a German/Irish family in Philadelphia, Kevin Kreider grew up with a loving family. But he soon found out that the outside world is not as caring. By the time he was in kindergarten, Kevin was bullied, beaten up and made fun of for being Asian. That continued through the years and he began to believe the hateful things others were telling him: Asian men were not as attractive. They were effeminate, skinny and weak. Feeling he was not white enough, and yet, not Asian enough either, Kevin set out to carve his own unique path to redefine Asian masculinity. He began to work out and finally turned into the sex symbol he always wanted to be. He left Philadelphia in 2008 to navigate his way in entertainment as a Korean American adoptee. He was signed with one of the top modeling agencies in New York City. ",
    "image_link":
    "https://image.cnbcfm.com/api/v1/image/106877965-1620143552137-GettyImages-1148387998.jpg?v=1620143610&w=740&h=416&ffmt=webp&vtcrop=yg"
}, {
    "event_id":
    4,
    "event_name":
    "Student Art Exhibition",
    "date":
    "2024-04-25",
    "time":
    "5:00 PM - 7:00 PM",
    "location":
    "Art Gallery",
    "description":
    "An exhibition showcasing artworks created by talented students from the art department.",
    "image_link":
    "https://www.bhcc.edu/media/02-images/artgallery/BHCCDistinguished-Artist-_hero.jpg"
}, {
    "event_id":
    5,
    "event_name":
    "Movie Night",
    "date":
    "2024-04-18",
    "time":
    "7:00 PM - 9:00 PM",
    "location":
    "Student Union Theater",
    "description":
    "Screening of a popular movie followed by discussions and refreshments.",
    "image_link":
    "https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg"
}, {
    "event_id":
    6,
    "event_name":
    "Community Service Day",
    "date":
    "2024-04-30",
    "time":
    "9:00 AM - 12:00 PM",
    "location":
    "Various locations",
    "description":
    "Students, faculty, and staff come together to volunteer for local community service projects.",
    "image_link":
    "https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg"
}]


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/home')
def home():
  return render_template('home.html')


@app.route('/events')
def events():
  return render_template('events.html', events=campus_events)


@app.route('/directory')
def directory():
  return render_template('directory.html', people=people)


# @app.route('/directory-test')
# def directory_test():
#   return render_template('directory_test.html', people=people)


@app.route('/profile')
def profile():
  return render_template('profile.html', people=profile_student)


@app.route('/profile-staff')
def profile_admin():
  return render_template('profile_staff.html', people=profile_staff)


@app.route('/groups')
def groups():
  return render_template('groups.html', groups=study_groups)


@app.route('/login')
def login():
  return render_template('login.html')


@app.route('/resources')
def resources():
  return render_template('resources.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
