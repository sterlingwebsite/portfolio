from django.shortcuts import render, get_object_or_404
from .models import Project
from django.db.models import Q

def home(request):
    projects = Project.objects.all().order_by('-created_at')
    
    search_query = request.GET.get('search', '')
    category_filter = request.GET.get('category', '')
    
    # Search across multiple fields
    if search_query:
        projects = projects.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(tech_stack__icontains=search_query) |
            Q(github_link__icontains=search_query) |
            Q(category__icontains=search_query)
        )
    
    if category_filter:
        projects = projects.filter(category=category_filter)
    
    categories = Project.objects.values_list('category', flat=True).distinct()
    
    context = {
        'projects': projects,
        'categories': categories,
        'search_query': search_query,
        'category_filter': category_filter,
    }
    return render(request, 'home.html', context)

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, 'project_detail.html', {'project': project})

def contact(request):
    if request.method == 'POST':
        # Handle form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        return render(request, 'contact.html', {'success': True})
    
    return render(request, 'contact.html')