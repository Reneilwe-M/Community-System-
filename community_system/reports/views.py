from django.shortcuts import render, redirect
from django.contrib import messages
# from .models import IssueReport
# from .forms import IssueReportForm


from django.http import JsonResponse
from django.views.decorators.http import require_POST

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from .models import Issue
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def report_issue(request):
    if request.method == 'POST':
      
            issue_type  = request.POST.get('issue_type')
            description = request.POST.get('description')
            photo       = request.FILES.get('photo')       # handles uploaded image
            address     = request.POST.get('address')
            latitude    = request.POST.get('latitude')
            longitude   = request.POST.get('longitude')

            Issue.objects.create(
             user=request.user,
             issue_type=issue_type,
             description=description,
             address=address,
             latitude=latitude,
             longitude=longitude,
             photo=photo,
             status="Pending",
             priority="Low"
        )
            
            
   
    return render(request, 'reports/report_issue.html')


def track_issues(request):
    issues = Issue.objects.all().order_by('-created_at')
    return render(request, 'reports/track_issues.html', {'issues': issues})

from django.contrib.admin.views.decorators import staff_member_required

# @staff_member_required
# def staff_dashboard(request):

#     issues = Issue.objects.all()

#     return render(request, 'reports/staff_dashboard.html', {'issues': issues})
def staff_dashboard(request):

    issues = Issue.objects.all().order_by('-created_at')

    pending_count = issues.filter(status="Pending").count()
    progress_count = issues.filter(status="In Progress").count()
    resolved_count = issues.filter(status="Resolved").count()

    context = {
        "issues": issues,
        "pending_count": pending_count,
        "progress_count": progress_count,
        "resolved_count": resolved_count
    }

    return render(request, "reports/staff_dashboard.html", context)
def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})

from django.http import JsonResponse


def update_issue(request, issue_id):

    issue = Issue.objects.get(id=issue_id)

    if request.method == "POST":

        issue.priority = request.POST.get("priority")
        issue.status = request.POST.get("status")
        issue.save()
        issue.resolution_notes = request.POST.get("resolution_notes")
        issue.save()

        return JsonResponse({"success": True})

    return JsonResponse({"success": False})

def staff_check(user):
    return user.is_staff

# @user_passes_test(staff_check)
# def staff_dashboard(request):
#     return render(request, "reports/staff_dashboard.html")





# def report_issue(request):
#     """View 1 — Submit a new issue."""
#     if request.method == 'POST':
#         form = IssueReportForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your report has been submitted successfully!')
#             return redirect('track')
#     else:
#         form = IssueReportForm()

#     return render(request, 'reports/report_issue.html', {'form': form})


# def track_issues(request):
#     """View 2 — Track all submitted issues."""
#     reports = IssueReport.objects.all().order_by('-submitted_at')
#     return render(request, 'reports/track_issues.html', {'reports': reports})