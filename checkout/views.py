from django.shortcuts import render, reverse, redirect
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JCoadCrmKjt13iyY26bqCs3KhQt7Rj0Gg5r7SFM3kPt8Md8fN5dSjd7L1UkxuN1RAA52lhkhPXYoh7ZdwYqvlSI00fBUfe5aa',
        'client_secret': 'test client seceret',
    }

    return render(request, template, context)
