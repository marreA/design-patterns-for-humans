
# Defines a dependency between objects so that whenever an object changes its state, all its dependents are notified.


class JobPost:
    
    _title = None
    
    def __init__(self, title):
        self._title = title
    
    def get_title(self):
        return self._title

class JobSeeker:
    
    _name = None
    
    def __init__(self, name):
        self._name = name
    
    def on_job_poster(self, job):
        print(f"Hi {self._name}! New job posted: {job.get_title()}")

class EmploymentAgency:
    
    _observers = list()
    
    def notify(self, job_posting):
        for obs in self._observers:
            obs.on_job_poster(job_posting)
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def add_job(self, job_posting):
        self.notify(job_posting)
        

john_doe = JobSeeker("John Doe")
jane_doe = JobSeeker("Jane Doe")

job_posting = EmploymentAgency()
job_posting.attach(john_doe)
job_posting.attach(jane_doe)
job_posting.add_job(JobPost("Software Engineer"))