from django.shortcuts   import render
from django.http        import HttpResponse
from django.shortcuts   import redirect

from ..models            import User, UserRole, UserJob
from ..models            import Object, ObjectType, ObjectDataType, ObjectData
from ..models            import ObjectHistory, ObjectState
from ..models            import Command, CommandState
from ..models            import Vendor


from ..forms             import UserForm, RoleForm, JobForm
from ..forms             import ObjectForm, ObjectTypeForm, ObjectDataTypeForm
from ..forms             import ObjectDataFormSet, ObjectDataTypeFormSet
from ..forms             import ObjectToStockForm, ObjectToUserForm, ObjectStateForm
from ..forms             import VendorForm, CommandForm
from ..forms             import LoginForm

from ..forms             import Command__object_form, Command__object_data_form
from ..forms             import command_object_formset, command_object_data_formset


from ..utils import render_to_pdf

from django.core.serializers import serialize
import datetime
from array              import array

from ._forms.history    import object_to_stock, object_to_user, object_state_new

from ._forms.user       import user_new, user_edit, user_delete
from ._forms.user       import job_new, job_edit
from ._forms.user       import role_new, role_edit

from ._forms.command    import command_new

from ._forms.vendor     import vendor_new

from ._forms.object     import object_new, object_type_new

from ._forms.auth      import login