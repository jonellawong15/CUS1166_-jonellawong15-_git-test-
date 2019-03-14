<head> Welcome! 
</head>

{% extends 'layout.html' %}
{% block body %}
<form action="{{ url_for('messenger') }}" method="post">
<input type="text" name="name" placeholder="Enter your name">
<input type="text" name="message" placeholder="Type in a course">
<button type="Submit"> Send Message</button>
</form>
{% endblock %}

def add_course():
  name = request.form.get("name")
  message = request.form.get("course")
  return render_template("course_details.html", name=name, course=course)

def register_student():
  {% get {{student_name}} %}


