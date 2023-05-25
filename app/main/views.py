from django.shortcuts import render
from django.views import View


# Create your views here.
class IndexView(View):
    template_name = "index.main.html"
    # model = Project_SC

    def get(self, request, *args, **kwargs):
        # projectos = self.model.objects.all()

        # print("➡ projectos :", projectos[0].file.name)
        # print("➡ projectos :", projectos[0].file.url)

        return render(request, self.template_name)

    # def post(self, request, *args, **kwargs):
    #     return HttpResponse('POST request!')
