from django.contrib import admin
from blog_app.models import Contact,ML,DL,DS
# Register your models here.




# Media Files are used to add the static files like if we want to add the Js file or Css file into our site,so we need to define them under the Media Class




admin.site.register(ML)

admin.site.register(DL)


admin.site.register(DS)



admin.site.register(Contact)

#admin.site.register(ML)


