from django.contrib.auth.hashers import check_password

from users.models import B_User

class UserAuthenticationModel(object):

    MODEL = B_User

    def authenticate(self, email , password):
        if email and password:
            try:
                user = self.MODEL.objects.get(email = email)
                if check_password(password=password, encoded=user.password):
                    return user
                return None
            except self.MODEL.DoesNotExist:
                return None
        return None
    
    def get_user(self,user_id):

        try:
            user = self.MODEL.objects.get(pk =user_id)
            return user
        except self.MODEL.DoesNotExist:
            return None
        except self.MODEL.MultipleObjectsReturned:
            return None
    