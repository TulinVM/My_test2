from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Journal, NameAsuModel
from .forms import JournalForm, JournalFormEvent, JournalFormEventTwo
#from .views import JournalFilter

from .forms import (
    JournalForm,
)


from .filters import (
    JournalFilter,
)
###################################################
from django.views.generic import ListView
from .models import Journal, NameAsuModel, ModuleTypeModel, ModuleTypeMkcModel
from django.contrib import messages

class JournalListView(ListView):
    model = Journal
    template_name = 'journal_list.html'  # Шаблон для отображения
    context_object_name = 'journals'  # Имя переменной в шаблоне
    paginate_by = 10  # Пагинация (по желанию)

    def get_queryset(self):
        """Фильтруем записи в зависимости от параметров GET-запроса."""
        queryset = super().get_queryset()

        # Получаем выбранное значение фильтра
        selected_asu = self.request.GET.get('name_asu')
        print("Выбранное АСУ:", selected_asu)  # Вывод в консоль
       # messages.info(self.request, f"Вы выбрали АСУ: {selected_asu}")  # Вывод в браузере

        selected_uso = self.request.GET.get('name_uso')
        print("Выбранное УСО:", selected_uso)  # Вывод в консоль
        # messages.info(self.request, f"Вы выбрали УСО: {selected_uso}")  # Вывод в браузере

        selected_mkc = self.request.GET.get('name_mkc')
        print("Выбранное МКС:", selected_mkc)  # Вывод в консоль
        # messages.info(self.request, f"Вы выбрали МКС: {selected_mkc}")  # Вывод в браузере

        # Фильтруем по выбранному значению
        if selected_asu:
            messages.info(self.request, f"Вы выбрали АСУ: {selected_asu}")  # Вывод в браузере
            queryset = queryset.filter(name_asu__name=selected_asu)

        if selected_uso:
            messages.info(self.request, f"Вы выбрали УСО: {selected_uso}")  # Вывод в браузере
            queryset = queryset.filter(module_type__name=selected_uso)  

        if selected_mkc:
            messages.info(self.request, f"Вы выбрали МКС: {selected_mkc}")  # Вывод в браузере
            queryset = queryset.filter(module_type_mkc__name=selected_mkc)  


        return queryset

    def get_context_data(self, **kwargs):
        """Добавляем дополнительные данные в контекст."""
        context = super().get_context_data(**kwargs)

        # Получаем уникальные значения для выпадающего списка
        context['name_asu_choices'] = NameAsuModel.objects.values_list('name', flat=True).distinct()
        context['name_uso_choices'] = ModuleTypeModel.objects.values_list('name', flat=True).distinct()
        context['name_mkc_choices'] = ModuleTypeMkcModel.objects.values_list('name', flat=True).distinct()
        # Сохраняем выбранное значение для отображения в шаблоне
        context['selected_asu'] = self.request.GET.get('name_asu', '')
        context['selected_uso'] = self.request.GET.get('name_uso', '')
        context['selected_mkc'] = self.request.GET.get('name_mkc', '')

        return context
    
from django.shortcuts import render

def unauthorized_index(request):
    context = {}

    if request.method == "POST":
        date_def = request.POST.get("date_def")
        journal_entry = (
            Journal.objects.filter(date_def=date_def)
            .values(
                'date_def',
                'name_asu',
                'module_type',
                'module_type_mkc',
                'fault',
                'events',
            )
            .first()
        )
        context['journal_entry'] = journal_entry  # Добавляем данные в контекст

    return render(request, "index.html", context)  # Возвращаем HttpResponse
##########

# List view for Journal
from django.shortcuts import render
from .models import Journal


# Detail view for Journal
class JournalDetailView(DetailView):
    model = Journal
    template_name = 'journal_detail.html'
    context_object_name = 'journal'

# Create view for Journal
class JournalCreateView(CreateView):
    model = Journal
    form_class = JournalForm
    template_name = 'journal_create.html'
    success_url = reverse_lazy('journal_list')

# Update view for Journal
class JournalUpdateView(UpdateView):
    model = Journal
    form_class = JournalFormEvent
    template_name = 'journal_update.html'
    success_url = reverse_lazy('journal_list')

# Update Two view for Journal
class JournalUpdateViewTwo(UpdateView):
    model = Journal
    form_class = JournalFormEventTwo
    template_name = 'journal_update_two.html'
    success_url = reverse_lazy('journal_list')

# Delete view for Journal
class JournalDeleteView(DeleteView):
    model = Journal
    template_name = 'journal_delete.html'
    success_url = reverse_lazy('journal_list')

# Custom function-based view for filtering (optional)
def filter_journals(request):
    query = request.GET.get('q')
    journals = Journal.objects.filter(name_asu__name__icontains=query) if query else Journal.objects.all()
    return render(request, 'journal_list.html', {'journals': journals})
