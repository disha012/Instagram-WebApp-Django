# Create your views here.
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from oslapp.forms import SignUpForm, DocumentForm, FooForm  # , ProfileForm
from oslapp.token import account_activation_token
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.decorators import login_required
from oslapp.models import Document, Profile
from django.forms.models import model_to_dict
# from django.shortcuts import get_object_or_404
from friendship.models import Friend, Follow
# from django.http import JsonResponse


@login_required(login_url='/login/')
def home(request):
    # try:
        p = FooForm(data=model_to_dict(Profile.objects.get(user=request.user)))
        d = Document.objects.filter(user=request.user)
        print(d)
        q = Profile.objects.all()
        following = Follow.objects.following(request.user)
        followers = Follow.objects.followers(request.user)
        print(q)
        return render(request, 'home.html', {'profile': p, 'document': d, 'search': q, 'followers': followers, 'following': following})

    # except Exception:
    #     return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        # pform = ProfileForm(request.POST, request.FILES)
        if form.is_valid():  # and pform.is_valid():
            user = form.save()  # commit=False)
            user.is_active = False
            user.refresh_from_db()
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.is_private = form.cleaned_data.get('is_private')
            user.profile.bio = form.cleaned_data.get('bio')
            # user.dp = form.cleaned_data.get('dp')
            user.save()
            # profile = pform.save()
            # profile.user = user
            # profile.save()
            current_site = get_current_site(request)
            subject = 'Activate Your Insta Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')


@login_required(login_url='/login/')
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = form.save()
            newdoc.user = request.user
            newdoc.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })


@login_required(login_url='/login/')
def profileview(request, username):
    user = User.objects.get(username=username)
    print(user)
    a = 0
    following = Follow.objects.following(request.user)
    for i in following:
        if user == i:
            a = 1
    if a == 0 and request.user != user:
        return render(request, 'is_private.html', {'user': user})
    else:
        p = FooForm(data=model_to_dict(Profile.objects.get(user=user)))
        d = Document.objects.filter(user=user)
        # print(d[0].votes.up(user.id))
        abc = []
        for docu in d:
            abc.append(docu.votes.count())
        # abc = d[0].votes.user_ids()[0][0]
        # print(abc)
        # abcd = User.objects.get(id=abc)
        # print(abcd)
        q = Profile.objects.all()
        return render(request, 'home.html', {'profile': p, 'document': d, 'votes': abc, 'userss': user, 'search': q})


'''
def like(request, document_id):
    d = Document.objects.get(id=document_id)
    d.votes.up(request.user.id)
'''

'''
@login_required(login_url='/login/')
def follow_user(request, user_profile_id):
    profile_to_follow = get_object_or_404(User, =user_profile_id)
    user_profile = request.user.userprofile
    data = {}
    if profile_to_follow.follows.filter(id=user_profile.id).exists():
        data['message'] = "You are already following this user."
    else:
        profile_to_follow.follows.add(user_profile)
        data['message'] = "You are now following {}".format(profile_to_follow)
    return JsonResponse(data, safe=False)
'''


@login_required(login_url='/login/')
def follow_user(request, username):
    user = User.objects.get(username=username)
    Follow.objects.add_follower(request.user, user)
    return redirect('profile_view', username=username)



@login_required(login_url='/login/')
def follower(request, username):
    user = User.objects.get(username=username)
    followers = Follow.objects.followers(user)
    user = User.objects.get(username=username)
    return render(request, 'home.html', {'followers': followers, 'userss': user})


@login_required(login_url='/login/')
def following(request, username):
    user = User.objects.get(username=username)
    following = Follow.objects.following(user)
    user = User.objects.get(username=username)
    return render(request, 'home.html', {'following': following, 'userss': user})


@login_required(login_url='/login/')
def upvote(request, username, photo_id):
    photo = Document.objects.get(id=photo_id)
    photo.votes.up(request.user.id)
    print(username)
    return redirect('profile_view', username=username)


@login_required(login_url='/login/')
def listofupvotes(request, username, photo_id):
    photo = Document.objects.get(id=photo_id)
    listofupvote = photo.votes.user_ids()
    a = []
    b = []
    for l in listofupvote:
        c = User.objects.get(id=l[0])
        a.append(c)
        b.append(l[1])
    print(a)
    print(b)
    user = User.objects.get(username=username)
    p = FooForm(data=model_to_dict(Profile.objects.get(user=user)))
    d = Document.objects.filter(user=user)
    # print(d[0].votes.up(user.id))
    abc = []
    for docu in d:
        abc.append(docu.votes.count())
    # abc = d[0].votes.user_ids()[0][0]
    # print(abc)
    # abcd = User.objects.get(id=abc)
    # print(abcd)
    q = Profile.objects.all()
    return render(request, 'home.html', {'profile': p, 'document': d, 'votes': abc, 'userss': user, 'search': q, 'upvoteid': a, 'upvotedate': b, })


@login_required(login_url='/login/')
def deletephoto(request, username, photo_id):
    photo = Document.objects.get(id=photo_id)
    user = User.objects.get(username=username)
    p = FooForm(data=model_to_dict(Profile.objects.get(user=user)))
    d = Document.objects.filter(user=user)
    abc = []
    for docu in d:
        abc.append(docu.votes.count())
    q = Profile.objects.all()
    if(photo.user == request.user):
        photo.delete()
        deleteFailed = 'Deleted successfully'
        return render(request, 'home.html', {'profile': p, 'document': d, 'votes': abc, 'userss': user, 'search': q, 'deleteFailed': deleteFailed})
    else:
        deleteFailed = "Can't delete someone's photo"
        return render(request, 'home.html', {'profile': p, 'document': d, 'votes': abc, 'userss': user, 'search': q, 'deleteFailed': deleteFailed})


@login_required(login_url='/login/')
def search(request):
    d = Document.objects.all().order_by('-uploaded_at')
    return render(request, 'search.html', {'document': d})
