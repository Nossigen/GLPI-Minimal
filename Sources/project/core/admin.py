from django.contrib     import admin

# User
from .models            import User, UserRole, UserJob

admin.site.register(User)
admin.site.register(UserRole)
admin.site.register(UserJob)

# Object
from .models            import Object, ObjectType, ObjectData, ObjectDataType

admin.site.register(Object)
admin.site.register(ObjectType)
admin.site.register(ObjectData)
admin.site.register(ObjectDataType)

# History
from .models            import ObjectHistory, ObjectState

admin.site.register(ObjectHistory)
admin.site.register(ObjectState)

# Command
from .models            import Command, CommandState, Vendor


admin.site.register(Command)
admin.site.register(CommandState)
admin.site.register(Vendor)
