from    django.contrib.auth import authenticate

from    ..forms import *

def     login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)

        user = authenticate(
            username = form['login'],
            password = form['password']
        )

        if user:
            return render(request, 'forms/object_to_stock.html', view_param)
    else:
        form = LoginForm()
    print(form)
    view_param = {
        'form': form
    }
    return render(request, 'forms/login.html', view_param)