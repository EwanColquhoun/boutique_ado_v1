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
        'stripe_public_key': 'pk_test_51KZFq0E2giPo2Le28UZtqlck08lQe4CPQJwiwdsleDIx8gBETEqI5cvQojPF1RFKxttEQA85zb8X3Sy2MXxnno73005mtUpT02',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
