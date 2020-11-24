class student:
	count = 0
	grade = []
	def average():
		return 0 if student.count == 0 else sum(student.grade)/student.count

student.count = int(input())
student.grade += [int(i) for i in input().split(' ')]
print(student.average())