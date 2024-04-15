class SalileshVerma:
  def __init__(self):
      self.name = "Salilesh Verma"
      self.role = "Computer Science Student"
      self.technologies = [
          "Frontend Development",
          "Machine Learning",
          "Deep Learning",
          "C++",
          "Data Structures & Algorithms"
      ]
      self.learning = ["Backend Development", "Cloud Computing"]
      self.hobbies = ["Exploring New Tech", "Coding Challenges", "Reading Sci-Fi"]

  def say_hello(self):
      print("Hey fellow coders! Welcome to my GitHub profile! 🚀")

  def show_technologies(self):
      print("💻 Technologies I'm familiar with:")
      for tech in self.technologies:
          print(f"- {tech}")

  def show_learning(self):
      print("📚 Currently diving into:")
      for tech in self.learning:
          print(f"- {tech}")

  def show_hobbies(self):
      print("🌟 When I'm not coding, you can find me:")
      for hobby in self.hobbies:
          print(f"- {hobby}")

salilesh = SalileshVerma()
salilesh.say_hello()
salilesh.show_technologies()
salilesh.show_learning()
salilesh.show_hobbies()
