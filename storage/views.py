from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from storage.models import Contact,ContactRelation
# Create your views here.

def storage(request):
    return render(request,'storage/index.html')

def contactStorage(request):
    if request.method=='GET':
        relations = ContactRelation.objects.all()
        context={'relations':relations}
        return render(request,'storage/contact_storage.html',context)
    if request.method=='POST':
        if not request.user.is_authenticated:
            messages.warning(request,'login required!')
            return redirect('login')
        contact_name = request.POST.get('contact_name','no name') 
        contact_number = request.POST.get('contact_number',0) 
        contact_relation = request.POST.get('contact_relation','not specified')

        
        if contact_relation=='Select':
            print('relation not specified')
            contact_relation = ContactRelation.objects.get(relation_type='Other')
        else:
            relation_exist=ContactRelation.objects.filter(relation_type=contact_relation).exists()
            if not relation_exist:
                messages.warning(request,'Relation of this tupe not exist')
                return redirect('contactStorage')
            contact_relation = ContactRelation.objects.get(relation_type=contact_relation)

        number_exists=Contact.objects.filter(number=contact_number).exists()
        if number_exists:
            messages.warning(request,'Contact number exist')
            return redirect('contactStorage')
        contact=Contact(user=request.user,name=contact_name,number=contact_number,relation=contact_relation)
        contact.save()
        messages.success(request, f'Contact saved! name : {contact_name}, number : {contact_number}, relation : {contact_relation}') 
        return redirect('contactStorage')
        # return HttpResponse(f'Contact saved! <hr><h2>name : {contact_name}, number : {contact_number}, relation : {contact_relation}</h2>')
# @login_required(login_url='/accounts/login/')
def contactSearch(request):
    if not request.user.is_authenticated:
        messages.warning(request,'Login required!')
        return redirect('login')
    
    contact_name = request.POST.get('contact_name') 
    contact_number = request.POST.get('contact_number') 
    contact_relation = request.POST.get('contact_relation')
    print(f'name : {contact_name},number : {contact_number}, relation : {contact_relation}')
    if not contact_name and not contact_number and not contact_relation:
        print('no field specified')
        contacts = Contact.objects.all()
    if contact_name:
        print('contact name')
        contacts = Contact.objects.filter(user=request.user,name=contact_name)
    if contact_number:
        print('contact number')
        contacts = Contact.objects.filter(user=request.user,number=contact_number)  
    if contact_relation:
        print('contact relation')
        relation = ContactRelation.objects.get(relation_type=contact_relation)
        contacts = Contact.objects.filter(user=request.user,relation=relation)
    if contact_name and contact_number:
        print('name and number')
        contacts = Contact.objects.filter(user=request.user,name=contact_name,number=contact_number)
        
    if contact_name and contact_relation:
        print('name and relation')
        relation = ContactRelation.objects.get(relation_type=contact_relation)
        contacts = Contact.objects.filter(user=request.user,name=contact_name,relation=relation)
    
    if contact_number and contact_relation:
        print('number and relation')
        relation = ContactRelation.objects.get(relation_type=contact_relation)
        contacts = Contact.objects.filter(user=request.user,number=contact_number,relation=relation)
        
    if contact_name and contact_number and contact_relation:
        print('all fields')
        relation = ContactRelation.objects.get(relation_type=contact_relation)
        contacts = Contact.objects.filter(user=request.user,name=contact_name,number=contact_number,relation=relation)
      
    
    return render(request,'storage/contact_searched.html',{'contacts':contacts,'results':contacts.count()})
    # return HttpResponse(f'Contacts found! <hr><h2>name : {contact_name}, number : {contact_number}, relation : {contact_relation}</h2>')

        