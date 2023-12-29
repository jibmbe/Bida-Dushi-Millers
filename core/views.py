from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Service, Invoice, InvoiceModel
from django.conf import settings
import stripe
from django.views import View

def home(request):
    return render(request, 'core/home.html')

def pricing(request):
    services = Service.objects.all()
    return render(request, 'core/pricing.html', {'services': services})

class PortfolioView(View):
    def get(self, request):
        return render(request, 'core/portfolio.html')

def view_invoice(request, invoice_id):
    # Fetch the InvoiceModel instance or return a 404 response if not found
    invoice = get_object_or_404(InvoiceModel, id=invoice_id)

    # Your view logic here
    context = {
        'invoice': invoice,
    }

    return render(request, 'core/invoice.html', context)

stripe.api_key = settings.STRIPE_SECRET_KEY

def buy_now(request, service_id):
    if request.method == 'POST':
        selected_service = Service.objects.get(pk=service_id)
        buyer_name = request.POST.get('buyer_name')
        buyer_email = request.POST.get('buyer_email')
        payment_method = request.POST.get('payment_method')

        # Create an invoice
        invoice = Invoice.objects.create(
            service=selected_service,
            buyer_name=buyer_name,
            buyer_email=buyer_email
        )

        # Handle payment based on the selected method
        if payment_method == 'card':
            # Use Stripe to process the card payment
            try:
                intent = stripe.PaymentIntent.create(
                    amount=int(selected_service.price * 100),  # Amount in cents
                    currency="usd",
                    payment_method=request.POST.get('payment_method'),
                    confirmation_method="manual",
                    confirm=True,
                )

                # Update payment status (for demonstration purposes)
                invoice.payment_status = True
                invoice.save()

                # Display a success message
                messages.success(request, f'Card payment successful! Invoice #{invoice.id} generated.')
                return redirect('home')

            except stripe.error.CardError as e:
                # Handle card errors
                messages.error(request, f'Card payment error: {e.error.message}')
                return redirect('buy_now', service_id=service_id)

        elif payment_method == 'mpesa':
            # Handle M-Pesa payment (Replace the following code with your actual M-Pesa integration)
            mpesa_phone = request.POST.get('mpesa_phone')
            print('M-Pesa Phone:', mpesa_phone)

            # Placeholder for M-Pesa integration - replace with actual implementation
            messages.success(request, f'M-Pesa payment successful! Invoice #{invoice.id} generated.')
            return redirect('home')  # Redirect to home after successful M-Pesa payment

        else:
            # Handle unsupported payment method
            messages.error(request, 'Unsupported payment method.')
            return redirect('buy_now', service_id=service_id)

    else:
        selected_service = Service.objects.get(pk=service_id)
        return render(request, 'core/buy_now.html', {'service': selected_service})
    
    