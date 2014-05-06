# from datetime import datetime
#
# from django.contrib.auth import logout
# from django.contrib.auth.decorators import login_required
# from django.core.urlresolvers import reverse_lazy
# from django.utils.decorators import method_decorator
# from django.views.generic import TemplateView, RedirectView
# from django.views.generic.edit import FormView
#
#
# class LoginRequiredMixin(object):
#     @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)
#
#
# class ItemView(LoginRequiredMixin, FormView):
#     template_name = 'item/add.html'
#     form_class = ItemForm
#     success_url = reverse_lazy('home')
#
#     def __init__(self, **kwargs):
#         super(ItemView, self).__init__(**kwargs)
#
#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         # form.send_email()
#         form.save()
#
#         return super(ItemView, self).form_valid(form)
#
#     def post(self, request, *args, **kwargs):
#         return super(ItemView, self).post(request, *args, **kwargs)
#
#
# class UserLogout(RedirectView):
#     url = reverse_lazy('app_home')
#
#     @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         logout(request)
#
#         return super(RedirectView, self).dispatch(request, *args, **kwargs)
