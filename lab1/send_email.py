from gmail import GMail, Message
from random import choice
import datetime
time = datetime.datetime.now()
gmail = GMail("hiimdangoilaxiit2610@gmail.com", "nnd26101999")
sickness_list = ["dau bung", "so mui", "di ia"]
templace = '''
<p style="text-align: left;"><em><strong>Chao sep</strong></em></p>
<p style="text-align: left;"><strong>Hom nay, em ngu day thay hoi {{sick}}, em xin nghi lam hom nay&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" /></strong></p>
<p style="text-align: left;"><strong>Xin loi sep</strong></p>
<p style="text-align: left;"><strong>ahihi</strong></p>
'''
sickness = choice(sickness_list) 
templace = templace.replace("{{sick}}", sickness) 
message = Message("Xin nghi lam", to="patphantuan251@gmail.com", html= templace)
gmail.send(message) 

      
        
        



