# from django import forms
# # from .models import IssueReport


# class IssueReportForm(forms.ModelForm):
#     class Meta:
#         model = IssueReport
#         fields = ['issue_type', 'description', 'photo']
#         widgets = {
#             'issue_type':  forms.Select(attrs={'class': 'form-select'}),
#             'description': forms.Textarea(attrs={
#                 'class': 'form-textarea',
#                 'rows': 4,
#                 'placeholder': 'Describe the issue...',
#             }),
#             'photo': forms.ClearableFileInput(attrs={'class': 'form-file'}),
#         }