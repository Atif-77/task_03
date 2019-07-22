from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {

    "my_list": [
       {"restaurant_name": "krm", "food_type": "gril"},

       {"restaurant_name": "shbra", "food_type": "kbsh"},

       {"restaurant_name": "sndbad", "food_type": "shawrma"},
    ]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {

    	"my_object": [
    		{"restaurant_name": "shbra", "food_type": "kbsh"},    	
    		]

    }
    return render(request, 'detail.html', context)
