from django.shortcuts import render
from coach.models import Order

def profile(request):
    orders = Order.objects.all().prefetch_related("ordertoproduct_set")
    order_data = []

    for order in orders:
            for order_item in order.ordertoproduct_set.all():
                if order_item.training_session:
                    training_session_name = order_item.training_session.name
                else:
                    training_session_name = "No Session"
                order_data.append({
                "name":order_item.product_name,
                "price":order_item.price,
                "first_name":order.first_name,
                "last_name":order.last_name,
                "email":order.email,
                "order_total":order.order_total,
                "training_session":training_session_name,
            })

    return render(request, 'coach/profile.html', {'product_data': order_data})