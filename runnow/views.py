from django.shortcuts import render
from .forms import *
# from myprofile.forms import *
from formtools.wizard.views import SessionWizardView
# from django.forms import formset_factory

FORMS = [("regions", RegionFormset),
         ("roles", RoleFormset),
         ("brands", BrandFormset),
         ("servernodes", ServerNodeFormset)]
         # ("f3", ProfileFormM)]


TEMPLATES = {"regions": "regions.html",
             "roles": "roles.html",
             "brands": "brands.html",
             "servernodes": "servernodes.html"}

class AnswerWizard(SessionWizardView):
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        return render(self.request, 'done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })

    def get_context_data(self, **kwargs):
        data = super(AnswerWizard, self).get_context_data(**kwargs)
        return data

# def index(request):
#     DrinkFormSet = formset_factory(DrinkForm, extra=2, max_num=20)
#     if request.method == 'POST':
#     # TODO
#     else:
#         formset = DrinkFormSet(initial=[{'name': 1, 'size': 'm', 'amount': 1}])
#     return render(request, 'online/index.html', {'formset': formset})
# def post(request):
#         form = DistributorForm(request.POST)
#         form.product_instances = ProductFormset(request.POST)
#         if form.is_valid():
#             distributor= Distributor() #model class
#             distributor.name= form.cleaned_data('name')
#             distributor.save()
#             if form.product_instances.cleaned_data is not None:
#                 for items in form.product_instances.cleaned_data:
#                     product = Product() #Product model class
#                     product.name= item['name']
#                     product.quantity= item['quantity']
#                     product.price= item['price']
#                     product.save()
#                     distributor.products.add(product)
#             return redirect('/success')
#         return redirect('/failure')