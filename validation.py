import re
class validations:

    def validatemob(self,mob):
        pattern = re.compile(r'\d{10}')
        if(pattern.match(mob)):
            return True
        else:
            return False

    def validateeml(self,eml):
        pattern=re.compile(r'[\w\.-]+@[\w\.-]+')
        if(pattern.match(eml)):
            return True
        else:
            return False

   