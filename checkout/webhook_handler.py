from django.http import HttpResponse


class StripeWH_Handler:
    """ Handles Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle a generic/unknown/unexpected webhook event"""
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """ Handle a payment intent succeeded webhook event"""
        intent = event.data.object
        print(intent, 'wh_handler used')
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """ Handle a payment intent failed webhook event"""
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
