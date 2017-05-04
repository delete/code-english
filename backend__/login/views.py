import json

from django.http import Http404, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.views import (
    login as login_view,
    logout as logout_view,
    password_reset as password_reset_view,
    password_reset_done as password_reset_done_view,
    password_reset_confirm as password_reset_confirm_view,
    password_reset_complete as password_reset_complete_view
)

from .models import User, Interest, Message
from .forms import (
    UserSignupForm, UserLoginForm, UserForm, InterestForm
)
from .utils import default_token_generator, to_dict, serialize_to_json


# def user_signup(request):
#     if request.method == 'POST':
#         f = UserSignupForm(request.POST)
#         if f.is_valid():
#             user = f.save()

#             user = authenticate(
#                 email=f.cleaned_data['email'],
#                 password=f.cleaned_data['password']
#             )
#             login(request, user)

#             user.send_verification_mail(request)

#             return redirect('users:dashboard')
#     else:
#         f = UserSignupForm()

#     return render(request, 'users/user_signup.html', {
#         'form': f
#     })


def user_login(request):
    # if request.user.is_authenticated():
    #     return redirect('users:dashboard')
    return login_view(
        request,
        authentication_form=UserLoginForm,
        template_name='login.html'
    )


# def user_logout(request):
#     return logout_view(request, next_page='core:index')


# @login_required
# def user_verification(request):
#     if request.method == 'POST':
#         request.user.send_verification_mail(request)

#     return render(request, 'users/user_verification.html')


# def user_verify(request, uidb64, token):
#     try:
#         uid = urlsafe_base64_decode(uidb64)
#         user = User.objects.get(pk=uid)
#     except (ValueError, User.DoesNotExist):
#         raise Http404

#     if default_token_generator.check_token(user, token):
#         user.is_verified = True
#         user.save()

#         return redirect('users:user_verify_done')
#     else:
#         raise Http404


# def user_verify_done(request):
#     return render(request, 'users/user_verify_done.html')


# def user_password_reset(request):
#     return password_reset_view(
#         request,
#         template_name='users/user_password_reset.html',
#         email_template_name='users/user_password_reset_email.html',
#         subject_template_name='users/user_password_reset_subject.txt',
#         post_reset_redirect='users:password_reset_done'
#     )


# def user_password_reset_done(request):
#     return password_reset_done_view(
#         request,
#         template_name='users/user_password_reset_done.html',
#     )


# def user_password_reset_confirm(request, uidb64, token):
#     return password_reset_confirm_view(
#         request,
#         token=token,
#         uidb64=uidb64,
#         template_name='users/user_password_reset_confirm.html',
#         post_reset_redirect='users:password_reset_complete'
#     )


# def user_password_reset_complete(request):
#     return password_reset_complete_view(
#         request,
#         template_name='users/user_password_reset_complete.html'
#     )


@login_required
def update_user_profile(request):
    context = {}
    user_pk = request.user.pk
    user = get_object_or_404(User, pk=user_pk)

    if request.method == 'POST':
        response = {}
        post = json.loads(request.body)

        form = UserForm(post, instance=user)
        if form.is_valid():
            form.save()
            response['message'] = 'User edited successfully!'
        else:
            response['message'] = 'Error on edit user profile!'

        return JsonResponse(response)

    context['user'] = to_dict(user)
    return render(
        request,
        'update_profile.html',
        context
    )


@login_required
def dashboard(request):
    context = {}
    user = request.user

    context['user'] = to_dict(user)
    context['teaching_to'] = serialize_to_json(
        user.relationship_user_teacher.all()
    )
    context['learning_from'] = serialize_to_json(
        user.relationship_user_student.all()
    )
    context['interests'] = serialize_to_json(user.interests.all())
    return render(
        request,
        'dashboard.html',
        context
    )


# @login_required
# def update_interests(request):
#     context = {}
#     user = request.user

#     if request.method == 'POST':
#         form = InterestForm(request.POST)
#         if form.is_valid():
#             interest = form.save(commit=False)
#             interest.user = user
#             interest.save()
#             messages.success(request, 'User edited successfully!')
#             return redirect(reverse('users:update_interests'))
#     else:
#         form = InterestForm()

#     context['form'] = form
#     context['user'] = user
#     context['interests'] = user.interests.all()
#     return render(request, 'users/user_interests.html', context)


# @login_required
# def remove_interest(request, pk):
#     interest = get_object_or_404(Interest, pk=pk)
#     interest.delete()
#     messages.success(request, 'Interest removed successfully!')

#     return redirect(reverse('users:update_interests'))


# @login_required
# def notifications(request):
#     context = {}
#     user = request.user

#     context['user'] = user
#     context['messages_received'] = user.messages_receiver.all()
#     return render(request, 'users/notifications.html', context)


# @login_required
# def user_explore(request):
#     context = {}
#     user = request.user
#     user_subject_learn = [
#         u.subject.name for u in user.interests.filter(iam='S')
#     ]
#     user_subject_teach = [
#         u.subject.name for u in user.interests.filter(iam='T')
#     ]
#     teacher_users = [
#         i.user for i in Interest.objects.filter(
#             subject__name__in=user_subject_learn, iam='T'
#         )
#     ]
#     student_users = [
#         i.user for i in Interest.objects.filter(
#             subject__name__in=user_subject_teach, iam='S'
#         )
#     ]
#     context['teacher_users'] = teacher_users
#     context['student_users'] = student_users
#     return render(request, 'users/explore.html', context)


# @login_required
# def remove_message(request, pk):
#     interest = get_object_or_404(Message, pk=pk)
#     interest.delete()
#     messages.success(request, 'Message removed successfully!')

#     return redirect(reverse('users:notifications'))
# Contact GitHub API Training Shop Blog About
