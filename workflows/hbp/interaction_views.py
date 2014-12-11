from django.shortcuts import render

def hbp_construct_query(request, input_dict,output_dict,widget):
    return render(request, 'interactions/hbp_construct_query.html',
        {'widget':widget})

def hbp_filter_integers(request,input_dict,output_dict,widget):
    return render(request, 'interactions/hbp_filter_integers.html',
        {'widget':widget,'intList':input_dict['intList']})