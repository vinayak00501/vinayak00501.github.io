from django.shortcuts import HttpResponse, render, HttpResponseRedirect, redirect
from .models import Product, Order, Profile, Comment, ProductImage

from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login

from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth.decorators import login_required
from django.contrib import messages
import random
# Create your views here.


def index(request):

    try:
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)
    except:
        pass

    # sequence of data is
    # images is a list of images
    # [product_id, product_name, product_price, product_desc, primary_img, category1, category2, category3, images, img_id]

    # 0 - product_id
    # 1 - product_name
    # 2 - product_price
    # 3 - product_desc
    # 4 - primary_img
    # 5 - category1
    # 6 - category2
    # 7 - category3
    # 8 - images
    # 9 - img_id
    # 10- comments

    all_products = []
    all_categories = set()
    for p in Product.objects.all():
        product_id = p.product_id
        product_name = p.product_name
        product_price = p.product_price
        product_desc = p.product_desc
        primary_img = p.primary_img
        category1 = p.category1
        category2 = p.category2
        category3 = p.category3
        img_id = p.img_id
        # images = list(Product.objects.filter(img_id=img_id))
        images = []
        for i in Product.objects.filter(img_id=img_id):
            images.append(i.images)

        print("index", images)

        listed_product = [product_id, product_name, product_price, product_desc,
                          primary_img, category1, category2, category3, images, img_id]
        all_categories.add(category1)
        # all_categories.add(category2)
        # all_categories.add(category3)
        all_products.append(listed_product)

    # current_user = request.user
    context = {
        "product": all_products,
        "categories": list(all_categories),
        
        # "user" : user_object,
    }

    # send_mail(
    #     "hello guys subject",
    #     "this is a message",
    #     settings.EMAIL_HOST_USER,
    #     ["vinayak000501@gmail.com"],
    #     fail_silently=False,
    # )

    messages.success(request, "currently successfull")

    return render(request, 'app_shop/index.html', context)


def services(request):
    return render(request, 'app_shop/services.html')


def about(request):
    return render(request, 'app_shop/about.html')


def contact(request):
    return render(request, 'app_shop/contact.html')


def add_product(request):

    all_ids = []
    last_id = 0
    try:
        for p in Product.objects.all():
            all_ids.append(p.img_id)
            last_id = all_ids[-1]
    except:
        last_id = -1

    print(all_ids)

    if request.method == "POST":
        name = request.POST.get("name")
        if name != "":
            print('yes')
            price = int(request.POST.get("price"))
            desc = request.POST.get("desc")
            primary_img = request.FILES.get("primary_img")
            category1 = request.POST.get("category1")
            category2 = request.POST.get("category2")
            category3 = request.POST.get("category3")

            images = request.FILES.getlist('images')
            img_id = int(last_id) + 1

            # print("printed", image)
            # new_product = Product(img_id = img_id ,product_name = name, images=image)
            # new_product = Product(product_name = name, product_price = price, product_desc = desc, primary_img = primary_img, category1=category1, category2=category2, category3=category3, images=image, img_id=img_id)
            # new_product.save()

            new_product = Product()
            new_product.product_name = name
            new_product.product_price = price
            new_product.product_desc = desc
            new_product.primary_img = primary_img
            new_product.category1 = category1
            new_product.category2 = category2
            new_product.category3 = category3
            images_list = []
            # for image in images:
            #     images_list.append(str(image.url))

            # new_product.images = str(images_list)
            new_product.img_id = img_id

            new_product.save()

            name = ""
            price = ""
            desc = ""
            primary_img = ""
            category1 = ""
            category2 = ""
            category3 = ""
            images = ""
            img_id = ""

            return render(request, "app_shop/add_product.html", {"p": new_product})

    else:

        # return render(request, "app_shop/add_product.html", {"p" : Product.objects.all()})
        return render(request, "app_shop/add_product.html")


def product_view(request, p_id):
    product_view = Product.objects.filter(product_id=p_id)
    product_id = product_view[0].product_id
    product_name = product_view[0].product_name
    product_price = product_view[0].product_price
    product_desc = product_view[0].product_desc
    primary_img = product_view[0].primary_img
    category1 = product_view[0].category1
    category2 = product_view[0].category2
    category3 = product_view[0].category3
    img_id = product_view[0].img_id
    images = product_view[0]

    comments = Comment.objects.filter(product=product_view[0])
    # print(comments[0])

    
    final_product = [product_id, product_name, product_price, product_desc,
                     primary_img, category1, category2, category3, images, img_id, comments]
    

    if request.method == "POST":
        user_comment = request.POST.get("user_comment")
        comment = Comment()

        comment.product = product_view[0]
        comment.user_profile = Profile.objects.get(user=request.user)
        comment.body = user_comment

        comment.save()

    
    # for Multiple images of the Product

    images = ProductImage.objects.filter(image_of=product_view[0])
    

    

    
    context = {
        "product_view" : final_product, 
        "other_images" : images,
    }
    return render(request, 'app_shop/product_view.html', context)


def your_cart(request):
    if request.method == "POST":
        price = request.POST.get('cart_total')
        client_email = request.POST.get('input_email')
        p = request.POST.get('cart_items_input')

        # for taking cart products array from js using JSON
        try:
            from simplejson import json
        except:
            import json
        l = json.loads(p)
        print("this l", l)

        # organizing cart items
        new_order = Order(order_item=l)
        new_order.save()

        # for sending email
        # product index
        # 0 - id
        # 1 - Name
        # 2 - price
        # 3 - quantity

        def generate_ordered_email(order_list, total_price):

            email_text = ""
            email_text += "Welcome To fantasy Store\n\n"
            email_text += "\nYour Order Items are --\n"
            for serial_no, product in enumerate(order_list):

                product_name = product[1]
                price_ = product[2]
                price = int(price_.replace("RS ", ""))
                qunatity = int(product[3])
                multiplied_price = str(price*qunatity)

                email_text += "\n" + f"{serial_no + 1}." + \
                    " " + product_name + "   -   "
                email_text += "\n" + "RS " + \
                    str(price) + " x " + str(qunatity) + " = " + \
                    "RS " + str(multiplied_price) + "\n"
            email_text += "\n\n" + "Your Total" + "   --   " + "RS " + total_price
            email_text += "\n\nThank You for Shopping with us :)"
            email_text += "\n" + "Any Queries are Welcomed"
            email_text += "\n" + "contact us at ---  hello@gmail.com"
            email_text += "\n\n" + "Fantasy Stores Ltd."

            return email_text

        final_email_text = generate_ordered_email(l, price)
        send_mail(
            "Your Order at Fantasy Stores",
            final_email_text,
            settings.EMAIL_HOST_USER,
            ['bhuvan00501@gmail.com', 'komal55501@gmail.com', client_email],
            fail_silently=False,
        )

    return render(request, 'app_shop/product_cart.html')


def login_(request):
    if request.method == "POST":
        username = request.POST.get('login_username')
        password = request.POST.get('login_pass')
        user = authenticate(username=username, password=password)
        if user is not None:
            try:
                login(request, user)
                print("logged", user)
                return redirect(request, "app_shop/index.html")
            except:
                
                return index(request)
                pass
            # finally:
            #     return index(request)
        else:
            print(user)
            print(username, password)
            return redirect("login_")
    else:
        print("else")
        return render(request, "app_shop/login_.html")


def signup_(request):
    context = {
        "state" : "cleared_nothing", 
        "error" : "none",
    }

    if request.method == "POST":
        email = request.POST.get("input_email")
        user_otp = request.POST.get("input_otp")
        username = request.POST.get("input_username")
        
        if email :
            otp = random.randint(1000, 9999)
            context["otp"] = otp
            context["email"] = email
            context["state"] = "cleared_sent_otp"
            send_mail(
            otp,
            f"This is your otp for email {email}\n otp  :   <b>{otp}<b>",
            settings.EMAIL_HOST_USER,
            ['komal55501@gmail.com', email],
            fail_silently=False,
            )

        if user_otp:
            js_otp = request.POST.get("js_otp")
            print(js_otp, "js")
            print(user_otp, "otp")
            if js_otp == user_otp:
                context["state"] = "cleared_otp"
        
        if username:
            print(username)
            print("object", bool(User.objects.filter(username=username)))

            password1 = request.POST.get("input_password1")
            password2 = request.POST.get("input_password2")
            email = request.POST.get("email_input_last")

            if password1 == password2:

                def generate_redirect(message, page_link, context_state, context_error):
                    messages.error(request, message)
                    redirect(page_link)
                    context['state'] = context_state
                    context['error'] = context_error

                # username error
                if User.objects.filter(username=username):
                    generate_redirect("This is username error", "app_shop/signup_/html", "cleared_otp", "username")

                # username equal password
                if username == password1:
                    generate_redirect("Password can't be same as Username", "app_shop/signup_/html", "cleared_otp", "internal_password_error")

                # length short
                elif len(password1) <= 8:
                    generate_redirect("Length of password must be more than 8 characters", "app_shop/signup_/html", "cleared_otp", "internal_password_error")

                # all decimal
                elif password1.isdecimal():
                    generate_redirect("Password can't be all Numbers", "app_shop/signup_/html", "cleared_otp", "internal_password_error")

                # all alphabet
                elif password1.isalpha():
                    generate_redirect("Password can't be all Alphabets", "app_shop/signup_/html", "cleared_otp", "internal_password_error")

            else:
                messages.info(request, "Password Doesn't Match")
                redirect("app_shop/signup_.html")
                context['state'] = "cleared_otp"
                context['error'] = "password"

            # saving all data in database
            if username and email and password1 and password2:
                try:
                    profile_model = Profile()

                    # user model
                    user_model = User.objects.create(username=username, password=password1, email=email)
                    user_model.save()

                    # profile model
                    profile_model.user = user_model
                    profile_model.profile_img = "app_shop/default_img.png"
                    profile_model.save()
                except:
                    print("save error")
                    print(username)
                    print(password1)
                    print(password2)
                    print(email)

            print(username)
            print(password1, password2)
            print(email)

        
                
                


        



        



    
    return render(request, "app_shop/signup_.html", context)


def profile(request):

    if request.method == "POST":
        new_username = request.POST.get('new_change_profile_username', request.user.username)
        new_location = request.POST.get('new_change_profile_location', Profile.objects.get(user=request.user).location)
        new_bio = request.POST.get('new_change_profile_bio', Profile.objects.get(user=request.user).bio)
        # new_img = request.POST.get('new_change_profile_img', Profile.objects.get(user=request.user).profile_img)

        profile = Profile.objects.get(user = request.user)
        profile.location = new_location
        profile.bio = new_bio
        # profile.profile_img = new_img
        user_ = request.user
        user_.username = new_username

        user_.save()
        profile.user = user_
        profile.save()
        
    else:
        print("failed correction")

    return render(request, "app_shop/profile.html")
