from django.shortcuts import render,redirect,get_object_or_404
from userapp.models import *
from django.contrib.auth import logout
import datetime
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def admin_login(request):
    if request.method=='POST':
        unm= request.POST["username"]
        pas = request.POST["password"]

        if unm=="admin" and pas=="admin@123":
            print("Login successfully!")
            return redirect("admin_dashboard")
        else:
            print("Error! Login Failed!")
    return render(request,'admin_login.html')

def admin_dashboard(request):
    total_user=Usersignup.objects.count()
    total_note=Notesdata.objects.count()
    pending_count = Notesdata.objects.filter(status="Pending").count()
    approval_count = Notesdata.objects.filter(status="Approve").count()
    rejeted_count = Notesdata.objects.filter(status="Reject").count()
    return render(request,'admin_dashboard.html',{'total_user':total_user,'total_note':total_note,'pending_count':pending_count,'approval_count':approval_count,'rejeted_count':rejeted_count})

def admin_manage_users(request):
    udata=Usersignup.objects.all()
    return render(request,'admin_manage_users.html',{'udata':udata})

def admin_manage_notes(request):
    ndata=Notesdata.objects.all()
    return render(request,'admin_manage_notes.html',{'ndata':ndata})

def adminlogout(request):
    logout(request)
    return redirect("admin_login")

def admin_user_delete(request,uid):
    udata = Usersignup.objects.get(id=uid)
    udata.delete()
    return redirect('admin_manage_users')

def approve_note(request,id):
    nid = get_object_or_404(Notesdata,id=id)
    nid.status="Approve"
    nid.updated_at=datetime.datetime.now()
    nid.save()
    print("Approve notes!")

    # #email sending code
    # sub = "Your Note Has Been Approved!"
    # msg = f"""Dear User,

    # We are happy to inform you that your note has been approved by the admin.

    # Note Title : {nid.title}

    # You can now access and manage your note in your account.

    # Thanks & Regards!
    # NotesApp Team
    # +91 9773077345 | www.tops-int.com
    # """

    # from_ID = settings.EMAIL_HOST_USER
    # to_ID = [nid.user.email]

    # send_mail(subject=sub, message=msg, from_email=from_ID, recipient_list=to_ID)

    sub = "Your Note Has Been Approved!"

    html_msg = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Note Approved</title>
    </head>
    <body style="margin:0; padding:0; background-color:#f4f6f8; font-family:Arial, sans-serif;">

        <table width="100%" cellpadding="0" cellspacing="0">
            <tr>
                <td align="center" style="padding:30px 0;">
                    
                    <table width="600" cellpadding="0" cellspacing="0" style="background:#ffffff; border-radius:8px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
                        
                        <!-- Header -->
                        <tr>
                            <td style="background:#22c55e; padding:20px; border-radius:8px 8px 0 0; text-align:center;">
                                <h2 style="color:#ffffff; margin:0;">Note Approved 🎉</h2>
                            </td>
                        </tr>

                        <!-- Body -->
                        <tr>
                            <td style="padding:25px; color:#333333;">
                                <p>Dear User,</p>

                                <p>
                                    We are happy to inform you that your note has been 
                                    <strong style="color:#22c55e;">approved</strong> by the admin.
                                </p>

                                <p style="background:#f1f5f9; padding:12px; border-left:4px solid #22c55e;">
                                    <strong>Note Title:</strong> {nid.title}
                                </p>

                                <p>
                                    You can now access and manage your note in your account.
                                </p>

                                <p style="margin-top:30px;">
                                    Thanks & Regards,<br>
                                    <strong>NotesApp Team</strong><br>
                                    +91 9773077345<br>
                                    <a href="https://www.tops-int.com" style="color:#0ea5e9; text-decoration:none;">
                                        www.tops-int.com
                                    </a>
                                </p>
                            </td>
                        </tr>

                        <!-- Footer -->
                        <tr>
                            <td style="background:#f8fafc; text-align:center; padding:12px; font-size:12px; color:#6b7280; border-radius:0 0 8px 8px;">
                                © 2025 NotesApp. All rights reserved.
                            </td>
                        </tr>

                    </table>

                </td>
            </tr>
        </table>

    </body>
    </html>
    """

    from_ID = settings.EMAIL_HOST_USER
    to_ID = [nid.user.email]

    send_mail(
        subject=sub,
        message="",              # plain text optional
        from_email=from_ID,
        recipient_list=to_ID,
        html_message=html_msg    # 👈 HTML content
    )


    return redirect("admin_manage_notes")
   
    
def reject_note(request,id):
    nid = get_object_or_404(Notesdata,id=id)
    nid.status="Reject"
    nid.updated_at=datetime.datetime.now()
    nid.save()
    print("Reject notes!")

    sub = "Your Note Has Been Rejected"

    html_msg = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Note Rejected</title>
    </head>
    <body style="margin:0; padding:0; background-color:#f4f6f8; font-family:Arial, sans-serif;">

        <table width="100%" cellpadding="0" cellspacing="0">
            <tr>
                <td align="center" style="padding:30px 0;">
                    
                    <table width="600" cellpadding="0" cellspacing="0" style="background:#ffffff; border-radius:8px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
                        
                        <!-- Header -->
                        <tr>
                            <td style="background:#ef4444; padding:20px; border-radius:8px 8px 0 0; text-align:center;">
                                <h2 style="color:#ffffff; margin:0;">Note Rejected ❌</h2>
                            </td>
                        </tr>

                        <!-- Body -->
                        <tr>
                            <td style="padding:25px; color:#333333;">
                                <p>Dear User,</p>

                                <p>
                                    We regret to inform you that your note has been 
                                    <strong style="color:#ef4444;">rejected</strong> by the admin.
                                </p>

                                <p style="background:#fef2f2; padding:12px; border-left:4px solid #ef4444;">
                                    <strong>Note Title:</strong> {nid.title}
                                </p>

                                <p style="margin-top:15px;">
                                    <strong>Reason:</strong><br>
                                    Your note does not meet our content guidelines.
                                </p>

                                <p>
                                    You may update and resubmit your note for approval.
                                </p>

                                <p style="margin-top:30px;">
                                    Thanks & Regards,<br>
                                    <strong>NotesApp Team</strong><br>
                                    +91 9773077345<br>
                                    <a href="https://www.tops-int.com" style="color:#0ea5e9; text-decoration:none;">
                                        www.tops-int.com
                                    </a>
                                </p>
                            </td>
                        </tr>

                        <!-- Footer -->
                        <tr>
                            <td style="background:#f8fafc; text-align:center; padding:12px; font-size:12px; color:#6b7280; border-radius:0 0 8px 8px;">
                                © 2025 NotesApp. All rights reserved.
                            </td>
                        </tr>

                    </table>

                </td>
            </tr>
        </table>

    </body>
    </html>
    """

    from_ID = settings.EMAIL_HOST_USER
    to_ID = [nid.user.email]

    send_mail(
        subject=sub,
        message="",                # plain text optional
        from_email=from_ID,
        recipient_list=to_ID,
        html_message=html_msg      # 👈 HTML content
    )

    return redirect("admin_manage_notes")


def admin_show_contact(request):
    cdata=Usercontact.objects.all()
    return render(request,'admin_show_contact.html',{'cdata':cdata})

def admin_contact_delete(request,cid):
    cdata = Usercontact.objects.get(id=cid)
    cdata.delete()
    return redirect('admin_show_contact')

def admin_user_view(request, id):
    user = Usersignup.objects.get(id=id)
    return render(request, 'admin_user_view.html', {'user': user})

def admin_manage_notes_cards(request):
    status = request.GET.get('status')

    if status:
        ndata = Notesdata.objects.filter(status=status)
    else:
        ndata = Notesdata.objects.all()

    return render(request, 'admin_manage_notes.html', {'ndata': ndata})


    


