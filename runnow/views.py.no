from django.shortcuts import render
from .forms import *
from formtools.wizard.views import SessionWizardView

# from django.forms import formset_factory
FORMS = [("regions", RegionFormset),
         ]

TEMPLATES = {"regions": "regions.html",
             }
#
# FORMS = [("regions", RegionFormset),
#          ("brands", BrandFormset),
#          ("servernodes", ServerNodeFormset),
#          ("configlevels", ConfigLevelFormset),
#          ("apilevels", ApiLevelFormset)]
#
# TEMPLATES = {"regions": "regions.html",
#              "brands": "brands.html",
#              "servernodes": "servernodes.html",
#              "configlevels": "configlevels.html",
#              "apilevels": "apilevels.html",
#              }


class AnswerWizard(SessionWizardView):
    def get_template_names(self):
        """

        :return: template for current step
        :rtype: file name
        """
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        """

        :param form_list: forms to process
        :type form_list:  list of forms with names
        :param kwargs:
        :type kwargs:
        :return: currently render the data
        :rtype:
        """
        return render(self.request, 'done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })

    def get_context_data(self, **kwargs):
        data = super(AnswerWizard, self).get_context_data(**kwargs)
        return data

